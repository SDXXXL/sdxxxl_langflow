# Create custom Python components | Langflow Documentation

- Components reference
- Create custom Python components

On this page# Create custom Python components

[data-ch-theme="github-dark"] {  --ch-t-colorScheme: dark;--ch-t-foreground: #c9d1d9;--ch-t-background: #0d1117;--ch-t-lighter-inlineBackground: #0d1117e6;--ch-t-editor-background: #0d1117;--ch-t-editor-foreground: #c9d1d9;--ch-t-editor-lineHighlightBackground: #6e76811a;--ch-t-editor-rangeHighlightBackground: #ffffff0b;--ch-t-editor-infoForeground: #3794FF;--ch-t-editor-selectionBackground: #264F78;--ch-t-focusBorder: #1f6feb;--ch-t-tab-activeBackground: #0d1117;--ch-t-tab-activeForeground: #c9d1d9;--ch-t-tab-inactiveBackground: #010409;--ch-t-tab-inactiveForeground: #8b949e;--ch-t-tab-border: #30363d;--ch-t-tab-activeBorder: #0d1117;--ch-t-editorGroup-border: #30363d;--ch-t-editorGroupHeader-tabsBackground: #010409;--ch-t-editorLineNumber-foreground: #6e7681;--ch-t-input-background: #0d1117;--ch-t-input-foreground: #c9d1d9;--ch-t-input-border: #30363d;--ch-t-icon-foreground: #8b949e;--ch-t-sideBar-background: #010409;--ch-t-sideBar-foreground: #c9d1d9;--ch-t-sideBar-border: #30363d;--ch-t-list-activeSelectionBackground: #6e768166;--ch-t-list-activeSelectionForeground: #c9d1d9;--ch-t-list-hoverBackground: #6e76811a;--ch-t-list-hoverForeground: #c9d1d9; }Create your own custom components to add any functionality you need to Langflow, from API integrations to data processing.

In Langflow's node-based environment, each node is a "component" that performs discrete functions.
Custom components in Langflow are built upon:

- The Python class that inherits from Component.
- Class-level attributes that identify and describe the component.
- Input and output lists that determine data flow.
- Methods that define the component's behavior and logic.
- Internal variables for Error handling and logging

Use the Custom component quickstart to add an example component to Langflow, and then use the reference guide that follows for more advanced component customization.

## Custom component quickstart​

Create a custom DataFrameProcessor component by creating a Python file, saving it in the correct folder, including an __init__.py file, and loading it into Langflow.

### Create a Python file​

[data-ch-theme="github-dark"] {  --ch-t-colorScheme: dark;--ch-t-foreground: #c9d1d9;--ch-t-background: #0d1117;--ch-t-lighter-inlineBackground: #0d1117e6;--ch-t-editor-background: #0d1117;--ch-t-editor-foreground: #c9d1d9;--ch-t-editor-lineHighlightBackground: #6e76811a;--ch-t-editor-rangeHighlightBackground: #ffffff0b;--ch-t-editor-infoForeground: #3794FF;--ch-t-editor-selectionBackground: #264F78;--ch-t-focusBorder: #1f6feb;--ch-t-tab-activeBackground: #0d1117;--ch-t-tab-activeForeground: #c9d1d9;--ch-t-tab-inactiveBackground: #010409;--ch-t-tab-inactiveForeground: #8b949e;--ch-t-tab-border: #30363d;--ch-t-tab-activeBorder: #0d1117;--ch-t-editorGroup-border: #30363d;--ch-t-editorGroupHeader-tabsBackground: #010409;--ch-t-editorLineNumber-foreground: #6e7681;--ch-t-input-background: #0d1117;--ch-t-input-foreground: #c9d1d9;--ch-t-input-border: #30363d;--ch-t-icon-foreground: #8b949e;--ch-t-sideBar-background: #010409;--ch-t-sideBar-foreground: #c9d1d9;--ch-t-sideBar-border: #30363d;--ch-t-list-activeSelectionBackground: #6e768166;--ch-t-list-activeSelectionForeground: #c9d1d9;--ch-t-list-hoverBackground: #6e76811a;--ch-t-list-hoverForeground: #c9d1d9; }1. Create a Python file for your component, such as dataframe_processor.py.
2. Write your component as an object of the Component class. Create a new class that inherits from Component and override the base class's methods.
Backwards compatibilityThe lfx import path replaced the import from langflow.custom import Component in Langflow 1.7, but the original input is still compatible and works the same way.
_10from typing import Any, Dict, Optional_10import pandas as pd_10from lfx.custom.custom_component.component import Component_10_10class DataFrameProcessor(Component):_10    """A component that processes pandas DataFrames with various operations."""
3. Define class attributes to provide information about your custom component:
_13from typing import Any, Dict, Optional_13import pandas as pd_13from lfx.custom.custom_component.component import Component_13_13class DataFrameProcessor(Component):_13    """A component that processes pandas DataFrames with various operations."""_13_13    display_name: str = "DataFrame Processor"_13    description: str = "Process and transform pandas DataFrames with various operations like filtering, sorting, and aggregation."_13    documentation: str = "https://docs.langflow.org/components-dataframe-processor"_13    icon: str = "DataframeIcon"_13    priority: int = 100_13    name: str = "dataframe_processor"
display_name: A user-friendly name shown in the visual editor.
description: A brief description of what your component does.
documentation: A link to detailed documentation.
icon: An emoji or icon identifier for visual representation.
Langflow uses Lucide for icons. To assign an icon to your component, set the icon attribute to the name of a Lucide icon as a string, such as icon = "file-text". Langflow renders icons from the Lucide library automatically.
For more information, see Contributing bundles.
priority: An optional integer to control display order. Lower numbers appear first.
name: An optional internal identifier that defaults to class name.
4. Define the component's interface by specifying its inputs, outputs, and the method that will process them. The method name must match the method field in your outputs list, as this is how Langflow knows which method to call to generate each output.
This example creates a minimal custom component skeleton.
_21from typing import Any, Dict, Optional_21import pandas as pd_21from lfx.custom.custom_component.component import Component_21_21class DataFrameProcessor(Component):_21    """A component that processes pandas DataFrames with various operations."""_21_21    display_name: str = "DataFrame Processor"_21    description: str = "Process and transform pandas DataFrames with various operations like filtering, sorting, and aggregation."_21    documentation: str = "https://docs.langflow.org/components-dataframe-processor"_21    icon: str = "DataframeIcon"_21    priority: int = 100_21    name: str = "dataframe_processor"_21_21    # input and output lists_21    inputs = []_21    outputs = []_21_21    # method_21    def some_output_method(self):_21        return ...

### Save the custom component​

Save the custom component in the Langflow directory where the UI will discover and load it.

By default, Langflow looks for custom components in the src/lfx/src/lfx/components directory.

When saving components in the default directory, components must be organized in a specific directory structure to be properly loaded and displayed in the visual editor.

Components must be placed inside category folders, not directly in the base directory.

The category folder name determines where the component appears in the Langflow  Core components menu.
For example, to add the example DataFrameProcessor component to the Data category, place it in the data subfolder:

`_10src/lfx/src/lfx/components/_10    └── data/                      # Category folder (determines menu location)_10        ├── __init__.py            # Required - makes it a Python package_10        └── dataframe_processor.py # Your custom component file`If you're creating custom components in a different location using the LANGFLOW_COMPONENTS_PATH environment variable, components must be similarly organized in a specific directory structure to be displayed in the visual editor.

`_10/your/custom/components/path/    # Base directory set by LANGFLOW_COMPONENTS_PATH_10    └── category_name/_10        ├── __init__.py_10        └── custom_component.py`You can have multiple category folders to organize components into different categories:

`_10/app/custom_components/_10    ├── data/_10    │   ├── __init__.py_10    │   └── dataframe_processor.py_10    └── tools/_10        ├── __init__.py_10        └── custom_tool.py`### Create the __init__.py file​

Each category directory must contain an __init__.py file for Langflow to properly recognize and load the components.
This is a Python package requirement that ensures the directory is treated as a module.

To include the DataFrameProcessor component, create a file named __init__.py in your component's directory with the following content.

`_10from .dataframe_processor import DataFrameProcessor_10_10__all__ = ["DataFrameProcessor"]`Lazy load the DataFrameProcessor componentAlternatively, you can load your component lazily, which is better for performance but a little more complex.

`_32from __future__ import annotations_32_32from typing import TYPE_CHECKING, Any_32_32from lfx.components._importing import import_mod_32_32if TYPE_CHECKING:_32    from lfx.components.data.dataframe_processor import DataFrameProcessor_32_32_dynamic_imports = {_32    "DataFrameProcessor": "dataframe_processor",_32}_32_32__all__ = [_32    "DataFrameProcessor",_32]_32_32def __getattr__(attr_name: str) -> Any:_32    """Lazily import data components on attribute access."""_32    if attr_name not in _dynamic_imports:_32        msg = f"module '{__name__}' has no attribute '{attr_name}'"_32        raise AttributeError(msg)_32    try:_32        result = import_mod(attr_name, _dynamic_imports[attr_name], __spec__.parent)_32    except (ModuleNotFoundError, ImportError, AttributeError) as e:_32        msg = f"Could not import '{attr_name}' from '{__name__}': {e}"_32        raise AttributeError(msg) from e_32    globals()[attr_name] = result_32    return result_32_32def __dir__() -> list[str]:_32    return list(__all__)`For an additional example of lazy loading, see the FAISS component.

### Load your component​

Ensure the application builds your component.

1. To rebuild the backend and frontend, run make install_frontend && make build_frontend && make install_backend && uv run langflow run --port 7860.
2. Refresh the frontend application.
Your new DataFrameProcessor component is available in the  Core components menu under the Data category in the visual editor.

### Docker deployment​

When running Langflow in Docker, mount your custom components directory and set the LANGFLOW_COMPONENTS_PATH environment variable in the docker run command to point to the custom components directory.

`_10docker run -d \_10  --name langflow \_10  -p 7860:7860 \_10  -v ./custom_components:/app/custom_components \_10  -e LANGFLOW_COMPONENTS_PATH=/app/custom_components \_10  langflowai/langflow:latest`Create the same custom components directory structure as the example in Save the custom component.

`_10/app/custom_components/          # LANGFLOW_COMPONENTS_PATH_10    └── data/_10        ├── __init__.py_10        └── dataframe_processor.py`## How components execute​

Langflow's engine manages:

1. Instantiation:  A component is created and internal structures are initialized.
2. Assigning Inputs: Values from the visual editor or connections are assigned to component fields.
3. Validation and Setup: Optional hooks like _pre_run_setup.
4. Outputs Generation: run() or build_results() triggers output methods.

You can customize execution by overriding these optional hooks in your custom component code.

- _pre_run_setup() - Used during Validation and Setup.
Add this method inside your component class to initialize component state before execution begins:
_10class MyComponent(Component):_10    # ... your inputs, outputs, and other attributes ..._10_10    def _pre_run_setup(self):_10        if not hasattr(self, "_initialized"):_10            self._initialized = True_10            self.iteration = 0
- Override run or _run - Used during Outputs Generation.
Add this method inside your component class to customize the main execution logic:
_10class MyComponent(Component):_10_10    async def_run(self):_10        # Custom execution logic here_10        # This runs instead of the default output method calls_10        pass
- Store data in self.ctx.
Use self.ctx in any of your component methods to share data between method calls.
_15class MyComponent(Component):_15_15    def _pre_run_setup(self):_15        # Initialize counter in setup_15        self.ctx["processed_items"] = 0_15_15    def process_data(self) -> Data:_15        # Increment counter during processing_15        self.ctx["processed_items"] += 1_15        return Data(data={"item": f"processed {self.ctx['processed_items']}"})_15_15    def get_summary(self) -> Data:_15        # Access counter in different method_15        total = self.ctx["processed_items"]_15        return Data(data={"summary": f"Processed {total} items total"})

## Inputs and outputs​

Inputs and outputs are class-level configurations that define how data flows through the component, how it appears in the visual editor, and how connections to other components are validated.

### Inputs​

Inputs are defined in a class-level inputs list. When Langflow loads the component, it uses this list to render component fields and ports in the visual editor. Users or other components provide values or connections to fill these inputs.

An input is usually an instance of a class from lfx.io (such as StrInput, DataInput, or MessageTextInput).

For example, this component has three inputs: a text field (StrInput), a Boolean toggle (BoolInput), and a dropdown selection (DropdownInput).

`_10from lfx.io import StrInput, BoolInput, DropdownInput_10_10inputs = [_10    StrInput(name="title", display_name="Title"),_10    BoolInput(name="enabled", display_name="Enabled", value=True),_10    DropdownInput(name="mode", display_name="Mode", options=["Fast", "Safe", "Experimental"], value="Safe")_10]`The StrInput creates a single-line text field for entering text. The name="title" parameter means you access this value in your component methods with self.title, while display_name="Title" shows "Title" as the label in the visual editor.

The BoolInput creates a boolean toggle that's enabled by default with value=True. Users can turn this on or off, and you access the current state with self.enabled.

The DropdownInput provides a selection menu with three predefined options: "Fast", "Safe", and "Experimental".
The value="Safe" sets "Safe" as the default selection, and you access the user's choice with self.mode.

For a list of all available parameters, see the BaseInputMixin definition in the Langflow codebase.

For a list of all available input types, see the input type definitions in the Langflow codebase.

`_10from lfx.io import StrInput, DataInput, MultilineInput, IntInput, BoolInput, DropdownInput, FileInput, CodeInput, ModelInput, HandleInput, Output`### Outputs​

Outputs are defined in a class-level outputs list. When Langflow renders a component, each output becomes a connector point in the visual editor. When you connect something to an output, Langflow automatically calls the corresponding method and passes the returned object to the next component.

An output is usually an instance of Output from lfx.io.

For example, this component has one output that returns a DataFrame:

`_16from lfx.io import Output_16from lfx.schema import DataFrame_16_16outputs = [_16    Output(_16        name="df_out",_16        display_name="DataFrame Output",_16        method="build_df"_16    )_16]_16_16def build_df(self) -> DataFrame:_16    # Process data and return DataFrame_16    df = DataFrame({"col1": [1, 2], "col2": [3, 4]})_16    self.status = f"Built DataFrame with {len(df)} rows."_16    return df`The Output creates a connector point in the visual editor labeled DataFrame Output. The name="df_out" parameter identifies this output, while display_name="DataFrame Output" shows the label in the UI. The method="build_df" parameter tells Langflow to call the build_df method when this output is connected to another component.

The build_df method processes data and returns a DataFrame. The -> DataFrame type annotation helps Langflow validate connections and provides color-coding in the visual editor. You can also set self.status to show progress messages in the UI.

For a complete list of all available parameters, see the Output class definition in the Langflow codebase. Common parameters include:

Additional return types:

- Message: Structured chat messages
- Data: Flexible object with .data and optional .text
- DataFrame: Tabular data (pandas DataFrame subclass)
- Primitive types: str, int, bool, not recommended for type consistency

#### Associated methods​

Each output is linked to a method where the output method name must match the method name. The method typically returns objects like Message, Data, or DataFrame, and can use inputs with self.<input_name>.

For example, the Output defines a connector point called file_contents that will call the read_file method when connected. The read_file method accesses the filename input with self.filename, reads the file content, sets a status message, and returns the content wrapped in a Data object.

`_12Output(_12    name="file_contents",_12    display_name="File Contents",_12    method="read_file"_12)_12_12def read_file(self) -> Data:_12    path = self.filename_12    with open(path, "r") as f:_12        content = f.read()_12    self.status = f"Read {len(content)} chars from {path}"_12    return Data(data={"content": content})`#### Components with multiple outputs​

A component can define multiple outputs.
Each output can have a different corresponding method.

For example:

`_10outputs = [_10    Output(display_name="Processed Data", name="processed_data", method="process_data"),_10    Output(display_name="Debug Info", name="debug_info", method="provide_debug_info"),_10]`By default, components in Langflow that produce multiple outputs only allow one output selection in the visual editor.
The component will have only one output port where the user can select the preferred output type.

This behavior is controlled by the group_outputs parameter:

- group_outputs=False (default): When a component has more than one output and group_outputs is false or not set, the outputs are grouped in the visual editor, and the user must select one.
Use this option when the component is expected to return only one type of output when used in a flow.
- group_outputs=True: All outputs are available simultaneously in the visual editor. The component has one output port for each output, and the user can connect zero or more outputs to other components.
Use this option when the component is expected to return multiple values that are used in parallel by downstream components or processes.

- False or not set
- True

In this example, the visual editor provides a single output port, and the user can select one of the outputs.
Since group_outputs=False is the default behavior, it doesn't need to be explicitly set in the component, as shown in this example.

`_12outputs = [_12    Output(_12        name="structured_output",_12        display_name="Structured Output",_12        method="build_structured_output",_12    ),_12    Output(_12        name="dataframe_output",_12        display_name="DataFrame Output",_12        method="build_structured_dataframe",_12    ),_12]`In this example, all outputs are available simultaneously in the visual editor.

`_14outputs = [_14    Output(_14        name="true_result",_14        display_name="True",_14        method="true_response",_14        group_outputs=True,_14    ),_14    Output(_14        name="false_result",_14        display_name="False",_14        method="false_response",_14        group_outputs=True,_14    ),_14]`### Tool mode​

Components that support Tool Mode can be used as standalone components (when not in Tool Mode) or as tools for other components with a Tools input, such as Agent components.

You can allow a custom component to support Tool Mode by setting tool_mode=True:

`_10inputs = [_10    MessageTextInput(_10        name="message",_10        display_name="Mensage",_10        info="Enter the message that will be processed directly by the tool",_10        tool_mode=True,_10    ),_10]`## Typed annotations​

In Langflow, typed annotations allow Langflow to visually guide users and maintain flow consistency.
Always annotate your output methods with return types like -> Data, -> Message, or -> DataFrame to enable proper visual editor color-coding and validation.
Use Data, Message, or DataFrame wrappers instead of returning plain structures for better consistency. Stay consistent with types across your components to make flows predictable and easier to build.

Typed annotations provide color-coding where outputs like -> Data or -> Message get distinct colors, automatic validation that blocks incompatible connections, and improved readability for users to quickly understand data flow between components.

### Common return types​

- Message
- Data
- DataFrame
- Primitive Types

For chat-style outputs. Connects to any of several Message-compatible inputs.

`_10def produce_message(self) -> Message:_10    return Message(text="Hello! from typed method!", sender="System")`For structured data like dicts or partial texts. Connects only to DataInput (ports that accept Data).

`_10def get_processed_data(self) -> Data:_10    processed = {"key1": "value1", "key2": 123}_10    return Data(data=processed)`For tabular data. Connects only to DataFrameInput (ports that accept DataFrame).

`_10def build_df(self) -> DataFrame:_10    pdf = pd.DataFrame({"A": [1, 2], "B": [3, 4]})_10    return DataFrame(pdf)`Returning primitives is allowed, but wrapping in Data or Message is recommended for better consistency in the visual editor.

`_10def compute_sum(self) -> int:_10    return sum(self.numbers)`## Enable dynamic fields​

In Langflow, dynamic fields allow inputs to change or appear based on user interactions. You can make an input dynamic by setting dynamic=True. Optionally, setting real_time_refresh=True triggers the update_build_config method to adjust the input's visibility or properties in real time, creating a contextual visual editor experience that only exposes relevant fields based on the user's choices.

In this example, the operator field triggers updates with real_time_refresh=True.
The regex_pattern field is initially hidden and controlled with dynamic=True.

`_23from lfx.custom import Component_23from lfx.io import DropdownInput, StrInput_23_23class RegexRouter(Component):_23    display_name = "Regex Router"_23    description = "Demonstrates dynamic fields for regex input."_23_23    inputs = [_23        DropdownInput(_23            name="operator",_23            display_name="Operator",_23            options=["equals", "contains", "regex"],_23            value="equals",_23            real_time_refresh=True,_23        ),_23        StrInput(_23            name="regex_pattern",_23            display_name="Regex Pattern",_23            info="Used if operator='regex'",_23            dynamic=True,_23            show=False,_23        ),_23    ]`### Show or hide fields based on user selections​

When a user changes a field with real_time_refresh=True, Langflow calls your update_build_config method.

This method lets you show, hide, or modify other fields based on what the user selected.

This example shows the regex_pattern field only when the user selects "regex" from the operator dropdown.

`_10def update_build_config(self, build_config: dict, field_value: str, field_name: str | None = None) -> dict:_10    if field_name == "operator":_10        if field_value == "regex":_10            build_config["regex_pattern"]["show"] = True_10        else:_10            build_config["regex_pattern"]["show"] = False_10    return build_config`You can modify additional field properties in update_build_config other than just show and hide.

- required: Make fields required or optional dynamically
_10if field_value == "regex":_10    build_config["regex_pattern"]["required"] = True_10else:_10    build_config["regex_pattern"]["required"] = False
- advanced: Move fields to the "Advanced" section
_10if field_value == "experimental":_10    build_config["regex_pattern"]["advanced"] = False  # Show in main section_10else:_10    build_config["regex_pattern"]["advanced"] = True   # Hide in advanced
- options: Change dropdown options based on other selections
_10if field_value == "regex":_10    build_config["operator"]["options"] = ["regex", "contains", "starts_with"]_10else:_10    build_config["operator"]["options"] = ["equals", "contains", "not_equals"]

## Error handling and logging​

You can raise standard Python exceptions such as ValueError or specialized exceptions like ToolException when validation fails. Langflow automatically catches these and displays appropriate error messages in the visual editor, helping users quickly identify what went wrong.

`_10def compute_result(self) -> str:_10    if not self.user_input:_10        raise ValueError("No input provided.")_10    # ...`Alternatively, instead of stopping a flow abruptly, you can return a Data object containing an "error" field. This approach allows the flow to continue operating and enables downstream components to detect and handle the error gracefully.

`_10def run_model(self) -> Data:_10    try:_10        # ..._10    except Exception as e:_10        return Data(data={"error": str(e)})`Langflow provides several tools to help you debug and manage component execution. You can use self.status to display short messages about execution results directly in the visual editor, making troubleshooting easier for users.

`_10def parse_data(self) -> Data:_10# ..._10self.status = f"Parsed {len(rows)} rows successfully."_10return Data(data={"rows": rows})`You can halt individual output paths when certain conditions fail using self.stop(), without stopping other outputs from the same component.

This example stops the output if the user input is empty, preventing the component from processing invalid data.

`_10def some_output(self) -> Data:_10if not self.user_input or len(self.user_input.strip()) == 0:_10    self.stop("some_output")_10    return Data(data={"error": "Empty input provided"})`You can log key execution details inside components using self.log(). These logs are stored as structured data and displayed in the "Logs" or "Events" section of the component's detail view, and can be accessed later through the Logs button in the visual editor or exported files.

Component logs are distinct from Langflow's main application logging system. self.log() creates component-specific logs that appear in the UI, while Langflow's main logging system uses structlog for application-level logging  that outputs to langflow.log files. For more information, see Logs.

This example logs a message when the component starts processing a file.

`_10def process_file(self, file_path: str):_10self.log(f"Processing file {file_path}")`## Contribute custom components to Langflow​

To contribute your custom component to the Langflow project, see Contribute components.
