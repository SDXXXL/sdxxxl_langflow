# Build flows | Langflow Documentation

- Flows
- Build flows

On this page# Build flows

A flow is a functional representation of an application workflow.
Flows receive input, process it, and produce output.

Flows consist of components that represent individual steps in your application's workflow.

Langflow flows are fully serializable and can be saved and loaded from the file system where Langflow is installed.

tipTo try building and running a flow in a few minutes, see the Langflow quickstart.

## Create a flow​

From the Projects page, there are four ways to create a flow:

- Create a blank flow: Select a project, click New Flow, and then click Blank Flow.
- Create a flow from a template: Select a project, click New Flow, and then click the template that you want to use.
What are templates?Templates are pre-built flows that you can use as a starting point for your own flow.
They range from basic flows with a few components to complex flows with many components and sub-flows.For example, the Basic Prompting template demonstrates a small flow that passes both chat input and pre-defined instructions (as a prompt) to an LLM.
In contrast, the Vector Store RAG template consists of two sub-flows that demonstrate how to create a Retrieval Augmented Generation (RAG) chatbot. One sub-flow populates the vector store with contextually relevant data and embeddings, and the other sub-flow queries the vector store for similar data to answer user questions.You can also contribute templates to the Langflow codebase.
- Duplicate an existing flow: Locate the flow you want to copy, click  More, and then select Duplicate.
- Import a flow: See Import and export flows.

You can also create a flow with the Langflow API, but the Langflow team recommends using the visual editor until you are familiar with flow creation.

### Add components​

Flows consist of components, which are nodes that you configure and connect in the workspace.
Each component performs a specific task, like serving an AI model or connecting a data source.

Drag and drop components from the  Core components and  Bundles menus to add them to your flow.
Then, configure the component settings and connect the components together.

Each component has configuration settings and options. Some of these are common to all components, and some are unique to specific components.

To form a cohesive flow, you connect components by edges or ports, which have a specific data type they receive or send.
For example, message ports send text strings between components.

For more information about component configuration, including port types and underlying component code, see Components overview.

### Run a flow​

After you build a prototype flow, you can test it in the Playground.
When you're ready to use Langflow for application development, learn how to trigger flows with the Langflow API, explore more advanced configuration options like custom dependencies, and, eventually, containerize your Langflow application.

When you're ready to go to production or deploy a Langflow MCP server for access over the public internet, see Langflow deployment overview.

#### Flow graphs​

When a flow runs, Langflow builds a Directed Acyclic Graph (DAG) object from the nodes (components) and edges (connections), and the nodes are sorted to determine the order of execution.

The graph build calls each component's def_build function to validate and prepare the nodes.
This graph is then processed in dependency order.
Each node is built and executed sequentially, with results from each built node being passed to nodes that are dependent on that node's results.

## Manage flows in projects​

The Projects page is where you arrive when you launch Langflow.
From here, you can manage flows and your projects' MCP servers.

Langflow projects are like folders that you can use to organize related flows.
The default project is Starter Project, and your flows are stored here unless you create another project.
To create a project, click  Create new project.

tipTo get back to the Projects page after editing a flow, click the project name or Langflow icon in the Langflow header.

### Edit flow details​

1. On the Projects page, locate the flow you want to edit.
2. Click  More, and then select Edit details.
3. Edit the Name and Description, and then click Save.

### Lock a flow​

To prevent changes to a flow, you can lock it:

1. On the Projects page, locate the flow you want to lock.
2. Click  More, and then select Edit details.
3. Enable Lock Flow, and then click Save.

Repeat these steps to unlock the flow by disabling Lock Flow.

When editing a flow, the Lock Status indicates whether the flow is  Locked or  Unlocked.
You cannot change the lock status while editing the flow.

### Move a flow​

To move a flow from one project to another, do the following:

1. On the Projects page, locate the flow you want to move.
2. Click and drag the flow from the list of flows to the target project name in the list of projects.

### Delete a flow​

1. On the Projects page, locate the flow you want to delete.
2. Click  More, and then select Delete.

## Flow storage and logs​

By default, flows and flow execution data are stored in the Langflow database, and flow logs are stored with other Langflow logs in the Langflow config directory.
For more information, see Memory management options and Logging.

## See also​

- Share and embed flows
- Import and export flows
- Langflow environment variables
