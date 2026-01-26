# Quickstart | Langflow Documentation

- Get started
- Quickstart

On this page# Quickstart

[data-ch-theme="github-dark"] {  --ch-t-colorScheme: dark;--ch-t-foreground: #c9d1d9;--ch-t-background: #0d1117;--ch-t-lighter-inlineBackground: #0d1117e6;--ch-t-editor-background: #0d1117;--ch-t-editor-foreground: #c9d1d9;--ch-t-editor-lineHighlightBackground: #6e76811a;--ch-t-editor-rangeHighlightBackground: #ffffff0b;--ch-t-editor-infoForeground: #3794FF;--ch-t-editor-selectionBackground: #264F78;--ch-t-focusBorder: #1f6feb;--ch-t-tab-activeBackground: #0d1117;--ch-t-tab-activeForeground: #c9d1d9;--ch-t-tab-inactiveBackground: #010409;--ch-t-tab-inactiveForeground: #8b949e;--ch-t-tab-border: #30363d;--ch-t-tab-activeBorder: #0d1117;--ch-t-editorGroup-border: #30363d;--ch-t-editorGroupHeader-tabsBackground: #010409;--ch-t-editorLineNumber-foreground: #6e7681;--ch-t-input-background: #0d1117;--ch-t-input-foreground: #c9d1d9;--ch-t-input-border: #30363d;--ch-t-icon-foreground: #8b949e;--ch-t-sideBar-background: #010409;--ch-t-sideBar-foreground: #c9d1d9;--ch-t-sideBar-border: #30363d;--ch-t-list-activeSelectionBackground: #6e768166;--ch-t-list-activeSelectionForeground: #c9d1d9;--ch-t-list-hoverBackground: #6e76811a;--ch-t-list-hoverForeground: #c9d1d9; }Get started with Langflow by loading a template flow, running it, and then serving it at the /run API endpoint.

## Prerequisites​

- Install and start Langflow
- Create an OpenAI API key
- Create a Langflow API key
Create a Langflow API keyA Langflow API key is a user-specific token you can use with Langflow.To create a Langflow API key, do the following:
In Langflow, click your user icon, and then select Settings.
Click Langflow API Keys, and then click  Add New.
Name your key, and then click Create API Key.
Copy the API key and store it securely.
To use your Langflow API key in a request, set a LANGFLOW_API_KEY environment variable in your terminal, and then include an x-api-key header or query parameter with your request.
For example:
_13# Set variable_13export LANGFLOW_API_KEY="sk..."_13_13# Send request_13curl --request POST \_13--url "http://LANGFLOW_SERVER_ADDRESS/api/v1/run/FLOW_ID" \_13--header "Content-Type: application/json" \_13--header "x-api-key: $LANGFLOW_API_KEY" \_13--data '{_13  "output_type": "chat",_13  "input_type": "chat",_13  "input_value": "Hello"_13}'

tipIf you encounter the error "An API key must be passed as query or header" when attempting to sign up, see Troubleshooting.

## Run the Simple Agent template flow​

1. In Langflow, click New Flow, and then select the Simple Agent template.

The Simple Agent template consists of an Agent component connected to Chat Input and Chat Output components, a Calculator component, and a URL component. When you run this flow, you submit a query to the agent through the Chat Input component, the agent uses the Calculator and URL tools to generate a response, and then returns the response through the Chat Output component.

Many components can be tools for agents, including Model Context Protocol (MCP) servers. The agent decides which tools to call based on the context of a given query.

1. In the Agent component, enter your OpenAI API key directly or use a  global variable.
This example uses the Agent component's built-in OpenAI model.
If you want to use a different provider, edit the model provider, model name, and credentials accordingly.
If your preferred provider or model isn't listed, set Model Provider to Connect other models, and then connect any language model component.
2. To run the flow, click  Playground.
3. To test the Calculator tool, ask the agent a simple math question, such as I want to add 4 and 4.
To help you test and evaluate your flows, the Playground shows the agent's reasoning process as it analyzes the prompt, selects a tool, and then uses the tool to generate a response.
In this case, a math question causes the agent to select the Calculator tool and use an action like evaluate_expression.

1. To test the URL tool, ask the agent about current events.
For this request, the agent selects the URL tool's fetch_content action, and then returns a summary of current news headlines.
2. When you are done testing the flow, click Close.

Next stepsNow that you've run your first flow, try these next steps:

- Edit your Simple Agent flow by attaching different tools or adding more components to the flow.
- Build your own flows from scratch or by modifying other template flows.
- Integrate flows into your applications, as explained in Run your flows from external applications.

## Run your flows from external applications​

Langflow is an IDE, but it's also a runtime you can call through the Langflow API with Python, JavaScript, or HTTP.

When you start Langflow locally, you can send requests to the local Langflow server.
For production applications, you need to deploy a stable Langflow instance to handle API calls.

For example, you can use the /run endpoint to run a flow and get the result.

Langflow provides code snippets to help you get started with the Langflow API.

1. When editing a flow, click Share, and then click API access.
The default code in the API access pane constructs a request with the Langflow server url, headers, and a payload of request data.
The code snippets automatically include the LANGFLOW_SERVER_ADDRESS and FLOW_ID values for the flow, and a script to include your LANGFLOW_API_KEY if you've set it as an environment variable in your terminal session.
Replace these values if you're using the code for a different server or flow.
The default Langflow server address is http://localhost:7860.
PythonJavaScriptcurl_29import requests_29_29url = "http://LANGFLOW_SERVER_ADDRESS/api/v1/run/FLOW_ID"  # The complete API endpoint URL for this flow_29_29# Request payload configuration_29payload = {_29    "output_type": "chat",_29    "input_type": "chat",_29    "input_value": "hello world!"_29}_29_29# Request headers_29headers = {_29    "Content-Type": "application/json",_29    "x-api-key": "$LANGFLOW_API_KEY"_29}_29_29try:_29    # Send API request_29    response = requests.request("POST", url, json=payload, headers=headers)_29    response.raise_for_status()  # Raise exception for bad status codes_29_29    # Print response_29    print(response.text)_29_29except requests.exceptions.RequestException as e:_29    print(f"Error making API request: {e}")_29except ValueError as e:_29    print(f"Error parsing response: {e}")_20const payload = {_20    "output_type": "chat",_20    "input_type": "chat",_20    "input_value": "hello world!",_20    "session_id": "user_1"_20};_20_20const options = {_20    method: 'POST',_20    headers: {_20        'Content-Type': 'application/json',_20        'x-api-key': 'LANGFLOW_API_KEY'_20    },_20    body: JSON.stringify(payload)_20};_20_20fetch('http://LANGFLOW_SERVER_ADDRESS/api/v1/run/FLOW_ID', options)_20    .then(response => response.json())_20    .then(response => console.log(response))_20    .catch(err => console.error(err));_11curl --request POST \_11     --url 'http://LANGFLOW_SERVER_ADDRESS/api/v1/run/FLOW_ID?stream=false' \_11     --header 'Content-Type: application/json' \_11     --header "x-api-key: LANGFLOW_API_KEY" \_11     --data '{_11      "output_type": "chat",_11      "input_type": "chat",_11      "input_value": "hello world!"_11      }'_11_11# A 200 response confirms the call succeeded.
2. Copy the snippet, paste it in a script file, and then run the script to send the request.
If you are using the curl snippet, you can run the command directly in your terminal.

If the request is successful, the response includes many details about the flow run, including the session ID, inputs, outputs, components, durations, and more.
The following is an example of a response from running the Simple Agent template flow:

Result`_162{_162  "session_id": "29deb764-af3f-4d7d-94a0-47491ed241d6",_162  "outputs": [_162    {_162      "inputs": {_162        "input_value": "hello world!"_162      },_162      "outputs": [_162        {_162          "results": {_162            "message": {_162              "text_key": "text",_162              "data": {_162                "timestamp": "2025-06-16 19:58:23 UTC",_162                "sender": "Machine",_162                "sender_name": "AI",_162                "session_id": "29deb764-af3f-4d7d-94a0-47491ed241d6",_162                "text": "Hello world! 🌍 How can I assist you today?",_162                "files": [],_162                "error": false,_162                "edit": false,_162                "properties": {_162                  "text_color": "",_162                  "background_color": "",_162                  "edited": false,_162                  "source": {_162                    "id": "Agent-ZOknz",_162                    "display_name": "Agent",_162                    "source": "gpt-4o-mini"_162                  },_162                  "icon": "bot",_162                  "allow_markdown": false,_162                  "positive_feedback": null,_162                  "state": "complete",_162                  "targets": []_162                },_162                "category": "message",_162                "content_blocks": [_162                  {_162                    "title": "Agent Steps",_162                    "contents": [_162                      {_162                        "type": "text",_162                        "duration": 2,_162                        "header": {_162                          "title": "Input",_162                          "icon": "MessageSquare"_162                        },_162                        "text": "**Input**: hello world!"_162                      },_162                      {_162                        "type": "text",_162                        "duration": 226,_162                        "header": {_162                          "title": "Output",_162                          "icon": "MessageSquare"_162                        },_162                        "text": "Hello world! 🌍 How can I assist you today?"_162                      }_162                    ],_162                    "allow_markdown": true,_162                    "media_url": null_162                  }_162                ],_162                "id": "f3d85d9a-261c-4325-b004-95a1bf5de7ca",_162                "flow_id": "29deb764-af3f-4d7d-94a0-47491ed241d6",_162                "duration": null_162              },_162              "default_value": "",_162              "text": "Hello world! 🌍 How can I assist you today?",_162              "sender": "Machine",_162              "sender_name": "AI",_162              "files": [],_162              "session_id": "29deb764-af3f-4d7d-94a0-47491ed241d6",_162              "timestamp": "2025-06-16T19:58:23+00:00",_162              "flow_id": "29deb764-af3f-4d7d-94a0-47491ed241d6",_162              "error": false,_162              "edit": false,_162              "properties": {_162                "text_color": "",_162                "background_color": "",_162                "edited": false,_162                "source": {_162                  "id": "Agent-ZOknz",_162                  "display_name": "Agent",_162                  "source": "gpt-4o-mini"_162                },_162                "icon": "bot",_162                "allow_markdown": false,_162                "positive_feedback": null,_162                "state": "complete",_162                "targets": []_162              },_162              "category": "message",_162              "content_blocks": [_162                {_162                  "title": "Agent Steps",_162                  "contents": [_162                    {_162                      "type": "text",_162                      "duration": 2,_162                      "header": {_162                        "title": "Input",_162                        "icon": "MessageSquare"_162                      },_162                      "text": "**Input**: hello world!"_162                    },_162                    {_162                      "type": "text",_162                      "duration": 226,_162                      "header": {_162                        "title": "Output",_162                        "icon": "MessageSquare"_162                      },_162                      "text": "Hello world! 🌍 How can I assist you today?"_162                    }_162                  ],_162                  "allow_markdown": true,_162                  "media_url": null_162                }_162              ],_162              "duration": null_162            }_162          },_162          "artifacts": {_162            "message": "Hello world! 🌍 How can I assist you today?",_162            "sender": "Machine",_162            "sender_name": "AI",_162            "files": [],_162            "type": "object"_162          },_162          "outputs": {_162            "message": {_162              "message": "Hello world! 🌍 How can I assist you today?",_162              "type": "text"_162            }_162          },_162          "logs": {_162            "message": []_162          },_162          "messages": [_162            {_162              "message": "Hello world! 🌍 How can I assist you today?",_162              "sender": "Machine",_162              "sender_name": "AI",_162              "session_id": "29deb764-af3f-4d7d-94a0-47491ed241d6",_162              "stream_url": null,_162              "component_id": "ChatOutput-aF5lw",_162              "files": [],_162              "type": "text"_162            }_162          ],_162          "timedelta": null,_162          "duration": null,_162          "component_display_name": "Chat Output",_162          "component_id": "ChatOutput-aF5lw",_162          "used_frozen_result": false_162        }_162      ]_162    }_162  ]_162}`In a production application, you probably want to select parts of this response to return to the user, store in logs, and so on. The next steps demonstrate how you can extract data from a Langflow API response to use in your application.

### Extract data from the response​

The following example builds on the API pane's example code to create a question-and-answer chat in your terminal that stores the agent's previous answer.

1. Incorporate your Simple Agent flow's /run snippet into the following script.
This script runs a question-and-answer chat in your terminal and stores the agent's previous answer so you can compare them.
PythonJavaScript_59import requests_59import json_59_59url = "http://LANGFLOW_SERVER_ADDRESS/api/v1/run/FLOW_ID"_59_59def ask_agent(question):_59    payload = {_59        "output_type": "chat",_59        "input_type": "chat",_59        "input_value": question,_59    }_59_59    headers = {_59    "Content-Type": "application/json",_59    "x-api-key": "LANGFLOW_API_KEY"_59    }_59_59    try:_59        response = requests.post(url, json=payload, headers=headers)_59        response.raise_for_status()_59_59        # Get the response message_59        data = response.json()_59        message = data["outputs"][0]["outputs"][0]["outputs"]["message"]["message"]_59        return message_59_59    except Exception as e:_59        return f"Error: {str(e)}"_59_59def extract_message(data):_59    try:_59        return data["outputs"][0]["outputs"][0]["outputs"]["message"]["message"]_59    except (KeyError, IndexError):_59        return None_59_59# Store the previous answer from ask_agent response_59previous_answer = None_59_59# the terminal chat_59while True:_59    # Get user input_59    print("\nAsk the agent anything, such as 'What is 15 * 7?' or 'What is the capital of France?')")_59    print("Type 'quit' to exit or 'compare' to see the previous answer")_59    user_question = input("Your question: ")_59_59    if user_question.lower() == 'quit':_59        break_59    elif user_question.lower() == 'compare':_59        if previous_answer:_59            print(f"\nPrevious answer was: {previous_answer}")_59        else:_59            print("\nNo previous answer to compare with!")_59        continue_59_59    # Get and display the answer_59    result = ask_agent(user_question)_59    print(f"\nAgent's answer: {result}")_59    # Store the answer for comparison_59    previous_answer = result_74const readline = require('readline');_74_74const rl = readline.createInterface({_74    input: process.stdin,_74    output: process.stdout_74});_74_74const url = 'http://LANGFLOW_SERVER_ADDRESS/api/v1/run/FLOW_ID';_74_74// Store the previous answer from askAgent response_74let previousAnswer = null;_74_74// the agent flow, with question as input_value_74async function askAgent(question) {_74    const payload = {_74        "output_type": "chat",_74        "input_type": "chat",_74        "input_value": question_74    };_74_74    const options = {_74        method: 'POST',_74        headers: {_74            'Content-Type': 'application/json',_74            'x-api-key': 'LANGFLOW_API_KEY'_74        },_74        body: JSON.stringify(payload)_74    };_74_74    try {_74        const response = await fetch(url, options);_74        const data = await response.json();_74_74        // Extract the message from the nested response_74        const message = data.outputs[0].outputs[0].outputs.message.message;_74        return message;_74    } catch (error) {_74        return `Error: ${error.message}`;_74    }_74}_74_74// the terminal chat_74async function startChat() {_74    console.log("\nAsk the agent anything, such as 'What is 15 * 7?' or 'What is the capital of France?'");_74    console.log("Type 'quit' to exit or 'compare' to see the previous answer");_74_74    const askQuestion = () => {_74        rl.question('\nYour question: ', async (userQuestion) => {_74            if (userQuestion.toLowerCase() === 'quit') {_74                rl.close();_74                return;_74            }_74_74            if (userQuestion.toLowerCase() === 'compare') {_74                if (previousAnswer) {_74                    console.log(`\nPrevious answer was: ${previousAnswer}`);_74                } else {_74                    console.log("\nNo previous answer to compare with!");_74                }_74                askQuestion();_74                return;_74            }_74_74            const result = await askAgent(userQuestion);_74            console.log(`\nAgent's answer: ${result}`);_74            previousAnswer = result;_74            askQuestion();_74        });_74    };_74_74    askQuestion();_74}_74_74startChat();
2. To view the agent's previous answer, type compare. To close the terminal chat, type exit.

### Use tweaks to apply temporary overrides to a flow run​

You can include tweaks with your requests to temporarily modify flow parameters.
Tweaks are added to the API request, and temporarily change component parameters within your flow.
Tweaks override the flow's components' settings for a single run only.
They don't modify the underlying flow configuration or persist between runs.

Tweaks are added to the /run endpoint's payload.
To assist with formatting, you can define tweaks in Langflow's Input Schema pane before copying the code snippet.

1. To open the Input Schema pane, from the API access pane, click Input Schema.
2. In the Input Schema pane, select the parameter you want to modify in your next request.
Enabling parameters in the Input Schema pane doesn't permanently change the listed parameters. It only adds them to the sample code snippets.
3. For example, to change the LLM provider from OpenAI to Groq, and include your Groq API key with the request, select the values Model Providers, Model, and Groq API Key.
Langflow updates the tweaks object in the code snippets based on your input parameters, and includes default values to guide you.
Use the updated code snippets in your script to run your flow with your overrides.

`_12payload = {_12    "output_type": "chat",_12    "input_type": "chat",_12    "input_value": "hello world!",_12    "tweaks": {_12        "Agent-ZOknz": {_12            "agent_llm": "Groq",_12            "api_key": "GROQ_API_KEY",_12            "model_name": "llama-3.1-8b-instant"_12        }_12    }_12}`## Next steps​

- Trigger flows with the Langflow API
- Use Langflow as a Model Context Protocol (MCP) server
- Containerize a Langflow application
- File management
