# Test flows in the Playground | Langflow Documentation

- Flows
- Test flows

On this page# Test flows in the Playground

[data-ch-theme="github-dark"] {  --ch-t-colorScheme: dark;--ch-t-foreground: #c9d1d9;--ch-t-background: #0d1117;--ch-t-lighter-inlineBackground: #0d1117e6;--ch-t-editor-background: #0d1117;--ch-t-editor-foreground: #c9d1d9;--ch-t-editor-lineHighlightBackground: #6e76811a;--ch-t-editor-rangeHighlightBackground: #ffffff0b;--ch-t-editor-infoForeground: #3794FF;--ch-t-editor-selectionBackground: #264F78;--ch-t-focusBorder: #1f6feb;--ch-t-tab-activeBackground: #0d1117;--ch-t-tab-activeForeground: #c9d1d9;--ch-t-tab-inactiveBackground: #010409;--ch-t-tab-inactiveForeground: #8b949e;--ch-t-tab-border: #30363d;--ch-t-tab-activeBorder: #0d1117;--ch-t-editorGroup-border: #30363d;--ch-t-editorGroupHeader-tabsBackground: #010409;--ch-t-editorLineNumber-foreground: #6e7681;--ch-t-input-background: #0d1117;--ch-t-input-foreground: #c9d1d9;--ch-t-input-border: #30363d;--ch-t-icon-foreground: #8b949e;--ch-t-sideBar-background: #010409;--ch-t-sideBar-foreground: #c9d1d9;--ch-t-sideBar-border: #30363d;--ch-t-list-activeSelectionBackground: #6e768166;--ch-t-list-activeSelectionForeground: #c9d1d9;--ch-t-list-hoverBackground: #6e76811a;--ch-t-list-hoverForeground: #c9d1d9; }Langflow's Playground is a dynamic interface you can use to test your LLM-based flows in real-time.

You can test how a flow responds to different inputs, review and modify memories, and monitor flow output and logic.
For example, you can make sure agent flows use the appropriate tools to respond to different inputs.

The Playground allows you to quickly iterate over your flow's logic and behavior, making it easier to prototype and refine your applications.

## Run a flow in the Playground​

To run a flow in the Playground, open the flow, and then click  Playground.
Then, if your flow has a Chat Input component, enter a prompt or use voice mode to trigger the flow and start a chat session.

tipIf there is no message input field in the Playground, make sure your flow has a Chat Input component that is connected, directly or indirectly, to the Input port of a Language Model or Agent component.

Because the Playground is designed for flows that use an LLM in a query-and-response format, such as chatbots and agents, a flow must have Chat Input, Language Model/Agent, and Chat Output components to be fully supported by the Playground chat interface

For flows that require another type of input, such as a webhook event, file upload, or text input, you can use the Langflow API to trigger the flow, and then open the Playground to review the LLM activity for the flow run, if applicable.

For technical details about how the Playground works, see Monitor endpoints.

### Review agent logic​

If your flow has an Agent component, the Playground prints the tools used by the agent and the output from each tool.
This helps you monitor the agent's tool use and understand the logic behind the agent's responses.
For example, the following agent used a connected fetch_content tool to perform a web search:

### View chat history​

In the Playground, you can view message logs for each of your flow's chat sessions, including timestamps, content, and senders.

In the Playground sidebar, find the chat session you want to review, click  Options, and then select Message Logs.

Message logs break apart the Message data for each chat message.
Click any cell in the message logs to view the full contents of that cell.

### Modify memories in the Playground​

To help debug and test your flows, you can edit or delete individual messages in message logs.
For example, you might want to delete messages that you sent while testing a component that is no longer part of your flow.

You can also delete entire chat sessions from the sidebar: click  Options, and then select Delete.

Modifying memories influences the behavior of the chatbot responses if you continue the chat session or if you preserve memories over multiple chat sessions.

Editing message logs edits Langflow's internal messages table, which is the default chat memory storage.
For more information about managing sessions and chat memory in Langflow, see Use custom session IDs and Memory management options.

## Set custom session IDs​

Chat sessions are identified by session ID (session_id), which is a unique identifier for a flow run.

The default session ID is the flow ID, which means that all chat messages for a flow are stored under the same session ID as one enormous chat session.

If you need to preserve chat context over multiple flow runs or differentiate chat sessions when debugging flows, you can set a custom session_id.

Custom session IDs are helpful for multiple reasons:

- Separate chat sessions in situations where one flow has multiple chat sessions, such as a chatbot that can have multiple simultaneous user interactions.
- Preserve memory when continuing a chat session across multiple flow runs or when passing context from one flow to another.
- Differentiate activity from multiple users within the same flow.
- Identify your own chat sessions when debugging and testing flows.

You can set custom session IDs in the visual editor and programmatically.

- Visual editor
- Langflow API

In your input and output components, use the Session ID field:

1. Click the component where you want to set a custom session ID.
2. In the component's header menu, click  Controls.
3. Enable Session ID.
4. Click Close.
5. Enter a custom session ID.
If the field is empty, the flow uses the default session ID.
6. Open the Playground to start a chat under your custom session ID.

Make sure to change the Session ID when you want to start a new chat session or continue an earlier chat session with a different session ID.

When you trigger a flow with the Langflow API, include the session_id parameter in the request payload.
For example:

`_10curl -X POST "http://$LANGFLOW_SERVER_ADDRESS/api/v1/run/$FLOW_ID" \_10-H "Content-Type: application/json" \_10-H "x-api-key: $LANGFLOW_API_KEY" \_10-d '{_10    "session_id": "CUSTOM_SESSION_ID",_10    "input_value": "message",_10    "input_type": "chat",_10    "output_type": "chat"_10}'`This command starts a new chat sessions with the specified session_id or it retrieves an existing session with that ID, if one exists.

tipIn a production environment, consider using a variable for the session ID rather than a hardcoded value.

For example, if you want to preserve context for authenticated users, user ID could be a useful variable for the session ID.
Alternatively, if you want every chat to be unique, you might want to automatically generate a UUID for each session ID.

For more information, see Use session ID to manage communication between components.

## Share a flow's Playground​

warningThe Shareable Playground is for testing purposes only.
The Playground isn't meant for embedding flows in applications. For information about running flows in applications or websites, see Trigger flows with the Langflow API.

The Shareable Playground isn't available in Langflow Desktop.

The Shareable Playground option exposes the Playground for a single flow at the /public_flow/$FLOW_ID endpoint.

After you deploy a public Langflow server, you can share this public URL with another user to allow them to access the specified flow's Playground only.
The user can interact with the flow's chat input and output and view the results without installing Langflow or generating a Langflow API key.

To share a flow's Playground with another user, do the following:

1. In Langflow, open the flow you want share.
2. In the workspace, click Share, and then enable Shareable Playground.
3. Click Shareable Playground again to open the Playground window.
This window's URL is the flow's Shareable Playground address, such as https://3f7c-73-64-93-151.ngrok-free.app/playground/d764c4b8-5cec-4c0f-9de0-4b419b11901a.
4. Send the URL to another user to give them access to the flow's Playground.

## See also​

- Upload images
- Use voice mode
- Trigger flows with the Langflow API
- Session ID
