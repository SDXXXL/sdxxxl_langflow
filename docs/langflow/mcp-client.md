# Use Langflow as an MCP client | Langflow Documentation

- Model Context Protocol (MCP)
- Use Langflow as an MCP client

On this page# Use Langflow as an MCP client

Langflow integrates with the Model Context Protocol (MCP) as both an MCP server and an MCP client.

This page describes how to use Langflow as an MCP client with the MCP Tools component and connected MCP servers.

For information about using Langflow as an MCP server, see Use Langflow as an MCP server.

## Use the MCP tools component​

The MCP Tools component connects to an MCP server so that a Langflow agent can use the server's tools when responding to user queries.

This component has two modes, depending on the type of server you want to access:

- Connect to a non-Langflow MCP server with a JSON configuration file, server start command, or HTTP/SSE URL to access tools provided by external, non-Langflow MCP servers.
- Connect to a Langflow MCP server to use flows from your Langflow projects as MCP tools.

### Connect to a non-Langflow MCP server​

1. Add an MCP Tools component to your flow.
2. In the MCP Server field, select a previously connected server or click  Add MCP Server.
There are multiple ways to add a new server:
JSON: Paste the MCP server's JSON configuration object into the field, including required and optional parameters that you want to use, and then click Add Server.
STDIO: Enter the MCP server's Name, Command, and any Arguments and Environment Variables the server uses, and then click Add Server.
For example, to start a Fetch server, the Command is uvx mcp-server-fetch.
HTTP/SSE: Enter your MCP server's Name, URL, and any Headers and Environment Variables the server uses, and then click Add Server.
The default URL for Langflow MCP servers is http://localhost:7860/api/v1/mcp/project/PROJECT_ID/streamable or http://localhost:7860/api/v1/mcp/streamable. For more information, see Connect to a Langflow MCP server.
tipuvx is included with uv in the Langflow package.To use npx server commands, you must first install an LTS release of Node.js. If you run Langflow in Docker, install Node.js inside the container image and rebuild so that npx-based MCP servers are available at runtime. For more information, see Package management.For an example of an npx MCP server in Langflow, see Connect an Astra DB MCP server to Langflow.
3. To use environment variables in your server command, enter each variable in the Env fields as key-value pairs.
tipLangflow passes environment variables from the .env file to MCP, but it doesn't pass global variables declared in your Langflow Settings.
To define an MCP server environment variable as a global variable, add it to Langflow's .env file at startup.
For more information, see global variables.
4. In the Tool field, select a tool that you want this component to use, or leave the field blank to allow access to all tools provided by the MCP server.
If you select a specific tool, you might need to configure additional tool-specific fields. For information about tool-specific fields, see your MCP server's documentation.
At this point, the MCP Tools component is serving a tool from the connected server, but nothing is using the tool. The next steps explain how to make the tool available to an Agent component so that the agent can use the tool in its responses.
5. In the component's header menu, enable Tool mode so you can use the component with an agent.
6. Connect the MCP Tools component's Toolset port to an Agent component's Tools port.
If not already present in your flow, make sure you also attach Chat Input and Chat Output components to the Agent component.
7. Test your flow to make sure the MCP server is connected and the selected tool is used by the agent. Open the Playground, and then enter a prompt that uses the tool you connected through the MCP Tools component.
For example, if you use mcp-server-fetch with the fetch tool, you could ask the agent to summarize recent tech news. The agent calls the MCP server function fetch, and then returns the response.
8. If you want the agent to be able to use more tools, repeat these steps to add more tools components with different servers or tools.

### Connect a Langflow MCP server​

Every Langflow project runs a separate MCP server that exposes the project's flows as MCP tools.
For more information about your projects' MCP servers, including exposing flows as MCP tools, see Use Langflow as an MCP server.

Langflow MCP servers support both the streamable HTTP transport and Server-Sent Events (SSE) as a fallback.

To leverage flows-as-tools, use the MCP Tools component to connect to a project's MCP endpoint:

1. Add an MCP Tools component to your flow, click  Add MCP Server, and then select HTTP/SSE mode.
2. In the MCP URL field, enter your Langflow server's MCP endpoint.
For project-specific servers: http://localhost:7860/api/v1/mcp/project/PROJECT_ID/streamable
For global MCP server: http://localhost:7860/api/v1/mcp/streamable
Default for Langflow Desktop: http://localhost:7868/
All flows available from the targeted server are treated as tools.
3. In the component's header menu, enable Tool Mode so you can use the component with an agent.
4. Connect the MCP Tools component's Toolset port to an Agent component's Tools port.
5. If not already present in your flow, make sure you also attach Chat Input and Chat Output components to the Agent component.
6. Test your flow to make sure the agent uses your flows to respond to queries. Open the Playground, and then enter a prompt that uses a flow that you connected through the MCP Tools component.
7. If you want the agent to be able to use more tools, repeat these steps to add more tools components with different servers or tools.

## MCP Tools parameters​

NameTypeDescriptionmcp_serverStringInput parameter. The MCP server to connect to. Select from previously configured servers or add a new one.toolStringInput parameter. The specific tool to execute from the connected MCP server. Leave blank to allow access to all tools.use_cacheBooleanInput parameter. Enable caching of MCP server and tools to improve performance. Default:`false`.verify_sslBooleanInput parameter. Enable SSL certificate verification for HTTPS connections. Default:`true`.responseDataFrameOutput parameter.[DataFrame](https://docs.langflow.org/data-types#dataframe)containing the response from the executed tool.## Manage connected MCP servers​

To manage all MCP server connections for your Langflow client, click  MCP servers in the visual editor, or click your profile icon, select Settings, and then click MCP Servers.

To add a new MCP server, click Add MCP Server, and then follow the steps in Use the MCP Tools component to configure the connection and use the server in a flow.

Click  More to edit or delete an MCP server connection.

## See also​

- Use Langflow as an MCP server
- Use a DataStax Astra DB MCP server with the MCP Tools component
