#!/usr/bin/env python3
"""
LangChain 官方文档下载脚本 - 完整内容版
使用 llms.txt 索引，下载实际文档内容
"""

import requests
from bs4 import BeautifulSoup
import os
import json
import re
from urllib.parse import urljoin, urlparse
import time

BASE_URL = "https://docs.langchain.com/"
LLMS_TXT_URL = "https://docs.langchain.com/llms.txt"
OUTPUT_DIR = os.path.join(os.path.dirname(__file__), "docs", "langchain")
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


def parse_llms_txt(llms_content):
    """从 llms.txt 中解析出所有文档链接"""
    links = []
    
    lines = llms_content.split('\n')
    i = 0
    while i < len(lines):
        line = lines[i].strip()
        if not line:
            i += 1
            continue
        
        match = re.match(r'- \[([^\]]+)\]\(([^)]+)\)(?::\s*(.*))?', line)
        if match:
            title = match.group(1).strip()
            url = match.group(2).strip()
            description = match.group(3).strip() if match.group(3) else ""
            
            if url.endswith('.md') and 'docs.langchain.com' in url:
                # 保留 .md 后缀，直接获取 Markdown 内容
                if not url.startswith('http'):
                    url = urljoin(BASE_URL, url)
                
                next_line = lines[i + 1].strip() if i + 1 < len(lines) else ""
                if next_line and not next_line.startswith('- ['):
                    description = next_line
                
                links.append({
                    'title': title,
                    'url': url,  # 保留 .md 后缀
                    'description': description
                })
        
        i += 1
    
    return links


def extract_content_from_html(html_content, page_url):
    """从 Markdown 内容中提取文本（带 .md 后缀的 URL 直接返回纯 Markdown）"""
    if not html_content:
        return None
    
    # 直接使用 Markdown 内容
    markdown = html_content.strip()
    
    if not markdown:
        return None
    
    return markdown


def download_page(url):
    """下载单个页面"""
    try:
        response = SESSION.get(url, timeout=30)
        if response.status_code == 200:
            return response.text
    except Exception as e:
        print(f"  下载失败 {url}: {e}")
    return None


def save_markdown(content, url, doc_info, output_dir):
    """保存 Markdown 文件"""
    title = doc_info['title'] if doc_info else "Untitled"
    description = doc_info.get('description', '')
    
    if content:
        markdown = extract_content_from_html(content, url)
        if markdown:
            parsed = urlparse(url)
            path = parsed.path
            
            if path == '/' or path == '':
                filename = 'index.md'
                filepath = os.path.join(output_dir, filename)
            else:
                path = path.rstrip('/').rstrip('\\')
                parts = [p for p in path.split('/') if p and p not in ['docs', 'langchain.com']]
                if not parts:
                    filename = 'index.md'
                    filepath = os.path.join(output_dir, filename)
                else:
                    folder_path = output_dir
                    for i, part in enumerate(parts[:-1]):
                        folder_path = os.path.join(folder_path, part)
                        os.makedirs(folder_path, exist_ok=True)
                    
                    last_part = parts[-1]
                    last_part = last_part.replace('\\', '').replace('/', '').replace(':', '').replace('*', '').replace('?', '').replace('"', '').replace('<', '').replace('>', '').replace('|', '')
                    if '.' not in last_part:
                        filename = last_part + '.md'
                    else:
                        filename = last_part
                    filepath = os.path.join(folder_path, filename)
            
            os.makedirs(os.path.dirname(filepath) if os.path.dirname(filepath) else output_dir, exist_ok=True)
            
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(markdown)
            
            return filepath
    
    # 如果提取失败，至少保存标题和描述
    markdown = f"# {title}\n\n"
    if description:
        markdown += f"{description}\n\n"
    markdown += f"\n**原始链接**: [{url}]({url})\n"
    
    parsed = urlparse(url)
    path = parsed.path
    filename = path.split('/')[-1] if path else 'index'
    if not filename.endswith('.md'):
        filename += '.md'
    
    filepath = os.path.join(output_dir, filename)
    os.makedirs(os.path.dirname(filepath) if os.path.dirname(filepath) else output_dir, exist_ok=True)
    
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(markdown)
    
    return filepath


def create_search_index(downloaded_pages, output_dir):
    """创建搜索索引"""
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
    """创建 README 文件"""
    readme_content = f"""# LangChain Documentation

本地保存的 LangChain 官方文档。

## 使用说明

- 所有文档已转换为 Markdown 格式
- 可以使用任意文本编辑器或 IDE 搜索文档内容
- `search_index.json` 包含所有 {page_count} 个页面的索引信息

## 更新日期

{time.strftime('%Y-%m-%d %H:%M:%S')}

原始文档索引: {LLMS_TXT_URL}

## 注意事项

文档内容基于 llms.txt 索引从官方文档网站下载。
由于 LangChain 文档使用 JavaScript 动态渲染技术，部分页面内容可能不完整。
如需获取完整最新内容，请访问原始文档链接。
"""
    readme_file = os.path.join(output_dir, 'README.md')
    with open(readme_file, 'w', encoding='utf-8') as f:
        f.write(readme_content)


def main():
    print("=" * 60)
    print("LangChain 官方文档下载工具 (完整内容版)")
    print("=" * 60)
    print(f"\n文档索引: {LLMS_TXT_URL}")
    print(f"输出目录: {OUTPUT_DIR}\n")
    
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    
    print("正在下载 llms.txt 索引文件...")
    try:
        llms_response = SESSION.get(LLMS_TXT_URL, timeout=30)
        if llms_response.status_code != 200:
            print("  下载 llms.txt 失败!")
            return
        llms_content = llms_response.text
        print(f"  llms.txt 下载成功 ({len(llms_content)} 字符)\n")
    except Exception as e:
        print(f"  下载 llms.txt 失败: {e}")
        return
    
    print("正在解析文档链接...")
    doc_links = parse_llms_txt(llms_content)
    print(f"  找到 {len(doc_links)} 个文档链接\n")
    
    downloaded_pages = []
    
    print("开始下载文档 (这可能需要几分钟)...")
    for idx, doc in enumerate(doc_links, 1):
        url = doc['url']
        title = doc['title']
        
        if idx % 50 == 0:
            print(f"  进度: [{idx}/{len(doc_links)}] {title[:30]}...")
        else:
            print(f"  [{idx}/{len(doc_links)}] {title[:40]}", end=" ")
        
        if url in visited_urls:
            print("⏭")
            continue
        visited_urls.add(url)
        
        content = download_page(url)
        filepath = save_markdown(content, url, doc, OUTPUT_DIR)
        
        if filepath:
            rel_path = os.path.relpath(filepath, OUTPUT_DIR)
            downloaded_pages.append({
                'url': url,
                'title': title,
                'filepath': rel_path,
                'description': doc['description']
            })
            print("✓")
        else:
            print("✗")
        
        time.sleep(0.3)
    
    print(f"\n下载完成，共 {len(downloaded_pages)} 个页面")
    
    if downloaded_pages:
        print("\n正在生成搜索索引...")
        index_file = create_search_index(downloaded_pages, OUTPUT_DIR)
        print(f"  搜索索引已保存至: {index_file}")
        
        create_readme(OUTPUT_DIR, len(downloaded_pages))
        
        print(f"\n文档统计:")
        print(f"  - 总页面数: {len(downloaded_pages)}")
        
        categories = {}
        for page in downloaded_pages:
            path = page['filepath']
            parts = path.split(os.sep)
            if len(parts) > 1:
                category = parts[0]
                categories[category] = categories.get(category, 0) + 1
        
        for category, count in sorted(categories.items(), key=lambda x: -x[1])[:10]:
            print(f"  - {category}: {count} 个文件")
        
        if len(categories) > 10:
            other_count = sum(categories.values()) - sum([v for k, v in list(categories.items())[:10]])
            print(f"  - 其他类别: {other_count} 个文件")
    
    print("\n" + "=" * 60)
    print("下载完成!")
    print(f"文档已保存到: {OUTPUT_DIR}")
    print("=" * 60)


if __name__ == "__main__":
    main()
