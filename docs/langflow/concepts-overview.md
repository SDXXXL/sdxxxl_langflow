# Use the visual editor | Langflow Documentation

- Flows
- Use the visual editor

On this page# Use the visual editor

You use Langflow's visual editor to create, test, and share flows, which are functional representations of application workflows.
Flows consist of components that represent individual steps in your application's workflow.

Langflow's drag-and-drop interface allows you to create complex AI workflows without writing extensive code.
You can connect different resources, including prompts, large language models (LLMs), data sources, agents, MCP servers, and other tools and integrations.

tipTo try building and running a flow in a few minutes, see the Langflow quickstart.

## Workspace​

When building a flow, you primarily interact with the workspace.
This is where you add components, configure them, and attach them together.

From the workspace, you can also access the Playground, Share menu, and Logs.

### Workspace gestures and interactions​

Use these shortcuts, gestures, and functionality to navigate the workspace:

- Pan horizontally and vertically: Click and drag an empty area of the workspace.
- Rearrange components: Click and drag the components anywhere on the workspace.
To change the programmatic relationship between components, you must manipulate the component edges or ports. For more information, see Components overview.
To enable guide lines, click  Help, and then toggle Enable smart guides.
If you can't edit any components, make sure the flow is unlocked.
- Zoom: Scroll on the mouse or trackpad, or click  Canvas controls next to the zoom percentage more zoom options: Zoom In, Zoom Out, Zoom To 100%, and Zoom To Fit.
- Add notes and comments: Click  Add Note.
- Keyboard shortcuts: To view available shortcuts, click  Help, and then select Shortcuts.

## Playground​

If your flow has a Chat Input component, you can use the Playground to run your flow, chat with your flow, view inputs and outputs, and modify the LLM's memories to tune the flow's responses in real time.

To try this for yourself, create a flow based on the Basic Prompting template, and then click  Playground when editing the flow in the workspace.

If you have an Agent component in your flow, the Playground displays its tool calls and outputs so you can monitor the agent's tool use and understand the reasoning behind its responses.
To try an agent flow in the Playground, use the Simple Agent template or the Langflow quickstart.

For more information, see Test flows in the Playground.

## Share​

The Share menu provides the following options for integrating your flow into external applications:

- API access: Integrate your flow into your applications with automatically-generated Python, JavaScript, and curl code snippets.
- Export: Export your flow to your local machine as a JSON file.
- MCP Server: Expose your flow as a tool for MCP-compatible clients.
- Embed into site: Embed your flow in HTML, React, or Angular applications.
- Shareable Playground: Share your Playground interface with another user.
This is specifically for sharing the Playground experience; it isn't for running a flow in a production application.
The Sharable Playground isn't available for Langflow Desktop.

## See also​

- Manage files in Langflow
- Global variables
- API keys and authentication
