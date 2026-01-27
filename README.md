# sdxxxl_langflow
自用 Langflow/LangChain 工具合集，主要面向 Windows 平台。

## 快速开始

### 自动装载节点

运行脚本自动将自定义组件同步到 Langflow：

```powershell
# 在 conda 环境下执行
conda activate <your_env_name>
.\auto_load_nodes.ps1
```

**首次运行**：脚本会设置 `LANGFLOW_COMPONENTS_PATH` 用户环境变量，指向项目目录下的 `custom_components`。

**环境变量已设置的情况**：
- 如果 `LANGFLOW_COMPONENTS_PATH` 已指向其他目录，脚本会将 `custom_components` 下的所有分类复制到该目录

> **注意**：设置环境变量后，请重启终端或重新登录使配置生效。

### 自定义组件目录结构

```
custom_components/
├── 分类名称1/      # 每个分类会被自动同步
│   ├── __init__.py
│   └── 组件文件.py
├── 分类名称2/
│   └── ...
└── 分类名称N/
```

添加新分类时，只需在 `custom_components` 下创建新目录，脚本会自动处理。

### 修复 Langflow 权限问题

如果在 Windows 上运行 Langflow 时遇到权限拒绝错误（如无法访问 `secret_key` 文件），可以使用以下脚本修复：

```powershell
# 必须以管理员身份运行 PowerShell
Set-ExecutionPolicy ByPass -Scope Process -Force; & '.\fix_langflow_permission.ps1'
```

**脚本功能**：
- 获取 Langflow 缓存目录的所有权
- 优先尝试修复 `secret_key` 文件权限（保留文件）
- 如果修复失败，会提示是否删除 `secret_key` 文件
- 重置目录权限

**工作流程**：
1. **安全警告**：提示解锁后文件将可被所有用户访问
2. **非破坏性修复**：尝试多种方法修复权限，保留 `secret_key` 文件
3. **破坏性备份**：如果修复失败，询问是否删除 `secret_key`（将丢失所有全局变量中的密钥）

**注意事项**：
- 必须以管理员身份运行 PowerShell
- 脚本会提示数据安全风险，需确认后继续
- 如果 `secret_key` 文件不存在，脚本会显示相应提示
- 修复完成后，使用 `langflow run` 启动 Langflow

## 自定义组件

### UniversalOpenAI

通用 OpenAI 兼容 API 客户端，支持配置 HTTP 代理。

**主要特性**：
- 支持任意 OpenAI 兼容的 API 端点
- 可配置的模型列表（默认、API 获取、自定义）
- 支持 HTTP 代理

**代理配置**：
- 在组件中启用 `Enable Proxy` 开关
- `Proxy URL` 格式：`http://127.0.0.1:7890`
- 仅支持 HTTP 代理，不支持 HTTPS、SOCKS5 等其他协议
- 如果输入格式不正确，会提示正确的使用方式

**使用示例**：
```
# 代理 URL 格式（必须以 http:// 开头）
http://127.0.0.1:7890
http://127.0.0.1:7899
```

## 官方离线文档

本项目集成了 Langflow 和 LangChain 官方文档的离线版本，便于本地查阅和开发参考。

### Langflow 文档

**文档位置**：`docs/langflow/`

包含 **22 个页面**，涵盖：

- **入门指南**：安装、快速开始
- **核心概念**：组件、Flow、Playground、发布
- **开发指南**：应用开发、自定义组件
- **部署相关**：部署概述、故障排除
- **高级功能**：MCP Server/MClient、Agents Tools

### LangChain 文档

**文档位置**：`docs/langchain/`

包含 **678 个页面**，涵盖：

#### API 参考
- `docs/langchain/api-reference/` - Auth Service、Deployments、Integrations、Listeners、Sandboxes 等 API

#### LangSmith 平台
- `docs/langchain/langsmith/` - 完整的 LangSmith 平台文档
  - **Agent Builder**：无代码 agent 创建、模板、工具、远程 MCP 服务器
  - **Agent Server**：分布式追踪、扩缩容、Webhooks
  - **Evaluation**：评估方法、数据集、实验对比
  - **Deployments**：自部署（AWS、Azure、GCP）、混合部署、云部署
  - **Observability**：追踪、日志、监控
  - **Authentication**：多种认证方式、API 密钥、自定义认证

#### 开源框架
- LangChain、LangGraph、Deep Agents 的完整文档

### 搜索索引

项目提供了搜索索引文件：

- `docs/langflow/search_index.json` - 22 个 Langflow 页面的索引
- `docs/langchain/search_index.json` - 678 个 LangChain 页面的索引

索引包含页面的标题、路径和描述信息，支持程序化搜索。

### 更新文档

运行以下命令可获取最新版本的文档：

```powershell
python download_langchain_docs.py
python download_langflow_docs.py
```

**注意**：Langchain 文档基于官方 `llms.txt` 索引下载。请在非高峰期运行脚本，或等待本项目更新，避免对官方服务器造成压力。
