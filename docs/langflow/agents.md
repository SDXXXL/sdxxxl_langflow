# Use Langflow agents | Langflow Documentation

- Agents
- Use Langflow agents

On this page# Use Langflow agents

[data-ch-theme="github-dark"] {  --ch-t-colorScheme: dark;--ch-t-foreground: #c9d1d9;--ch-t-background: #0d1117;--ch-t-lighter-inlineBackground: #0d1117e6;--ch-t-editor-background: #0d1117;--ch-t-editor-foreground: #c9d1d9;--ch-t-editor-lineHighlightBackground: #6e76811a;--ch-t-editor-rangeHighlightBackground: #ffffff0b;--ch-t-editor-infoForeground: #3794FF;--ch-t-editor-selectionBackground: #264F78;--ch-t-focusBorder: #1f6feb;--ch-t-tab-activeBackground: #0d1117;--ch-t-tab-activeForeground: #c9d1d9;--ch-t-tab-inactiveBackground: #010409;--ch-t-tab-inactiveForeground: #8b949e;--ch-t-tab-border: #30363d;--ch-t-tab-activeBorder: #0d1117;--ch-t-editorGroup-border: #30363d;--ch-t-editorGroupHeader-tabsBackground: #010409;--ch-t-editorLineNumber-foreground: #6e7681;--ch-t-input-background: #0d1117;--ch-t-input-foreground: #c9d1d9;--ch-t-input-border: #30363d;--ch-t-icon-foreground: #8b949e;--ch-t-sideBar-background: #010409;--ch-t-sideBar-foreground: #c9d1d9;--ch-t-sideBar-border: #30363d;--ch-t-list-activeSelectionBackground: #6e768166;--ch-t-list-activeSelectionForeground: #c9d1d9;--ch-t-list-hoverBackground: #6e76811a;--ch-t-list-hoverForeground: #c9d1d9; }Langflow's Agent component is critical for building agent flows.
This component provides everything you need to create an agent, including multiple Large Language Model (LLM) providers, tool calling, and custom instructions.
It simplifies agent configuration so you can focus on application development.

How do agents work?Agents extend Large Language Models (LLMs) by integrating tools, which are functions that provide additional context and enable autonomous task execution.
These integrations make agents more specialized and powerful than standalone LLMs.

Whereas an LLM might generate acceptable, inert responses to general queries and tasks, an agent can leverage the integrated context and tools to provide more relevant responses and even take action.
For example, you might create an agent that can access your company's documentation, repositories, and other resources to help your team with tasks that require knowledge of your specific products, customers, and code.

Agents use LLMs as a reasoning engine to process input, determine which actions to take to address the query, and then generate a response.
The response could be a typical text-based LLM response, or it could involve an action, like editing a file, running a script, or calling an external API.

In an agentic context, tools are functions that the agent can run to perform tasks or access external resources.
A function is wrapped as a Tool object with a common interface that the agent understands.
Agents become aware of tools through tool registration, which is when the agent is provided a list of available tools typically at agent initialization.
The Tool object's description tells the agent what the tool can do so that it can decide whether the tool is appropriate for a given request.

## Use the Agent component in a flow​

The following steps explain how to create an agent flow in Langflow from a blank flow.
For a prebuilt example, use the Simple Agent template or the Langflow quickstart.

1. Click New Flow, and then click Blank Flow.
2. Add an Agent component to your flow.
3. Select the provider and model that you want to use.
The default model for the Agent component is an OpenAI model.
If you want to use a different provider, edit the Model Provider and Model Name fields accordingly.
If your preferred model isn't listed, type the complete model name into the Model Name field, and then select it from the Model Name menu.
Make sure that the model is enabled/verified in your model provider account.
For more information, see Agent component parameters.
4. Enter a valid credential for your selected model provider.
Make sure that the credential has permission to call the selected model.
5. Add Chat Input and Chat Output components to your flow, and then connect them to the Agent component.
At this point, you have created a basic LLM-based chat flow that you can test in the  Playground.
However, this flow only chats with the LLM.
To enhance this flow and make it truly agentic, add some tools, as explained in the next steps.
6. Add Web Search, URL, and Calculator components to your flow.
7. Enable Tool Mode in the Web Search, URL, and Calculator components:
Click the Web Search component to expose the component's header menu, and then enable Tool Mode.
Repeat for the URL and Calculator components.
Connect the Toolset port for each tool component to the Tools port on the Agent component.
Tool Mode makes a component into a tool by modifying the component's inputs.
With Tool Mode enabled, a component can accept requests from an Agent component to use the component's available actions as tools.
When in Tool Mode, a component has a Toolset port that you must connect to an Agent component's Tools port if you want to allow the agent to use that component's actions as tools.
For more information, see Configure tools for agents.
8. Open the  Playground, and then ask the agent, What tools are you using to answer my questions?
The agent should respond with a list of the connected tools.
It may also include built-in tools.
_10I use a combination of my built-in knowledge (up to June 2024) and a set of external tools to answer your questions. Here are the main types of tools I can use:_10Web Search & Content Fetching: I can fetch and summarize content from web pages, including crawling links recursively._10News Search: I can search for recent news articles using Google News via RSS feeds._10Calculator: I can perform arithmetic calculations and evaluate mathematical expressions._10Date & Time: I can provide the current date and time in various time zones._10These tools help me provide up-to-date information, perform calculations, and retrieve specific data from the internet when needed. If you have a specific question, let me know, and I'll use the most appropriate tool(s) to help!
9. To test a specific tool, ask the agent a question that uses one of the tools, such as Summarize today's tech news.
To help you debug and test your flows, the Playground displays the agent's tool calls, the provided input, and the raw output the agent received before generating the summary.
With the given example, the agent should call the Web Search component with Search Mode set to News.

You've successfully created a basic agent flow that uses some generic tools.

To continue building on this tutorial, try connecting other tool components or use Langflow as an MCP client to support more complex and specialized tasks.

For a multi-agent example, see Use an agent as a tool.

## Agent component parameters​

You can configure the Agent component to use your preferred provider and model, custom instructions, and tools.

Some parameters are hidden by default in the visual editor.
You can modify all parameters through the  Controls in the component's header menu.

### Provider and model​

Use the Model Provider (agent_llm) and Model Name (llm_model) settings to select the model provider and LLM that you want the agent to use.

The Agent component includes many models from several popular model providers.
To access other providers or models, you can do either of the following:

- Set Model Provider to Connect other models, and then connect any language model component.
- Select your preferred provider, type the complete model name into the Model Name field, and then select your custom option from the Model Name menu.
Make sure that the model is enabled/verified in your model provider account.

If you need to generate embeddings in your flow, use an embedding model component.

### Model provider API key​

In the API Key field, enter a valid authentication key for your selected model provider, if you are using a built-in provider.
For example, to use the default OpenAI model, you must provide a valid OpenAI API key for an OpenAI account that has credits and permission to call OpenAI LLMs.

You can enter the key directly, but it is recommended that you follow industry best practices for storing and referencing API keys.
For example, you can use a  global variable or environment variables.
For more information, see Add component API keys to Langflow.

If you select Connect other models as the model provider, authentication is handled in the incoming language model component.

### Agent instructions and input​

In the Agent Instructions (system_prompt) field, you can provide custom instructions that you want the Agent component to use for every conversation.

These instructions are applied in addition to the Input (input_value), which can be entered directly or provided through another component, such as a Chat Input component.

### Tools​

Agents are most useful when they have the appropriate tools available to complete requests.

An Agent component can use any Langflow component as a tool, including other agents and MCP servers.

To attach a component as a tool, you must enable Tool Mode on the component that you want to attach, and then attach it to the Agent component's Tools port.
For more information, see Configure tools for agents.

tipTo allow agents to use tools from MCP servers, use the MCP Tools component.

### Agent memory​

Langflow agents have built-in chat memory that is enabled by default.
This memory allows them to retrieve and reference messages from previous conversations, maintaining a rolling context window for each chat session ID.

Chat memories are grouped by session ID (session_id).
It is recommended to use custom session IDs if you need to segregate chat memory for different users or applications that run the same flow.

By default, the Agent component uses your Langflow installation's storage, and it retrieves a limited number of chat messages, which you can configure with the Number of Chat History Messages parameter.

The Message History component isn't required for default chat memory, but it is required if you want to use external chat memory like Mem0.
Additionally, the Message History component provides more options for sorting, filtering, and limiting memories. Although, most of these options are built-in to the Agent component with default values.

For more information, see Store chat memory and Message History component.

### Additional parameters​

With the Agent component, the available parameters can change depending on the selected provider and model, including support for additional modes, arguments, or features like chat memory and temperature.
For example:

- Current Date (add_current_date_tool): When enabled (true), this setting adds a tool to the agent that can retrieve the current date.
- Handle Parse Errors (handle_parsing_errors): When enabled (true), this setting allows the agent to fix errors, like typos, when analyzing user input.
- Verbose (verbose): When enabled (true), this setting records detailed logging output for debugging and analysis.

Some parameters are hidden by default in the visual editor.
You can modify all parameters through the  Controls in the component's header menu.

## Agent component output​

The Agent component outputs a Response (response) that is Message data containing the agent's raw response to the query.

Typically, this is passed to a Chat Output component to return the response in a human-readable format.
It can also be passed to other components if you need to process the response further before, or in addition to, returning it to the user.

## See also​

- Agent and MCP Tools components
- Configure tools for agents
