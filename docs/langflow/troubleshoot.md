# Troubleshoot Langflow | Langflow Documentation

- Support
- Troubleshoot

On this page# Troubleshoot Langflow

[data-ch-theme="github-dark"] {  --ch-t-colorScheme: dark;--ch-t-foreground: #c9d1d9;--ch-t-background: #0d1117;--ch-t-lighter-inlineBackground: #0d1117e6;--ch-t-editor-background: #0d1117;--ch-t-editor-foreground: #c9d1d9;--ch-t-editor-lineHighlightBackground: #6e76811a;--ch-t-editor-rangeHighlightBackground: #ffffff0b;--ch-t-editor-infoForeground: #3794FF;--ch-t-editor-selectionBackground: #264F78;--ch-t-focusBorder: #1f6feb;--ch-t-tab-activeBackground: #0d1117;--ch-t-tab-activeForeground: #c9d1d9;--ch-t-tab-inactiveBackground: #010409;--ch-t-tab-inactiveForeground: #8b949e;--ch-t-tab-border: #30363d;--ch-t-tab-activeBorder: #0d1117;--ch-t-editorGroup-border: #30363d;--ch-t-editorGroupHeader-tabsBackground: #010409;--ch-t-editorLineNumber-foreground: #6e7681;--ch-t-input-background: #0d1117;--ch-t-input-foreground: #c9d1d9;--ch-t-input-border: #30363d;--ch-t-icon-foreground: #8b949e;--ch-t-sideBar-background: #010409;--ch-t-sideBar-foreground: #c9d1d9;--ch-t-sideBar-border: #30363d;--ch-t-list-activeSelectionBackground: #6e768166;--ch-t-list-activeSelectionForeground: #c9d1d9;--ch-t-list-hoverBackground: #6e76811a;--ch-t-list-hoverForeground: #c9d1d9; }This page provides troubleshooting advice for issues you might encounter when using Langflow or contributing to Langflow.

## Missing components​

As Langflow development continues, components are often recategorized or deprecated for better alignment or to prepare for new components.

If a component appears to be missing from the  Core components and  menus, try the following:

- Search for the component.
- Check other component categories and  Bundles.
- Check legacy components, which are hidden by default.
- Check the Changelog for component changes in recent releases.
- Make sure the component isn't already present in your flow if it is a single-use component.

If you still cannot locate the component, see Langflow GitHub Issues and Discussions.

## No input in the Playground​

If there is no message input field in the Playground, make sure your flow has a Chat Input component that is connected, directly or indirectly, to the Input port of a Language Model or Agent component.

Because the Playground is designed for flows that use an LLM in a query-and-response format, such as chatbots and agents, a flow must have Chat Input, Language Model/Agent, and Chat Output components to be fully supported by the Playground chat interface.

For more information, see Test flows in the Playground.

## Missing key, no key found, or invalid API key​

If you get an API key error when running a flow, try the following:

- For all components that require credentials, make sure those components have a valid credential in the component's settings, such as the API Key field.
- If you store your credentials in Langflow global variables, make sure you selected the correct global variable and that the variable contains a valid credential.
- Make sure the provided credentials are active, have the required permissions, and, if applicable, have sufficient funds in the account to execute the required action. For example, model providers require credits to use their LLMs.

## Langflow installation issues​

The following issues can occur when installing Langflow.

### Langflow installation freezes at pip dependency resolution​

Installing Langflow OSS with pip install langflow slowly fails with this error message:

`_10pip is looking at multiple versions of <<library>> to determine which version is compatible with other requirements. This could take a while.`To work around this issue, install Langflow with uv instead of pip, as explained in Install and run the Langflow OSS Python package.

### Linux installation fails to build required package​

When you try to install Langflow OSS on Linux, installation fails because of outdated or missing packages:

`_10Resolved 455 packages in 18.92s_10  × Failed to build `webrtcvad==2.0.10`_10  ├─▶ The build backend returned an error_10  ╰─▶ Call to `setuptools.build_meta:__legacy__.build_wheel` failed (exit status: 1)`To resolve this error, install the required build dependencies, and then retry the Langflow installation:

`_10sudo apt-get update_10sudo apt-get install build-essential python3-dev`If upgrading your packages doesn't fix the issue, install gcc separately, and then retry the Langflow installation:

`_10sudo apt-get install gcc`### Installation failure from webrtcvad package​

If you experience an error from the webrtcvad package, run uv pip install webrtcvad-wheels in your virtual environment, and then retry the Langflow installation.

### Protocol buffers (protoc) required for Intel-based Macs​

If you're installing Langflow on an Intel-based Mac, you may encounter installation errors if Protocol Buffers Compiler (protoc) is not installed.

This requirement doesn't apply to Apple Silicon Macs on ARM64.

To resolve this issue, install protoc using brew install protobuf.

For more information, including alternative installation methods, see the Protocol buffers installation documentation.

### C++ build tools required for Langflow Desktop on Windows​

Microsoft Windows installations of Langflow Desktop require a C++ compiler that may not be present on your system. If you receive a C++ Build Tools Required! error, follow the on-screen prompt to install Microsoft C++ Build Tools, or install Microsoft Visual Studio.

## Langflow startup issues​

The following issues can occur when attempting to start Langflow.

### No langflow.__main__ module​

When you try to run Langflow with the command langflow run, you encounter the following error:

`_10> No module named 'langflow.__main__'`To resolve this issue, try the following:

1. Run uv run langflow run instead of langflow run.
2. If that doesn't work, reinstall the latest Langflow version with uv pip install langflow -U.
3. If that doesn't work, reinstall Langflow and its dependencies with uv pip install langflow --pre -U --force-reinstall.

### Langflow runTraceback​

When you try to run Langflow using the command langflow run, you encounter the following error:

`_10> langflow runTraceback (most recent call last): File ".../langflow", line 5, in <module>  from langflow.__main__ import mainModuleNotFoundError: No module named 'langflow.__main__'`There are two possible reasons for this error:

- Multiple Langflow installations: You installed Langflow using pip install langflow but you already had a previous version of Langflow installed in your system. In this case, you might be running the wrong executable.
To solve this issue, run the correct executable by running python -m langflow run instead of langflow run.
If that doesn't work, try uninstalling and reinstalling Langflow with uv pip install langflow --pre -U.
- Version conflict during installation: Some version conflicts might have occurred during the installation process. To resolve this issue, reinstall Langflow and its dependencies by running python -m pip install langflow --pre -U --force-reinstall.

### Environment variables not available from terminal​

Environment variables set in your terminal aren't automatically available to GUI-based applications like Langflow Desktop when launched through the Finder or the Start Menu.
To set environment variables for Langflow Desktop, see Set environment variables for Langflow Desktop.

### Access Langflow Desktop startup logs​

If you encounter issues with Langflow Desktop, you might need to access Langflow Desktop startup logs for debugging.

### User not found or inactive when running multiple flows​

When running multiple local Langflow OSS instances on different ports, such as localhost:7860 and localhost:7861, you might see authentication errors in the logs.
For example:

`_10[07/22/25 10:57:07] INFO     2025-07-22 10:57:07 - INFO     - utils - User not found or inactive.`To resolve this error, use separate browser instances or browser profiles to access each Langflow instance.

### Package is not installed​

In Langflow OSS, you can follow the error message's instructions to install the missing dependency.

To manage dependencies in Langflow Desktop, see Install custom dependencies in Langflow Desktop.

### PostgreSQL asyncpg driver compatibility issue​

The following error can occur when initializing Langflow with a PostgreSQL database:

`_10sqlalchemy.exc.DBAPIError: (sqlalchemy.dialects.postgresql.asyncpg.Error) <class 'asyncpg.exceptions.DataError'>: invalid input for query argument $7: datetime.datetime(2025, 10, 31, 14, 8, 5... (can't subtract offset-naive and offset-aware datetimes)`This error occurs because asyncpg has stricter timezone handling than psycopg2, and is not fully compatible with Langflow's current database schema.

To resolve this issue, remove asyncpg from your installation and use psycopg2 instead.

### An API key must be passed as query or header​

The following error can occur when attempting to sign up on the Langflow sign in page: An API key must be passed as query or header.

This means that LANGFLOW_AUTO_LOGIN is set to false, and only superusers can create and activate non-superuser accounts.
Therefore, you are locked out of this Langflow instance.

If you aren't an administrator, then a superuser must create and activate a non-superuser account before you can sign in.

If you are the administrator, sign in with a superuser account, or restart Langflow with LANGFLOW_AUTO_LOGIN=true.

For more information, see Start Langflow Server with authentication enabled.

## Langflow upgrade issues​

The following issues can occur when upgrading your Langflow version.

For information about managing Langflow versions, see Install Langflow.

### Something went wrong running migrations​

The following error can occur during Langflow upgrades when the new version can't override langflow-pre.db in the Langflow cache folder:

`_10> Something went wrong running migrations. Please, run 'langflow migration --fix'`To resolve this error, clear the cache by deleting the contents of your Langflow cache folder.
The filepath depends on your operating system, installation type, and configuration options.
For more information and default filepaths, see Memory management options.

dangerClearing the cache erases your settings.
If you want to retain your settings files, create a backup of those files before clearing the cache folder.

### Langflow Desktop says it is running the latest version, but it is actually behind​

If you are running Langflow Desktop version 1.4.2 or earlier, the UI might incorrectly report that you are on the latest version when a newer version is available.

This happens because the automatic update feature in the UI was introduced in version 1.4.2.
Earlier versions can't automatically detect or apply updates.

To resolve this issue, uninstall Langflow Desktop, and then download and install the latest version of Langflow Desktop.

### 422 error when freezing components after upgrading Pydantic/FastAPI dependencies​

If you locally upgrade your Pydantic and FastAPI dependencies, you may encounter a 422 error when trying to freeze components.

This error occurs due to changes in how request bodies are handled in newer versions of these dependencies.

If you're experiencing this issue, update your Langflow installation to version 1.6.5 or later, which includes a fix for this issue.

`_10uv pip install langflow -U`## Langflow uninstall issues​

The following issues can occur when uninstalling Langflow.

### Dot directory isn't deleted when uninstalling Langflow Desktop on macOS​

On macOS, uninstalling Langflow Desktop deletes the .app file but doesn't delete files in ~/.langflow, which includes files generated during usage like cache and settings.

If you reinstall Langflow Desktop, it starts with the existing data from the previous installation.

To fully remove a Langflow Desktop macOS installation, you must also delete ~/.langflow:

`_10rm -rf .langflow`## Langflow MCP issues​

The following issues can occur when using Langflow as an MCP server or client.

### Claude for Desktop doesn't use MCP server tools correctly​

If Claude for Desktop doesn't use your server's tools correctly, try explicitly defining the path to your local uvx or npx executable file in the claude_desktop_config.json configuration file:

1. To find your uvx path, run which uvx.
To find your npx path, run which npx.
2. In your claude_desktop_config.json file, add the path to your Langflow MCP server configuration, as shown in the following examples.
uvxnpx_11{_11  "mcpServers": {_11    "PROJECT_NAME": {_11      "command": "PATH_TO_UVX",_11      "args": [_11        "mcp-proxy",_11        "http://LANGFLOW_SERVER_ADDRESS/api/v1/mcp/project/PROJECT_ID/streamable"_11      ]_11    }_11  }_11}_13{_13  "mcpServers": {_13    "PROJECT_NAME": {_13      "command": "PATH_TO_NPX",_13      "args": [_13        "-y",_13        "supergateway",_13        "--sse",_13        "http://LANGFLOW_SERVER_ADDRESS/api/v1/mcp/project/PROJECT_ID/streamable"_13      ]_13    }_13  }_13}

### MCP browser-based flows don't open a browser on Windows​

This is a known issue when using MCP Tools with browser navigation actions, such as Playwright, on Windows: The agent can execute the tool successfully but the browser tab or window doesn't open.

This issue occurs because the MCP server runs from a Python process, which prevents it from opening browser windows in WSL or Windows.

To work around this issue, use the standalone MCP server approach documented in the Playwright MCP repository.
After the server is up and running, you can add it as an HTTP/SSE server in Langflow.

For other browser navigation tools, see the provider's documentation for specific troubleshooting guidance.

### "No tools or prompts connected" on MCP servers in mixed Windows/WSL environments​

If you encounter "No tools or prompts connected" errors or connection failures when using Langflow Desktop as an MCP server with clients running in different environments, such as Langflow on a Windows host and an MCP client in WSL, this is due to network isolation between Windows and WSL environments.

WSL cannot directly access Windows localhost services, and Langflow running on a Windows host is not accessible from WSL clients at localhost:7860.

To work around this issue, run the server and host in the same operating environment.

Alternatively, configure Langflow Desktop to accept connections from WSL at the default Windows IP address of 10.255.255.254:7860 instead of localhost.

### MCP Tools component loses Tool Mode option after upgrading flows​

If you upgrade an existing flow that uses the MCP Tools component in Tool Mode, the component might lose its Tool Mode setting after upgrading the flow.
This can break flows that rely on the component's Tool Mode to expose MCP tools to agents.

If you experience this when upgrading a flow that you created in Langflow version 1.7.1 or earlier, do the following:

1. Select the MCP Tools component in your flow.
2. Click  Code to open the component's code editor.
3. In the component's template structure, locate the tool_mode field under inputs.
The field can be either missing or set to false.
4. Add the tool_mode field if it's missing, and set it to true:
_10tool_mode = True
5. Click Check & Save to apply the code changes.

## Token length limit errors in Embedding Model components​

Token length errors can happen if your chunking strategy doesn't align with your embedding model's tokenization limits.
For more information, see Tokenization errors due to chunk size.

## Document processing errors in Docker containers​

If you're running Langflow in a Docker container, you might encounter errors when using components that handle files or images, such as the Read File component or Docling components. To resolve these errors, you might need to install additional system dependencies.

When running Langflow in a Linux-based Docker container, Docling requires system libraries that aren't included in the base Docker image. If you see errors related to document or image processing, add the following to your Dockerfile:

`_10RUN apt-get update && apt-get install -y libgl1 libglib2.0-0`These dependencies are required by Docling for document processing operations.

For more information about customizing Docker images, see Customize the Langflow Docker image with your own code.

## Custom components and integrations issues​

For troubleshooting advice for a third-party integration, see the information about that integration in the Langflow documentation and the provider's documentation.

If you are building a custom component, see Error handling and logging for custom Python components.

### Custom components not appearing in the visual editor​

If your custom components are not appearing in the Langflow visual editor, try the following troubleshooting steps:

1. Ensure your components follow the required directory structure.
_10/your/custom/components/path/       # Base directory set by LANGFLOW_COMPONENTS_PATH_10    └── category_name/              # Required category subfolder that determines menu name_10        ├── __init__.py             # Required_10        └── custom_component.py     # Component file
2. Verify each category directory includes an __init__.py file.
This is required for Python to recognize the directory as a module.
3. Use the command line argument instead of the environment variable for LANGFLOW_COMPONENTS_PATH.
If you're using the LANGFLOW_COMPONENTS_PATH environment variable and components aren't loading, try the --components-path command line argument instead:
_10uv run langflow run --components-path /path/to/your/custom/components

If you continue to experience issues, please report them on GitHub with details about your directory structure and component setup.

## See also​

- Langflow GitHub Issues and Discussions
- Langflow telemetry
