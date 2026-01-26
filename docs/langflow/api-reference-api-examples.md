# Get started with the Langflow API | Langflow Documentation

- API reference
- Get started with the Langflow API

On this page# Get started with the Langflow API

[data-ch-theme="github-dark"] {  --ch-t-colorScheme: dark;--ch-t-foreground: #c9d1d9;--ch-t-background: #0d1117;--ch-t-lighter-inlineBackground: #0d1117e6;--ch-t-editor-background: #0d1117;--ch-t-editor-foreground: #c9d1d9;--ch-t-editor-lineHighlightBackground: #6e76811a;--ch-t-editor-rangeHighlightBackground: #ffffff0b;--ch-t-editor-infoForeground: #3794FF;--ch-t-editor-selectionBackground: #264F78;--ch-t-focusBorder: #1f6feb;--ch-t-tab-activeBackground: #0d1117;--ch-t-tab-activeForeground: #c9d1d9;--ch-t-tab-inactiveBackground: #010409;--ch-t-tab-inactiveForeground: #8b949e;--ch-t-tab-border: #30363d;--ch-t-tab-activeBorder: #0d1117;--ch-t-editorGroup-border: #30363d;--ch-t-editorGroupHeader-tabsBackground: #010409;--ch-t-editorLineNumber-foreground: #6e7681;--ch-t-input-background: #0d1117;--ch-t-input-foreground: #c9d1d9;--ch-t-input-border: #30363d;--ch-t-icon-foreground: #8b949e;--ch-t-sideBar-background: #010409;--ch-t-sideBar-foreground: #c9d1d9;--ch-t-sideBar-border: #30363d;--ch-t-list-activeSelectionBackground: #6e768166;--ch-t-list-activeSelectionForeground: #c9d1d9;--ch-t-list-hoverBackground: #6e76811a;--ch-t-list-hoverForeground: #c9d1d9; }You can use the Langflow API for programmatic interactions with Langflow, such as the following:

- Create and edit flows, including file management for flows.
- Develop applications that use your flows.
- Develop custom components.
- Build Langflow as a dependency of a larger application, codebase, or service.
- Contribute to the overall Langflow codebase.

To view and test all available endpoints, you can access the Langflow API's OpenAPI specification at your Langflow deployment's /docs endpoint, such as http://localhost:7860/docs.

Try itFor an example of the Langflow API in a script, see the Langflow quickstart.

The quickstart demonstrates how to get automatically generated code snippets for your flows, use a script to run a flow, and extract data from the Langfow API response.

## Form Langflow API requests​

While individual options vary by endpoint, all Langflow API requests share some commonalities, like a URL, method, parameters, and authentication.

As an example of a Langflow API request, the following curl command calls the /v1/run endpoint, and it passes a runtime override (tweaks) to the flow's Chat Output component:

`_14curl --request POST \_14  --url "$LANGFLOW_SERVER_URL/api/v1/run/$FLOW_ID?stream=false" \_14  --header "Content-Type: application/json" \_14  --header "x-api-key: $LANGFLOW_API_KEY" \_14  --data '{_14  "input_value": "hello world!",_14  "output_type": "chat",_14  "input_type": "chat",_14  "tweaks": {_14    "ChatOutput-6zcZt": {_14      "should_store_message": true_14    }_14  }_14}'`### Base URL​

By default, local deployments serve the Langflow API at http://localhost:7860/api.

Remotely hosted Langflow deployments are available at the domain set by the hosting service, such as http://IP_OR_DNS/api or http://IP_OR_DNS:LANGFLOW_PORT/api.

You can configure the Langflow port number in the LANGFLOW_PORT environment variable.

- https://UUID.ngrok.app/api
- http://IP_OR_DNS/api
- http://IP_OR_DNS:LANGFLOW_PORT/api

### Authentication​

In Langflow versions 1.5 and later, most API endpoints require authentication with a Langflow API key in either an x-api-key header or query parameter.
For more information, see API keys and authentication.

As with any API, follow industry best practices for storing and referencing sensitive credentials.
For example, you can set environment variables for your API keys, and then reference those environment variables in your API requests.

### Methods, paths, and parameters​

Langflow API requests use various methods, paths, path parameters, query parameters, and body parameters.
The specific requirements and options depend on the endpoint that you want to call.

For example, to create a flow, you pass a JSON-formatted flow definition to POST /v1/flows.
Then, to run your flow, you call POST /v1/run/$FLOW_ID with optional run parameters in the request body.

### API versions​

The Langflow API serves /v1 and /v2 endpoints.

Some endpoints only exist under a single version and some exist under both the /v1 and /v2 versions.

If a request fails or has an unexpected result, make sure your endpoint path has the correct version.

## Set environment variables​

You can store commonly used values in environment variables to facilitate reuse, simplify token rotation, and securely reference sensitive values.

You can use any method you prefer to set environment variables, such as export, .env, zshrc, or .curlrc.
Then, reference those environment variables in your API requests.
For example:

`_22# Set environment variables_22export LANGFLOW_API_KEY="sk..."_22export LANGFLOW_SERVER_URL="https://localhost:7860"_22export FLOW_ID="359cd752-07ea-46f2-9d3b-a4407ef618da"_22export PROJECT_ID="1415de42-8f01-4f36-bf34-539f23e47466"_22export LANGFLOW_API_KEY="sk-..."_22_22# Use environment variables in API requests_22curl --request POST \_22  --url "$LANGFLOW_SERVER_URL/api/v1/run/$FLOW_ID$?stream=false" \_22  --header "Content-Type: application/json" \_22  --header "x-api-key: $LANGFLOW_API_KEY" \_22  --data '{_22  "input_value": "hello world!",_22  "output_type": "chat",_22  "input_type": "chat",_22  "tweaks": {_22    "ChatOutput-6zcZt": {_22      "should_store_message": true_22    }_22  }_22}'`Commonly used values in Langflow API requests include your Langflow server URL, Langflow API keys, flow IDs, and project IDs.

You can retrieve flow IDs from the API access pane, in a flow's URL, and with GET /flows.

## Try some Langflow API requests​

Once you have your Langflow server URL, try calling these endpoints that return Langflow metadata.

### Health check​

Returns the health status of the Langflow database and chat services:

`_10curl -X GET \_10  "$LANGFLOW_SERVER_URL/health_check" \_10  -H "accept: application/json"`Result`_10{_10  "status": "ok",_10  "chat": "ok",_10  "db": "ok"_10}`Langflow provides an additional GET /health endpoint.
This endpoint is served by uvicorn before Langflow is fully initialized, so it's not reliable for checking Langflow service health.

### Get version​

Returns the current Langflow API version:

`_10curl -X GET \_10  "$LANGFLOW_SERVER_URL/api/v1/version" \_10  -H "accept: application/json"`Result`_10{_10    "version": "1.6.0",_10    "main_version": "1.6.0",_10    "package": "Langflow"_10}`### Get configuration​

Returns configuration details for your Langflow deployment.
Requires a Langflow API key.

`_10curl -X GET \_10  "$LANGFLOW_SERVER_URL/api/v1/config" \_10  -H "accept: application/json" \_10  -H "x-api-key: $LANGFLOW_API_KEY"`Result`_20{_20  "feature_flags": {_20    "mvp_components": false_20  },_20  "serialization_max_items_length": 1000,_20  "serialization_max_text_length": 6000,_20  "frontend_timeout": 0,_20  "auto_saving": true,_20  "auto_saving_interval": 1000,_20  "health_check_max_retries": 5,_20  "max_file_size_upload": 1024,_20  "webhook_polling_interval": 5000,_20  "public_flow_cleanup_interval": 3600,_20  "public_flow_expiration": 86400,_20  "event_delivery": "streaming",_20  "webhook_auth_enable": false,_20  "voice_mode_available": false,_20  "default_folder_name": "Starter Project",_20  "hide_getting_started_progress": false_20}`### Get all components​

Returns a dictionary of all Langflow components.
Requires a Langflow API key.

`_10curl -X GET \_10  "$LANGFLOW_SERVER_URL/api/v1/all" \_10  -H "accept: application/json" \_10  -H "x-api-key: $LANGFLOW_API_KEY"`## Available endpoints​

Because you can run Langflow as either an IDE (frontend and backend) or a runtime (headless, backend-only), it serves endpoints that support frontend and backend operations.
Many endpoints are for orchestration between the frontend and backend, reading and writing to the Langflow database, or enabling frontend functionality, like the Playground.
Unless you are contributing to the Langflow codebase, you won't directly call most of the Langflow endpoints.

For application development, the most commonly used endpoints are the /run and /webhook flow trigger endpoints.
For some use cases, you might use some other endpoints, such as the /files endpoints to use files in flows.

To help you explore the available endpoints, the following lists are sorted by primary use case, although some endpoints might support multiple use cases.

- Application development
- Codebase development
- Deprecated

The following endpoints are useful for developing applications with Langflow and administering Langflow deployments with one or more users.
You will most often use the flow trigger endpoints.
Other endpoints are helpful for specific use cases, such as administration and flow management in runtime deployments that don't have a visual editor.

- Flow trigger endpoints:
POST /v1/run/{flow_id_or_name}: Run a flow.
POST /v1/run/advanced/{flow_id}: Advanced run with explicit inputs, outputs, tweaks, and optional session_id.
POST /v1/webhook/{flow_id_or_name}: Trigger a flow via webhook payload.
- OpenAI Responses API:
POST /v1/responses: Execute flows using an OpenAI-compatible request format.
- Deployment details:
GET /v1/version: Return Langflow version. See Get version.
GET /v1/config: Return deployment configuration. See Get configuration.
GET /health_check: Health check endpoint that validates database and chat service connectivity. Returns 500 status if any service is unavailable.
- Projects endpoints:
POST /v1/projects/: Create a project.
GET /v1/projects/: List projects.
GET /v1/projects/{project_id}: Read a project (with paginated flows support).
PATCH /v1/projects/{project_id}: Update project info and membership.
DELETE /v1/projects/{project_id}: Delete a project.
GET /v1/projects/download/{project_id}: Export all flows in a project as ZIP.
POST /v1/projects/upload/: Import a project ZIP (creates project and flows).
GET /v1/starter-projects/: Return a list of templates.
- Files endpoints:
Files (v1)
POST /v1/files/upload/{flow_id}: Upload a file to a specific flow.
GET /v1/files/download/{flow_id}/{file_name}: Download a file from a flow.
GET /v1/files/images/{flow_id}/{file_name}: Stream an image from a flow.
GET /v1/files/profile_pictures/{folder_name}/{file_name}: Get a profile picture asset.
GET /v1/files/profile_pictures/list: List available profile picture assets.
GET /v1/files/list/{flow_id}: List files for a flow.
DELETE /v1/files/delete/{flow_id}/{file_name}: Delete a file from a flow.
Files (v2)
POST /v2/files (alias /v2/files/): Upload a file owned by the current user.
GET /v2/files (alias /v2/files/): List files owned by the current user.
DELETE /v2/files/batch/: Delete multiple files by IDs.
POST /v2/files/batch/: Download multiple files as a ZIP by IDs.
GET /v2/files/{file_id}: Download a file by ID (or return raw content internally).
PUT /v2/files/{file_id}: Edit a file name by ID.
DELETE /v2/files/{file_id}: Delete a file by ID.
DELETE /v2/files (alias /v2/files/): Delete all files for the current user.
- API keys and authentication:
GET /v1/api_key/: List API keys for the current user.
POST /v1/api_key/: Create a new API key.
DELETE /v1/api_key/{api_key_id}: Delete an API key.
POST /v1/api_key/store: Save an encrypted Store API key (cookie set).
- Flow management endpoints:
POST /v1/flows/: Create a flow.
GET /v1/flows/: List flows (supports pagination and filters).
GET /v1/flows/{flow_id}: Read a flow by ID.
GET /v1/flows/public_flow/{flow_id}: Read a public flow by ID.
PATCH /v1/flows/{flow_id}: Update a flow.
DELETE /v1/flows/{flow_id}: Delete a flow.
POST /v1/flows/batch/: Create multiple flows.
POST /v1/flows/upload/: Import flows from a JSON file.
DELETE /v1/flows/: Delete multiple flows by IDs.
POST /v1/flows/download/: Export flows to a ZIP file.
GET /v1/flows/basic_examples/: List basic example flows.
- Users endpoints:
POST /v1/users/: Add a user (superuser required when auth enabled).
GET /v1/users/whoami: Return the current authenticated user.
GET /v1/users/: List all users (superuser required).
PATCH /v1/users/{user_id}: Update a user (with role checks).
PATCH /v1/users/{user_id}/reset-password: Reset own password.
DELETE /v1/users/{user_id}: Delete a user (cannot delete yourself).
- Custom components: You might use these endpoints when developing custom Langflow components for your own use or to share with the Langflow community:
GET /v1/all: Return all available Langflow component types. See Get all components.
POST /v1/custom_component: Build a custom component from code and return its node.
POST /v1/custom_component/update: Update an existing custom component's build config and outputs.
POST /v1/validate/code: Validate a Python code snippet for a custom component.
POST /v1/validate/prompt: Validate a prompt payload.

The following endpoints are most often used when contributing to the Langflow codebase, and you need to understand or call endpoints that support frontend-to-backend orchestration or other internal functionality.

- Base (metadata):
GET /v1/all: Return all available Langflow component types. See Get all components.
GET /v1/version: Return Langflow version. See Get version.
GET /v1/config: Return deployment configuration. See Get configuration.
GET /v1/starter-projects/: Return a list of templates.
- Build endpoints (internal editor support):
POST /v1/build/{flow_id}/flow: Start a flow build and return a job ID.
GET /v1/build/{job_id}/events: Stream or fetch build events.
POST /v1/build/{job_id}/cancel: Cancel a build job.
POST /v1/build_public_tmp/{flow_id}/flow: Build a public flow without auth.
POST /v1/validate/prompt: Validate a prompt payload.
- API keys and authentication:
POST /v1/login: Login and set tokens as cookies.
GET /v1/auto_login: Auto-login (if enabled) and set tokens.
POST /v1/refresh: Refresh tokens using refresh cookie.
POST /v1/logout: Logout and clear cookies.
- Monitor endpoints:
GET /v1/monitor/builds: Get vertex builds for a flow.
DELETE /v1/monitor/builds: Delete vertex builds for a flow.
GET /v1/monitor/messages/sessions: List message session IDs (auth required).
GET /v1/monitor/messages: List messages with optional filters.
DELETE /v1/monitor/messages: Delete messages by IDs (auth required).
PUT /v1/monitor/messages/{message_id}: Update a message.
PATCH /v1/monitor/messages/session/{old_session_id}: Change a session ID for all messages in that session.
DELETE /v1/monitor/messages/session/{session_id}: Delete messages by session.
GET /v1/monitor/transactions: List transactions for a flow (paginated).
- Variables:
POST /v1/variables/: Create a variable, such as an API key, for the user.
GET /v1/variables/: List variables for the user.
PATCH /v1/variables/{variable_id}: Update a variable.
DELETE /v1/variables/{variable_id}: Delete a variable.
- Use voice mode:
WS /v1/voice/ws/flow_as_tool/{flow_id}: Bi-directional voice session exposing the flow as a tool.
WS /v1/voice/ws/flow_as_tool/{flow_id}/{session_id}: Same as above with explicit session ID.
WS /v1/voice/ws/flow_tts/{flow_id}: Voice-to-text session that runs a flow and returns TTS.
WS /v1/voice/ws/flow_tts/{flow_id}/{session_id}: Same as above with explicit session ID.
GET /v1/voice/elevenlabs/voice_ids: List available ElevenLabs voice IDs for the user.
- MCP servers: The following endpoints are for managing Langflow MCP servers and MCP server connections.
They aren't typically called directly; instead, they are used to drive internal functionality in the Langflow frontend and when running flows that call MCP servers.
Langflow MCP servers support both streamable HTTP and SSE transport.
HEAD /v1/mcp/streamable: Health check for streamable HTTP MCP.
GET /v1/mcp/streamable: Open streamable HTTP connection for MCP server.
POST /v1/mcp/streamable: Post messages to the MCP server via streamable HTTP.
DELETE /v1/mcp/streamable: Close streamable HTTP connection.
HEAD /v1/mcp/sse (LEGACY): Health check for MCP SSE.
GET /v1/mcp/sse (LEGACY): Open SSE stream for MCP server events.
POST /v1/mcp/ (LEGACY): Post messages to the MCP server.
GET /v1/mcp/project/{project_id}: List MCP-enabled tools and project auth settings.
HEAD /v1/mcp/project/{project_id}/streamable: Health check for project streamable HTTP MCP.
GET /v1/mcp/project/{project_id}/streamable: Open project-scoped streamable HTTP connection.
POST /v1/mcp/project/{project_id}/streamable: Post messages to project MCP server via streamable HTTP.
DELETE /v1/mcp/project/{project_id}/streamable: Close project streamable HTTP connection.
HEAD /v1/mcp/project/{project_id}/sse (LEGACY): Health check for project SSE.
GET /v1/mcp/project/{project_id}/sse (LEGACY): Open project-scoped MCP SSE.
POST /v1/mcp/project/{project_id} (LEGACY): Post messages to project MCP server.
PATCH /v1/mcp/project/{project_id}: Update MCP settings for flows and project auth settings.
POST /v1/mcp/project/{project_id}/install: Install MCP client config for Cursor/Windsurf/Claude (local only).
GET /v1/mcp/project/{project_id}/installed: Check which clients have MCP config installed.
- Custom components: You might use these endpoints when developing custom Langflow components for your own use or to share with the Langflow community:
GET /v1/all: Return all available Langflow component types. See Get all components.
POST /v1/custom_component: Build a custom component from code and return its node.
POST /v1/custom_component/update: Update an existing custom component's build config and outputs.
POST /v1/validate/code: Validate a Python code snippet for a custom component.
POST /v1/validate/prompt: Validate a prompt payload.

The following endpoints are deprecated:

- POST /v1/predict/{flow_id}: Use /v1/run/{flow_id} instead.
- POST /v1/process/{flow_id}: Use /v1/run/{flow_id} instead.
- GET /v1/task/{task_id}: Deprecated functionality.
- POST /v1/upload/{flow_id}: Use /files instead.
- POST /v1/build/{flow_id}/vertices: Replaced by /monitor/builds.
- POST /v1/build/{flow_id}/vertices/{vertex_id}: Replaced by /monitor/builds.
- GET /v1/build/{flow_id}/{vertex_id}/stream: Replaced by /monitor/builds.
- GET /v1/store/check/: Return whether the Store feature is enabled.
- GET /v1/store/check/api_key: Check if a Store API key exists and is valid.
- POST /v1/store/components/: Share a component to the Store.
- PATCH /v1/store/components/{component_id}: Update a shared component.
- GET /v1/store/components/: List available Store components (filters supported).
- GET /v1/store/components/{component_id}: Download a component from the Store.
- GET /v1/store/tags: List Store tags.
- GET /v1/store/users/likes: List components liked by the current user.
- POST /v1/store/users/likes/{component_id}: Like a component.

## Next steps​

- Use the Langflow API to run a flow.
- Use the Langflow API to upload files.
- Use the Langflow API to get flow logs.
- Explore all endpoints in the Langflow API specification.
