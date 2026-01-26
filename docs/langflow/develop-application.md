# Containerize a Langflow application | Langflow Documentation

- Deploy
- Containerized deployments
- Containerize a Langflow application

On this page# Containerize a Langflow application

[data-ch-theme="github-dark"] {  --ch-t-colorScheme: dark;--ch-t-foreground: #c9d1d9;--ch-t-background: #0d1117;--ch-t-lighter-inlineBackground: #0d1117e6;--ch-t-editor-background: #0d1117;--ch-t-editor-foreground: #c9d1d9;--ch-t-editor-lineHighlightBackground: #6e76811a;--ch-t-editor-rangeHighlightBackground: #ffffff0b;--ch-t-editor-infoForeground: #3794FF;--ch-t-editor-selectionBackground: #264F78;--ch-t-focusBorder: #1f6feb;--ch-t-tab-activeBackground: #0d1117;--ch-t-tab-activeForeground: #c9d1d9;--ch-t-tab-inactiveBackground: #010409;--ch-t-tab-inactiveForeground: #8b949e;--ch-t-tab-border: #30363d;--ch-t-tab-activeBorder: #0d1117;--ch-t-editorGroup-border: #30363d;--ch-t-editorGroupHeader-tabsBackground: #010409;--ch-t-editorLineNumber-foreground: #6e7681;--ch-t-input-background: #0d1117;--ch-t-input-foreground: #c9d1d9;--ch-t-input-border: #30363d;--ch-t-icon-foreground: #8b949e;--ch-t-sideBar-background: #010409;--ch-t-sideBar-foreground: #c9d1d9;--ch-t-sideBar-border: #30363d;--ch-t-list-activeSelectionBackground: #6e768166;--ch-t-list-activeSelectionForeground: #c9d1d9;--ch-t-list-hoverBackground: #6e76811a;--ch-t-list-hoverForeground: #c9d1d9; }tipPodman can be used instead of Docker for all commands shown here. For more information, see the Podman documentation.

Designing flows in the visual editor is only the first step in building an application that uses Langflow.

Once you have a functional flow, you can use that flow in a larger application, such as a website or mobile app.
Because Langflow is both an IDE and a runtime, you can use Langflow to build and test your flows locally, and then package and serve your flows in a production environment.

This guide introduces application development with Langflow from initial setup through packaging and deployment.
This documentation doesn't explain how to write a complete application; it only describes how to include Langflow in the context of a larger application.

## Directory structure​

The following example describes the directory structure for a minimal Langflow application:

`_10LANGFLOW-APPLICATION/_10├── docker.env_10├── Dockerfile_10├── flows/_10│   ├── flow1.json_10│   └── flow2.json_10├── langflow-config-dir/_10├── README.md`This directory contains the following:

- docker.env: This file is copied to the Docker image as a .env file in the container root.
- Dockerfile: This file controls how your Langflow image is built.
- /flows: This folder holds the flows you want to host, which are the flows that your application uses.
- /langflow-config-dir: This folder is referenced in the Dockerfile as the location for your Langflow deployment's configuration files, database, and logs.
- README.md: This is a typical README file for your application's documentation.

This is a minimal example of a Langflow application directory.
Your application might have additional files and folders, such as a /components folder for custom components, or a pyproject.toml file for additional dependencies.

### Package management​

The base Langflow Docker image includes the Langflow core dependencies because it uses langflowai/langflow:latest as the parent image.

If your application requires additional dependencies, create a pyproject.toml file for the additional dependencies.
For more information, see Install custom dependencies.

To deploy an application with additional dependencies to Docker, you must copy the pyproject.toml and uv.lock files to the Docker image.
To do this, add the following to your Langflow application's Dockerfile:

`_10COPY pyproject.toml uv.lock /app/`### Environment variables​

The docker.env file is a .env file loaded into your Docker image.
It contains Langflow environment variables that are used in flows or control Langflow's behavior, such as authentication, database storage, API keys, and server configurations.
For example:

`_10LANGFLOW_AUTO_LOGIN=True_10LANGFLOW_SAVE_DB_IN_CONFIG_DIR=True_10LANGFLOW_BASE_URL=http://0.0.0.0:7860_10OPENAI_API_KEY=sk-...`You can set environment variables in the Dockerfile as well.
However, if you set an environment variable in both docker.env and the Dockerfile, Langflow uses the value set in docker.env.

Langflow can also create global variables from your environment variables, or use environment variables as a backup for missing global variables.

### Secrets​

For simplicity, the examples in the Langflow documentation might use direct references to API keys and other sensitive values.
In your own applications, you should always follow industry best practices for managing secrets, such as using environment variables or secret management tools.

For information about generating authentication keys and managing secrets in Langflow, see API keys and authentication.

### Storage​

By default, Langflow uses an SQLite database for storage.
If you prefer to use PostgreSQL, see Configure an external PostgreSQL database.

For more information about storage, including cache and memory, see Memory management options.

### Flows​

Your local Langflow instance might have many flows for different applications.
When you package Langflow as a dependency of an application, you only want to include the flows your application uses.

1. Export flows that are relevant to your application.
If you have chained flows (flows that trigger other flows), make sure you export all necessary flows.
2. Add the exported Langflow JSON files to the /flows folder in your application directory.

### Components​

The  Core components and  [Bundles] that you see in the Langflow visual editor are automatically included in the base Langflow Docker image.

If you have any custom components that you created for your application, you must include these components in your application directory:

1. Create a /components folder in your application directory.
2. Add your custom component files to the /components folder.
3. Specify the path to /components in your docker.env.

## Langflow Dockerfile​

The Dockerfile determines how your Langflow image is built, including the dependencies, flows, components, and configuration files.

At minimum, you need to specify the base Langflow image, create the necessary folders in the container, copy folders and files to the container, and provide a startup command.

`_29# Use the latest version of the base Langflow image_29FROM langflowai/langflow:latest_29_29# Create folders and set the working directory in the container_29RUN mkdir /app/flows_29RUN mkdir /app/langflow-config-dir_29WORKDIR /app_29_29# Copy flows, langflow-config-dir, and docker.env to the container_29COPY flows /app/flows_29COPY langflow-config-dir /app/langflow-config-dir_29COPY docker.env /app/.env_29_29# Optional: Copy custom components to the container_29COPY components /app/components_29_29# Optional: Use custom dependencies_29COPY pyproject.toml uv.lock /app/_29_29# Set environment variables if not set in docker.env_29ENV PYTHONPATH=/app_29ENV LANGFLOW_LOAD_FLOWS_PATH=/app/flows_29ENV LANGFLOW_CONFIG_DIR=/app/langflow-config-dir_29ENV LANGFLOW_COMPONENTS_PATH=/app/components_29ENV LANGFLOW_LOG_ENV=container_29_29# Command to run the Langflow server on port 7860_29EXPOSE 7860_29CMD ["langflow", "run", "--backend-only", "--env-file","/app/.env","--host", "0.0.0.0", "--port", "7860"]`The environment variables set directly in this Dockerfile specify resource paths for Langflow.
If these variables are also set in docker.env, the values in docker.env override the values set in the Dockerfile.

In this example, ENV LANGFLOW_LOG_ENV=container sets the logging behavior for serialized JSON to stdout to track the application's behavior in a containerized environment. For more information, see Logging.

### Backend-only mode​

The --backend-only flag in CMD starts Langflow in backend-only mode, which provides programmatic access only.
This is recommended when running Langflow as a dependency of an application where you don't need access to the visual editor.

If you want to serve the Langflow visual editor and backend, then omit --backend-only.

For more information, see Deploy Langflow on Docker.

## Test your Langflow Docker image​

Build and run your Langflow Docker image to test it.

This example runs the container locally.
For information about publishing your image on Docker Hub and running a Langflow container remotely, see Deploy to Docker Hub and Kubernetes.

1. Build the Docker image:
_10docker build -t langflow-pokedex:1.2.0 .
2. Run the Docker container to start your Langflow server:
_10docker run -p 7860:7860 langflow-pokedex:1.2.0
3. To confirm that the container is serving your flows as expected, use the Langflow API to run a flow:
Open one of the JSON files in your application's /flows folder, and then find the flow's id in the  additional metadata and project information.
There are many id values; make sure you get the ID for the entire flow, not the ID for an individual component.
If your flow is complex, try searching for the flow's name, which is typically near the flow's id.
_10"name": "Basic Prompting",_10"description": "Perform basic prompting with an OpenAI model.",_10"id": "e4167236-938f-4aca-845b-21de3f399858",
Send a POST request to the /v1/run/$FLOW_ID endpoint using the flow ID from the previous step .
The following example runs a simple LLM chat flow that responds to a chat input string.
If necessary, modify the payload for your flow.
For example, if your flow doesn't have a Chat Input component, you must modify the payload to provide the expected input for your flow.
_10curl --request POST \_10  --url 'http://localhost:7860/api/v1/run/e4167236-938f-4aca-845b-21de3f399858?stream=true' \_10  --header 'Content-Type: application/json' \_10  --data '{_10    "input_value": "Tell me about Charizard.",_10    "output_type": "chat",_10    "input_type": "chat",_10    "session_id": "charizard_test_request"_10}'
About this exampleThis command runs the Pokédex template flow.
It provides chat input about a specific Pokémon, uses an optional custom session_id, and enables response streaming with ?stream=true.The default session ID is the flow ID.
Custom session IDs can help isolate unique conversation threads to keep the LLM's context clean, and they can help identify specific conversations in flow logs to make debugging easier.This command uses response streaming because the Pokédex flow can return a large amount of text.
To use batching, set ?stream=false.
Verify that the request succeeds and the response is valid, depending on the specific flow you ran.
This confirms that your Langflow Docker image is correctly configured and this flow is accessible through the Langflow API server that is hosted on the container.
When you build and test your entire application stack, your front-end application can use Langflow API requests to trigger the flows served by your Langflow container in the same way you manually tested the flow in the previous step.
This example triggered a flow by sending chat input to the /v1/run/$FLOW_ID endpoint.
For more examples of flow triggers, see Trigger flows with webhooks and the tutorial to Create a chatbot that can ingest files.

## Deploy to Docker Hub and Kubernetes​

When you're ready to share your application with the world, you need to serve Langflow in a production environment.
For more information about deploying Langflow, see the following:

- Learn about Langflow deployments
- Deploy Langflow on Docker
- Deploy the Langflow production environment on Kubernetes
