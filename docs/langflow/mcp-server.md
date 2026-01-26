# Use Langflow as an MCP server | Langflow Documentation

- Model Context Protocol (MCP)
- Use Langflow as an MCP server

On this page# Use Langflow as an MCP server

[data-ch-theme="github-dark"] {  --ch-t-colorScheme: dark;--ch-t-foreground: #c9d1d9;--ch-t-background: #0d1117;--ch-t-lighter-inlineBackground: #0d1117e6;--ch-t-editor-background: #0d1117;--ch-t-editor-foreground: #c9d1d9;--ch-t-editor-lineHighlightBackground: #6e76811a;--ch-t-editor-rangeHighlightBackground: #ffffff0b;--ch-t-editor-infoForeground: #3794FF;--ch-t-editor-selectionBackground: #264F78;--ch-t-focusBorder: #1f6feb;--ch-t-tab-activeBackground: #0d1117;--ch-t-tab-activeForeground: #c9d1d9;--ch-t-tab-inactiveBackground: #010409;--ch-t-tab-inactiveForeground: #8b949e;--ch-t-tab-border: #30363d;--ch-t-tab-activeBorder: #0d1117;--ch-t-editorGroup-border: #30363d;--ch-t-editorGroupHeader-tabsBackground: #010409;--ch-t-editorLineNumber-foreground: #6e7681;--ch-t-input-background: #0d1117;--ch-t-input-foreground: #c9d1d9;--ch-t-input-border: #30363d;--ch-t-icon-foreground: #8b949e;--ch-t-sideBar-background: #010409;--ch-t-sideBar-foreground: #c9d1d9;--ch-t-sideBar-border: #30363d;--ch-t-list-activeSelectionBackground: #6e768166;--ch-t-list-activeSelectionForeground: #c9d1d9;--ch-t-list-hoverBackground: #6e76811a;--ch-t-list-hoverForeground: #c9d1d9; }Langflow integrates with the Model Context Protocol (MCP) as both an MCP server and an MCP client.

This page describes how to use Langflow as an MCP server that exposes your flows as tools that MCP clients can use when generating responses.

Langflow MCP servers support both the streamable HTTP transport and Server-Sent Events (SSE) as a fallback.

For information about using Langflow as an MCP client and managing MCP server connections within flows, see Use Langflow as an MCP client.

## Prerequisites​

- A Langflow project with at least one flow that has a Chat Output component.
The Chat Output component is required to use a flow as an MCP tool.
- Any LTS version of Node.js installed on your computer if you want to use MCP Inspector to test and debug flows.
- ngrok installed and an ngrok authtoken if you want to deploy a public Langflow server.

## Serve flows as MCP tools​

When you create a Langflow project, Langflow automatically adds the project to your MCP server's configuration and makes the project's flows available as MCP tools.

If your Langflow server has authentication enabled (AUTO_LOGIN=false), the project's MCP server is automatically configured with API key authentication, and a new API key is generated specifically for accessing the new project's flows.
For more information, see MCP server authentication.

### Prevent automatic MCP server configuration for Langflow projects​

To disable automatic MCP server configuration for new projects, set the LANGFLOW_ADD_PROJECTS_TO_MCP_SERVERS environment variable to false.
For more information, see MCP server environment variables.

### Selectively enable and disable MCP servers for Langflow projects​

With or without automatic MCP server configuration enabled, you can selectively enable and disable the projects that are exposed as MCP tools:

1. Click the MCP Server tab on the Projects page, or, when editing a flow, click Share, and then select MCP Server.
The Flows/Tools section lists the flows that are currently being served as tools on this MCP server.
2. To toggle exposed flows, click  Edit Tools, and then select the flows that you want exposed as tools.
To prevent a flow from being used as a tool, clear the checkbox in the first column.
3. Close the MCP Server Tools dialog to save your changes.

### Edit flow tool names and descriptions​

Tool names and descriptions help MCP clients determine which actions your flows provide and when to use those actions.
It is recommended to provide clear, descriptive names and descriptions for all tools that you serve to MCP clients.

To edit the names and descriptions of flow tools on a Langflow MCP server, do the following:

1. Click the MCP Server tab on the Projects page, or, when editing a flow, click Share, and then select MCP Server.
2. Click  Edit Tools.
3. Click the Description or Tool that you want to edit:
Tool name: Enter a name that makes it clear what the flow does when used as a tool by an agent.
Tool description: Enter a description that completely and accurately describes the specific actions the flow performs.
4. Close the MCP Server Tools dialog to save your changes.

#### Importance of tool names and descriptions​

MCP clients use tool names and descriptions to determine which actions to use when generating responses.

Because MCP clients treat your Langflow project as a single MCP server with all of your enabled flows listed as tools, unclear names and descriptions can cause the agent to select tools incorrectly or inconsistently.

For example, a flow's default tool name is the flow ID, such as adbbf8c7-0a34-493b-90ea-5e8b42f78b66.
This provides no information to an agent about the type of flow or its purpose.

To provide more context about your flows, make sure to name and describe your flows clearly when configuring your Langflow project's MCP server.

Think of these names and descriptions as function names and code comments.
Use clear statements to describe the problems your flows solve.

Example: Tool name and description usageFor example, assume you create a flow based on the Document Q&A template that uses an LLM to chat about resumes, and then you give the flow the following name and description:

- Tool name: document_qa_for_resume
- Tool description: A flow for analyzing Emily's resume.

After connecting your Langflow MCP server to Cursor, you can ask Cursor about the resume, such as What job experience does Emily have?.
Using the context provided by your tool name and description, the agent can decide to use the document_qa_for_resume MCP tool to create a response about Emily's resume.
If necessary, the agent asks permission to use the flow tool before generating the response.

If you ask about a different resume, such as What job experience does Alex have?, the agent can decide that document_qa_for_resume isn't relevant to this request, because the tool description specifies that the flow is for Emily's resume.
In this case, the agent might use another available tool, or it can inform you that it doesn't have access to information about Alex's.
For example:

`_10I notice you're asking about Alex's job experience._10Based on the available tools, I can see there is a Document QA for Resume flow that's designed for analyzing resumes._10However, the description mentions it's for "Emily's resume" not Alex's. I don't have access to Alex's resume or job experience information.`## Connect clients to your Langflow MCP server​

Langflow provides automatic installation and code snippets to help you deploy your Langflow MCP servers to your local MCP clients.

- JSON
- Auto install

The JSON option allows you to connect a Langflow MCP server to any local or remote MCP client.
You can modify this process for any MCP-compatible client.

1. Install any MCP-compatible client.
These steps use Cursor as an example, but the process is generally the same for all clients, with slight differences in client-specific details like file names.
2. In your client, add a new MCP server using the client's UI or configuration file.
For example, in Cursor, go to Cursor Settings, select MCP, and then click Add New Global MCP Server to open Cursor's global mcp.json configuration file.
3. Recommended: Configure authentication for your MCP server.
4. In Langflow, on the Projects page, click the MCP Server tab.
5. Click the JSON tab, copy the code snippet for your operating system, and then paste it into your client's MCP configuration file.
For example:
_11{_11  "mcpServers": {_11    "PROJECT_NAME": {_11      "command": "uvx",_11      "args": [_11        "mcp-proxy",_11        "http://LANGFLOW_SERVER_ADDRESS/api/v1/mcp/project/PROJECT_ID/streamable"_11      ]_11    }_11  }_11}
The MCP Server tab automatically populates the LANGFLOW_SERVER_ADDRESS and PROJECT_ID values.
The default Langflow server address is http://localhost:7860.
If you are using a public Langflow server, the server address is automatically included.
If your Langflow server requires authentication, you must include your Langflow API key or OAuth settings in the configuration.
For more information, see MCP server authentication.
6. To include other environment variables with your MCP server command, add an env object with key-value pairs of environment variables:
_14{_14  "mcpServers": {_14    "PROJECT_NAME": {_14      "command": "uvx",_14      "args": [_14        "mcp-proxy",_14        "http://LANGFLOW_SERVER_ADDRESS/api/v1/mcp/project/PROJECT_ID/streamable"_14      ],_14      "env": {_14        "KEY": "VALUE"_14      }_14    }_14  }_14}
7. Save and close your client's MCP configuration file.
8. Confirm that your Langflow MCP server is on the client's list of MCP servers.
If necessary, restart your client to apply the modified configuration file.

infoThe auto install option is available only for specific MCP clients.
Auto install requires the client to be installed locally so Langflow can write to the client's configuration file.
If your client isn't supported, is installed remotely, or you need to pass additional environment variables, use the JSON option.

1. Install Cursor, Claude, or Windsurf on the same computer where your Langflow server is running.
2. Recommended: Configure authentication for your MCP server.
3. In Langflow, on the Projects page, click the MCP Server tab.
4. On the Auto install tab, find your MCP client provider, and then click  Add.
Your Langflow project's MCP server is automatically added to the configuration file for your local Cursor, Claude, or Windsurf client.
For example, with Cursor, the server configuration is added to the mcp.json configuration file.
Langflow attempts to add this configuration even if the selected client isn't installed.
To verify the installation, check the available MCP servers in your client.

Once your MCP client is connected to your Langflow project's MCP server, your flows are registered as tools.
Cursor determines when to use tools based on your queries, and requests permissions when necessary.
For more information, see the MCP documentation for your client, such as Cursor's MCP documentation.

## MCP server authentication​

Each Langflow project has its own MCP server with its own MCP server authentication settings.

When you create a new project, Langflow automatically configures authentication for the project's MCP server based on your Langflow server's authentication settings. If authentication is enabled (AUTO_LOGIN=false), the project is automatically configured with API key authentication, and a new API key is generated for accessing the project's flows.

To configure authentication for a Langflow MCP server, go to the Projects page in Langflow, click the MCP Server tab, click  Edit Auth, and then select your preferred authentication method:

- API key
- OAuth
- None

When authenticating your MCP server with a Langflow API key, your project's MCP server JSON code snippets and Auto install configuration automatically include the --headers and x-api-key arguments.

Click  Generate API key to automatically insert a new Langflow API key into the code template.
Alternatively, you can replace YOUR_API_KEY with an existing Langflow API key.

When OAuth is enabled, Langflow automatically starts an MCP Composer instance for your project, creating a secure client-side proxy between MCP clients and the mcp-proxy on your server.

OAuth integration allows your Langflow MCP server to authenticate users and applications through any OAuth 2.0 compliant service. When users or applications connect to your MCP server, they are redirected to your chosen OAuth provider to authenticate. Upon successful authentication, they are granted access to your flows as MCP tools.

Before configuring OAuth in Langflow, you must first set up an OAuth application with an external OAuth 2.0 service provider.
You must register your Langflow server as an OAuth client, and then obtain the required values to complete the configuration in Langflow.

The following table describes the required values.
GitHub OAuth is used for example purposes.
Be sure to use the actual values from your own deployment.
For more information, see your OAuth provider's documentation.

FieldDescriptionSourceExample**Host**OAuth server hostMCP Composer default.`localhost`**Port**OAuth server portMCP Composer default.`9000`**Server URL**Full OAuth server URLCombines the MCP Composer default OAuth host and port.`http://localhost:9000`**Callback URL**OAuth callback URL on your serverYou define this full URL during OAuth app registration. This must match exactly what you register with your OAuth provider.`http://localhost:9000/auth/idaas/callback`**Client ID**Your OAuth client identifierFrom your OAuth provider.`Ov23li9vx2grVL61qjb`**Client Secret**Your OAuth client secretFrom your OAuth provider.`1234567890abcdef1234567890abcdef12345678`**Authorization URL**OAuth authorization endpointFrom your OAuth provider.`https://github.com/login/oauth/authorize`**Token URL**OAuth token endpoint for getting refresh tokensFrom your OAuth provider.`https://github.com/login/oauth/access_token`**MCP Scope**Scope for MCP operationsYou define this. As of Langflow 1.6,`user`is the only available value.`user`**Provider Scope**OAuth provider scopeYou define this. As of Langflow 1.6,`openid`is the only available value.`openid`To configure OAuth authentication:

1. Select OAuth as the authentication type.
2. Configure the OAuth settings with the values from your OAuth deployment.
All values are required.
The OAuth credentials are encrypted and stored securely in your Langflow database.
3. Click Save.
Your MCP server's JSON code snippets and Auto install configuration are automatically updated with OAuth values. These are automatically used for new installations after enabling OAuth. However, you must manually update any existing installations, as explained in the next step.
4. If you already installed your Langflow MCP server in your MCP client, you must update your MCP client configuration to use the new OAuth settings after enabling OAuth on your MCP server.
The client update method depends on how you installed the server on the client:
Auto install: Manually update your client's config file using the updated JSON snippet from the JSON tab, or repeat the steps in Auto-install to re-install the client with the updated settings.
JSON option: Copy the updated JSON snippet from the JSON tab and replace your existing configuration.
New connections: Use either the Auto install or JSON option. The OAuth settings are included automatically.

After you enable OAuth and update your client configuration, an OAuth callback window opens each time your MCP client attempts to authenticate with the server.
A successful authentication returns Authentication complete. You may close this window.
If your client doesn't open the OAuth window, try restarting the client to retrieve the updated configuration.

When no authentication is configured, your MCP server becomes a public endpoint that anyone can access without providing credentials.
Only use this option when Langflow is running in a trusted environment.

## MCP server environment variables​

The following environment variables set behaviors related to your Langflow projects' MCP servers:

VariableFormatDefaultDescription`LANGFLOW_MCP_SERVER_ENABLED`Boolean`True`Whether to initialize an MCP server for each of your Langflow projects. If`false`, Langflow doesn't initialize MCP servers.`LANGFLOW_MCP_SERVER_ENABLE_PROGRESS_NOTIFICATIONS`Boolean`False`If`true`, Langflow MCP servers send progress notifications.`LANGFLOW_MCP_SERVER_TIMEOUT`Integer`20`The number of seconds to wait before an MCP server operation expires due to poor connectivity or long-running requests.`LANGFLOW_MCP_MAX_SESSIONS_PER_SERVER`Integer`10`Maximum number of MCP sessions to keep per unique server.`LANGFLOW_ADD_PROJECTS_TO_MCP_SERVERS`Boolean`True`Whether to automatically add newly created projects to the user's MCP servers configuration. If`false`, projects must be manually added to MCP servers.### Deploy your Langflow MCP server externally​

To deploy your Langflow MCP server externally, see Deploy a public Langflow server.

## Use MCP Inspector to test and debug flows​

Node prerequisiteMCP Inspector requires any LTS version of Node.js installed on your computer.

MCP Inspector is a common tool for testing and debugging MCP servers.
You can use MCP Inspector to monitor your flows and get insights into how they are being consumed by the MCP server.

1. Install MCP Inspector:
_10npx @modelcontextprotocol/inspector
For more information about configuring MCP Inspector, including specifying a proxy port, see the MCP Inspector GitHub project.
2. Open a web browser and navigate to the MCP Inspector UI.
The default address is http://localhost:6274.
3. In the MCP Inspector UI, enter the connection details for your Langflow project's MCP server.
The field values depend on your server's method of authentication.
API keyOAuthNone
Transport Type: Select STDIO.
Command: uvx
Arguments: Enter the following list of arguments, separated by spaces. Replace the values for YOUR_API_KEY, LANGFLOW_SERVER_ADDRESS, and PROJECT_ID with the values from your Langflow MCP server. For example:
_10mcp-proxy --headers x-api-key YOUR_API_KEY http://LANGFLOW_SERVER_ADDRESS/api/v1/mcp/project/PROJECT_ID/streamable
Transport Type: Select STDIO.
Command: uvx
Arguments: Enter the following list of arguments, separated by spaces. Replace the value for OAUTH_SERVER_URL with the URL of your OAuth server. For example:
_10mcp-composer --mode stdio --sse-url http://localhost:9000/sse --disable-composer-tools --client_auth_type oauth
Transport Type: Select SSE.
URL: Enter the Langflow MCP server's endpoint. For example:
_10http://localhost:7860/api/v1/mcp/project/d359cbd4-6fa2-4002-9d53-fa05c645319c/streamable
4. Click Connect.
If the connection was successful, you should see your project's flows in the Tools tab.
From this tab, you can monitor how your flows are being registered as tools by MCP, as well as test the tools with custom input values.
5. To quit MCP Inspector, press Control+C in the same terminal window where you started it.

## Troubleshoot Langflow MCP servers​

For troubleshooting advice for MCP servers and clients, see Troubleshoot Langflow: MCP issues.

## See also​

- Use Langflow as an MCP client
- Use a DataStax Astra DB MCP server
- MCP server environment variables
