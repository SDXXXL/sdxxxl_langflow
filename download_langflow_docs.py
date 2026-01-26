#!/usr/bin/env python3
"""
LangFlow 官方文档下载脚本 - 完整版
将 https://docs.langflow.org/ 的文档下载到本地，保存为 Markdown 格式
"""

import requests
from bs4 import BeautifulSoup
import os
import json
import re
from urllib.parse import urljoin, urlparse
import time

BASE_URL = "https://docs.langflow.org/"
OUTPUT_DIR = os.path.join(os.path.dirname(__file__), "docs", "langflow")
SESSION = requests.Session()
SESSION.headers.update({
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
})

visited_urls = set()
downloaded_pages = []


def clean_text(text):
    if not text:
        return ""
    lines = (line.strip() for line in text.splitlines())
    return '\n'.join(line for line in lines if line)


def html_to_markdown(html_content, page_url):
    if not html_content:
        return ""

    soup = BeautifulSoup(html_content, 'html.parser')

    title = ""
    title_tag = soup.find('title')
    if title_tag:
        title = clean_text(title_tag.get_text())
    else:
        h1 = soup.find('h1')
        if h1:
            title = clean_text(h1.get_text())

    main_content = None
    for selector in ['article', 'main', '[role="main"]', '.md-content', '.content', '#main-content']:
        main_content = soup.select_one(selector)
        if main_content:
            break
    if not main_content:
        main_content = soup.body

    def convert_element(element):
        if element.name in ['h1', 'h2', 'h3', 'h4', 'h5', 'h6']:
            level = int(element.name[1])
            text = clean_text(element.get_text())
            return f"{'#' * level} {text}\n\n" if text else ""
        elif element.name == 'p':
            text = clean_text(element.get_text())
            return f"{text}\n\n" if text else ""
        elif element.name == 'a':
            href = element.get('href', '')
            text = clean_text(element.get_text())
            if href and text and not href.startswith(('mailto:', 'tel:', '#')):
                if not href.startswith('http'):
                    href = urljoin(page_url, href)
                return f"[{text}]({href})"
            return text
        elif element.name in ['strong', 'b']:
            text = clean_text(element.get_text())
            return f"**{text}**" if text else ""
        elif element.name in ['em', 'i']:
            text = clean_text(element.get_text())
            return f"*{text}*" if text else ""
        elif element.name == 'code':
            text = clean_text(element.get_text())
            return f"`{text}`"
        elif element.name == 'pre':
            code = element.find('code')
            text = clean_text(code.get_text()) if code else clean_text(element.get_text())
            return f"\n```\n{text}\n```\n\n" if text else ""
        elif element.name == 'ul':
            result = ""
            for li in element.find_all('li', recursive=False):
                text = clean_text(li.get_text())
                if text:
                    result += f"- {text}\n"
            return result + "\n" if result else ""
        elif element.name == 'ol':
            result = ""
            for idx, li in enumerate(element.find_all('li', recursive=False), 1):
                text = clean_text(li.get_text())
                if text:
                    result += f"{idx}. {text}\n"
            return result + "\n" if result else ""
        elif element.name == 'blockquote':
            text = clean_text(element.get_text())
            result = ""
            for line in text.split('\n'):
                result += f"> {line}\n"
            return result + "\n"
        elif element.name == 'hr':
            return "\n---\n\n"
        elif element.name in ['span', 'div']:
            result = ""
            for child in element.children:
                if hasattr(child, 'name') and child.name:
                    result += convert_element(child)
                else:
                    text = clean_text(str(child))
                    if text:
                        result += text
            return result
        else:
            result = ""
            for child in element.children:
                if hasattr(child, 'name') and child.name:
                    result += convert_element(child)
                else:
                    text = clean_text(str(child))
                    if text:
                        result += text
            return result

    content = ""
    if main_content:
        for child in main_content.children:
            if hasattr(child, 'name') and child.name:
                content += convert_element(child)
            else:
                text = clean_text(str(child))
                if text:
                    content += text + "\n"

    full_markdown = f"# {title}\n\n"
    if content.strip():
        full_markdown += content.strip() + "\n"

    return full_markdown


def get_all_documentation_urls(start_url):
    all_urls = set()
    all_urls.add(start_url)

    try:
        response = SESSION.get(start_url, timeout=30)
        if response.status_code != 200:
            return all_urls

        soup = BeautifulSoup(response.text, 'html.parser')

        nav_selectors = [
            'nav', 'aside', '.sidebar', '.nav', '[class*="nav"]',
            '[class*="sidebar"]', '#sidebar', '.md-nav',
            '[role="navigation"]', '[aria-label*="nav"]'
        ]
        for selector in nav_selectors:
            nav = soup.select_one(selector)
            if nav:
                for link in nav.find_all('a', href=True):
                    href = link.get('href')
                    full_url = urljoin(start_url, href)
                    parsed = urlparse(full_url)
                    if parsed.netloc != urlparse(start_url).netloc:
                        continue
                    if any(ext in href.lower() for ext in ['.pdf', '.zip', '.png', '.jpg', '.jpeg', '.gif', '.svg', '.ico']):
                        continue
                    if '#' in full_url:
                        full_url = full_url.split('#')[0]
                    if full_url not in all_urls:
                        all_urls.add(full_url)

        for link in soup.find_all('a', href=True):
            href = link.get('href')
            if not href:
                continue
            full_url = urljoin(start_url, href)
            parsed = urlparse(full_url)
            if parsed.netloc != urlparse(start_url).netloc:
                continue
            path = parsed.path
            if any(ext in path.lower() for ext in ['.pdf', '.zip', '.png', '.jpg', '.jpeg', '.gif', '.svg', '.ico']):
                continue
            if '#' in full_url:
                full_url = full_url.split('#')[0]
            if full_url not in all_urls and 'docs.langflow.org' in full_url:
                all_urls.add(full_url)

        for script in soup.find_all('script'):
            if script.string:
                script_content = script.string
                url_pattern = r'["\']([^"\']*(?:docs\.langflow\.org|/docs/)[^"\']*)["\']'
                matches = re.findall(url_pattern, script_content)
                for match in matches:
                    if not match.startswith('http'):
                        match = urljoin(start_url, match)
                    parsed = urlparse(match)
                    if parsed.netloc == urlparse(start_url).netloc and match not in all_urls:
                        if not any(ext in match.lower() for ext in ['.pdf', '.zip', '.png', '.jpg', '.gif']):
                            all_urls.add(match)

        json_ld = soup.find_all('script', type='application/ld+json')
        for script in json_ld:
            if script.string:
                try:
                    import json
                    data = json.loads(script.string)
                    if isinstance(data, dict):
                        if '@graph' in data:
                            for item in data['@graph']:
                                if isinstance(item, dict) and 'url' in item:
                                    url = item['url']
                                    if 'docs.langflow.org' in url and url not in all_urls:
                                        all_urls.add(url)
                except:
                    pass

    except Exception as e:
        print(f"  获取链接时出错: {e}")

    return all_urls


def download_page(url):
    try:
        response = SESSION.get(url, timeout=30)
        if response.status_code == 200:
            return response.text
    except Exception as e:
        print(f"  下载失败 {url}: {e}")
    return None


def save_markdown(content, url, output_dir):
    if not content:
        return None

    markdown = html_to_markdown(content, url)

    parsed = urlparse(url)
    path = parsed.path

    if path == '/' or path == '':
        filename = 'index.md'
        filepath = os.path.join(output_dir, filename)
    else:
        path = path.rstrip('/')
        parts = [p for p in path.split('/') if p and p not in ['docs', 'langflow.org']]
        if not parts:
            filename = 'index.md'
            filepath = os.path.join(output_dir, filename)
        else:
            folder_path = output_dir
            for i, part in enumerate(parts[:-1]):
                folder_path = os.path.join(folder_path, part)
                os.makedirs(folder_path, exist_ok=True)

            last_part = parts[-1]
            if '.' not in last_part:
                filename = last_part + '.md'
            else:
                filename = last_part
            filepath = os.path.join(folder_path, filename)

    os.makedirs(os.path.dirname(filepath) if os.path.dirname(filepath) else output_dir, exist_ok=True)

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(markdown)

    return filepath


def create_search_index(downloaded_pages, output_dir):
    index_data = {
        'total_pages': len(downloaded_pages),
        'base_url': BASE_URL,
        'updated': time.strftime('%Y-%m-%d %H:%M:%S'),
        'pages': downloaded_pages
    }

    index_file = os.path.join(output_dir, 'search_index.json')
    with open(index_file, 'w', encoding='utf-8') as f:
        json.dump(index_data, f, ensure_ascii=False, indent=2)

    return index_file


def create_readme(output_dir, page_count):
    readme_content = f"""# LangFlow Documentation

本地保存的 LangFlow 官方文档。

## 使用说明

- 所有文档已转换为 Markdown 格式
- 可以使用任意文本编辑器或 IDE 搜索文档内容
- `search_index.json` 包含所有 {page_count} 个页面的索引信息

## 页面列表

请查看 `search_index.json` 获取完整页面列表。

## 更新日期

{time.strftime('%Y-%m-%d %H:%M:%S')}

原始文档: https://docs.langflow.org/
"""
    readme_file = os.path.join(output_dir, 'README.md')
    with open(readme_file, 'w', encoding='utf-8') as f:
        f.write(readme_content)


def main():

    print("=" * 60)
    print("LangFlow 官方文档下载工具 (完整版)")
    print("=" * 60)
    print(f"\n目标 URL: {BASE_URL}")
    print(f"输出目录: {OUTPUT_DIR}\n")

    os.makedirs(OUTPUT_DIR, exist_ok=True)

    print("正在获取所有文档页面链接...")
    page_urls = get_all_documentation_urls(BASE_URL)
    page_list = sorted(page_urls)
    print(f"找到 {len(page_list)} 个页面\n")

    downloaded_pages = []

    print("开始下载页面...")
    for idx, url in enumerate(page_list, 1):
        print(f"  [{idx}/{len(page_list)}] {url}", end=" ")

        if url in visited_urls:
            print("⏭")
            continue
        visited_urls.add(url)

        content = download_page(url)
        if content:
            filepath = save_markdown(content, url, OUTPUT_DIR)
            if filepath:
                rel_path = os.path.relpath(filepath, OUTPUT_DIR)

                soup = BeautifulSoup(content, 'html.parser')
                title_tag = soup.find('title')
                title = clean_text(title_tag.get_text()) if title_tag else url

                downloaded_pages.append({
                    'url': url,
                    'title': title,
                    'filepath': rel_path
                })
                print("✓")
            else:
                print("✗")
        else:
            print("✗")

        time.sleep(0.5)

    print(f"\n下载完成，共 {len(downloaded_pages)} 个页面")

    if downloaded_pages:
        print("\n正在生成搜索索引...")
        index_file = create_search_index(downloaded_pages, OUTPUT_DIR)
        print(f"搜索索引已保存至: {index_file}")

        create_readme(OUTPUT_DIR, len(downloaded_pages))

    print("\n" + "=" * 60)
    print("下载完成!")
    print(f"文档已保存到: {OUTPUT_DIR}")
    print("可以使用任何文本编辑器或 IDE 搜索文档内容")
    print("=" * 60)


if __name__ == "__main__":
    main()
