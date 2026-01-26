# sdxxxl_langflow
自用 Langflow 工具合集。

## 快速开始

### 自动装载节点

运行脚本自动将自定义组件同步到 Langflow：

```powershell
# 在 conda 环境下执行
conda activate <your_env_name>
.\auto_load_nodes.ps1
```

**首次运行**：脚本会设置 `LANGFLOW_COMPONENTS_PATH` 用户环境变量，指向项目目录下的 `custom_components`。

**后续运行**：脚本会将 `custom_components` 下的所有分类目录同步到环境变量指定的目录。

**环境变量已设置的情况**：
- 如果 `LANGFLOW_COMPONENTS_PATH` 已指向其他目录，脚本会将 `custom_components` 下的所有分类复制到该目录
- 无需手动修改环境变量，脚本会自动处理跨目录同步

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

### 使用自定义模型组件

**注意**：模型组件（如 `UniversalOpenAIComponent`）不会出现在组件菜单的分类中。

**使用方法**：
1. 在 Langflow 中添加需要模型的组件（如 Agent、Chat Input 等）
2. 在该组件的配置中，找到 **Model Provider** 选项
3. 选择 **"Connect other models"**
4. 将你的自定义模型组件连接到该端口

这样就可以使用自定义的模型组件了。

### 修复 Langflow 权限问题

如果在 Windows 上运行 Langflow 时遇到权限拒绝错误（如无法访问 `secret_key` 文件），可以使用以下脚本修复：

```powershell
# 必须以管理员身份运行 PowerShell
# 按 Win+X，选择 "Windows PowerShell (管理员)" 或 "终端 (管理员)"
# 然后执行以下命令：
Set-ExecutionPolicy ByPass -Scope Process -Force; & '.\fix_langflow_permission.ps1'
```

**脚本功能**：
- 获取 Langflow 缓存目录的所有权
- 删除旧的 `secret_key` 文件
- 重置目录权限

**注意事项**：
- 必须以管理员身份运行
- 如果 `secret_key` 文件已被删除，脚本会显示相应提示
- 修复完成后，使用 `langflow run` 启动 Langflow
