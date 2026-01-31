from __future__ import annotations

import json
import re
from typing import TYPE_CHECKING, Any

from pydantic import ValidationError

from lfx.components.models_and_agents.memory import MemoryComponent

if TYPE_CHECKING:
    from langchain_core.tools import Tool

from lfx.base.agents.agent import LCToolsAgentComponent
from lfx.base.agents.events import ExceptionWithMessageError
from lfx.components.helpers import CurrentDateComponent
from lfx.components.langchain_utilities.tool_calling import ToolCallingAgentComponent
from lfx.custom.custom_component.component import get_component_toolkit
from lfx.helpers.base_model import build_model_from_schema
from lfx.inputs.inputs import BoolInput, HandleInput, MultilineInput
from lfx.io import IntInput, MessageTextInput, Output, TableInput
from lfx.log.logger import logger
from lfx.schema.data import Data
from lfx.schema.dotdict import dotdict
from lfx.schema.message import Message
from lfx.schema.table import EditMode


def set_advanced_true(component_input):
    component_input.advanced = True
    return component_input


class UniversalAgentComponent(ToolCallingAgentComponent):
    display_name: str = "Universal Agent"
    description: str = (
        "Agent with support for any OpenAI-compatible API. "
        "Connect a LanguageModel from Universal OpenAI Compatible Model component."
    )
    documentation: str = "https://docs.langflow.org/agents"
    icon = "globe"
    beta = False
    name = "UniversalAgent"

    memory_inputs = [set_advanced_true(component_input) for component_input in MemoryComponent().inputs]

    inputs = [
        HandleInput(
            name="llm",
            display_name="Language Model",
            input_types=["LanguageModel"],
            required=True,
            info="Connect a LanguageModel from Universal OpenAI Compatible Model or other LLM components.",
        ),
        MultilineInput(
            name="system_prompt",
            display_name="Agent Instructions",
            info="System Prompt: Initial instructions and context provided to guide the agent's behavior.",
            value="You are a helpful assistant that can use tools to answer questions and perform tasks.",
            advanced=False,
        ),
        MessageTextInput(
            name="context_id",
            display_name="Context ID",
            info="The context ID of the chat. Adds an extra layer to the local memory.",
            value="",
            advanced=True,
        ),
        IntInput(
            name="n_messages",
            display_name="Number of Chat History Messages",
            value=100,
            info="Number of chat history messages to retrieve.",
            advanced=True,
            show=True,
        ),
        MultilineInput(
            name="format_instructions",
            display_name="Output Format Instructions",
            info="Generic Template for structured output formatting. Valid only with Structured response.",
            value=(
                "You are an AI that extracts structured JSON objects from unstructured text. "
                "Use a predefined schema with expected types (str, int, float, bool, dict). "
                "Extract ALL relevant instances that match the schema - if multiple patterns exist, capture them all. "
                "Fill missing or ambiguous values with defaults: null for missing values. "
                "Remove exact duplicates but keep variations that have different field values. "
                "Always return valid JSON in the expected format, never throw errors. "
                "If multiple objects can be extracted, return them all in the structured format."
            ),
            advanced=True,
        ),
        TableInput(
            name="output_schema",
            display_name="Output Schema",
            info=(
                "Schema Validation: Define the structure and data types for structured output. "
                "No validation if no output schema."
            ),
            advanced=True,
            required=False,
            value=[],
            table_schema=[
                {
                    "name": "name",
                    "display_name": "Name",
                    "type": "str",
                    "description": "Specify the name of the output field.",
                    "default": "field",
                    "edit_mode": EditMode.INLINE,
                },
                {
                    "name": "description",
                    "display_name": "Description",
                    "type": "str",
                    "description": "Describe the purpose of the output field.",
                    "default": "description of field",
                    "edit_mode": EditMode.POPOVER,
                },
                {
                    "name": "type",
                    "display_name": "Type",
                    "type": "str",
                    "edit_mode": EditMode.INLINE,
                    "description": ("Indicate the data type of the output field (e.g., str, int, float, bool, dict)."),
                    "options": ["str", "int", "float", "bool", "dict"],
                    "default": "str",
                },
                {
                    "name": "multiple",
                    "display_name": "As List",
                    "type": "boolean",
                    "description": "Set to True if this output field should be a list of the specified type.",
                    "default": "False",
                    "edit_mode": EditMode.INLINE,
                },
            ],
        ),
        *LCToolsAgentComponent.get_base_inputs(),
        BoolInput(
            name="add_current_date_tool",
            display_name="Current Date",
            advanced=True,
            info="If true, will add a tool to the agent that returns the current date.",
            value=True,
        ),
    ]

    outputs = [
        Output(name="response", display_name="Response", method="message_response"),
    ]

    def _has_external_llm(self) -> bool:
        """Check if an external LanguageModel is connected."""
        return hasattr(self, 'llm') and self.llm is not None

    async def get_agent_requirements(self):
        """Get the agent requirements for the agent.

        Uses the external LanguageModel from the llm input.
        """
        from langchain_core.language_models import BaseLanguageModel
        from langchain_core.tools import StructuredTool

        if not self._has_external_llm():
            msg = (
                "No LanguageModel connected. "
                "Please connect a LanguageModel input from Universal OpenAI Compatible Model or other LLM components."
            )
            raise ValueError(msg)

        llm_model = self.llm
        if not isinstance(llm_model, BaseLanguageModel):
            msg = (
                "Connected input is not a valid LanguageModel. "
                "Please connect a LanguageModel output from Universal OpenAI Compatible Model or other LLM components."
            )
            raise ValueError(msg)

        self.chat_history = await self.get_memory_data()
        await logger.adebug(f"Retrieved {len(self.chat_history)} chat history messages")
        if isinstance(self.chat_history, Message):
            self.chat_history = [self.chat_history]

        if self.add_current_date_tool:
            if not isinstance(self.tools, list):
                self.tools = []
            current_date_tool = (await CurrentDateComponent(**self.get_base_args()).to_toolkit()).pop(0)

            if not isinstance(current_date_tool, StructuredTool):
                msg = "CurrentDateComponent must be converted to a StructuredTool"
                raise TypeError(msg)
            self.tools.append(current_date_tool)

        self.set_tools_callbacks(self.tools, self._get_shared_callbacks())

        return llm_model, self.chat_history, self.tools

    async def build_structured_output_base(self, content: str):
        """Build structured output with optional BaseModel validation."""
        json_pattern = r"\{.*\}"
        schema_error_msg = "Try setting an output schema"

        json_data = None
        try:
            json_data = json.loads(content)
        except json.JSONDecodeError:
            json_match = re.search(json_pattern, content, re.DOTALL)
            if json_match:
                try:
                    json_data = json.loads(json_match.group())
                except json.JSONDecodeError:
                    return {"content": content, "error": schema_error_msg}
            else:
                return {"content": content, "error": schema_error_msg}

        if not hasattr(self, "output_schema") or not self.output_schema or len(self.output_schema) == 0:
            return json_data

        try:
            processed_schema = self._preprocess_schema(self.output_schema)
            output_model = build_model_from_schema(processed_schema)

            if isinstance(json_data, list):
                validated_objects = []
                for item in json_data:
                    try:
                        validated_obj = output_model.model_validate(item)
                        validated_objects.append(validated_obj.model_dump())
                    except ValidationError as e:
                        await logger.aerror(f"Validation error for item: {e}")
                        validated_objects.append({"data": item, "validation_error": str(e)})
                return validated_objects

            try:
                validated_obj = output_model.model_validate(json_data)
                return [validated_obj.model_dump()]
            except ValidationError as e:
                await logger.aerror(f"Validation error: {e}")
                return [{"data": json_data, "validation_error": str(e)}]

        except (TypeError, ValueError) as e:
            await logger.aerror(f"Error building structured output: {e}")
            return json_data

    async def json_response(self) -> Data:
        """Convert agent response to structured JSON Data output with schema validation."""
        try:
            system_components = []

            agent_instructions = getattr(self, "system_prompt", "") or ""
            if agent_instructions:
                system_components.append(f"{agent_instructions}")

            format_instructions = getattr(self, "format_instructions", "") or ""
            if format_instructions:
                system_components.append(f"Format instructions: {format_instructions}")

            if hasattr(self, "output_schema") and self.output_schema and len(self.output_schema) > 0:
                try:
                    processed_schema = self._preprocess_schema(self.output_schema)
                    output_model = build_model_from_schema(processed_schema)
                    schema_dict = output_model.model_json_schema()
                    schema_info = (
                        "You are given some text that may include format instructions, "
                        "explanations, or other content alongside a JSON schema.\n\n"
                        "Your task:\n"
                        "- Extract only the JSON schema.\n"
                        "- Return it as valid JSON.\n"
                        "- Do not include format instructions, explanations, or extra text.\n\n"
                        "Input:\n"
                        f"{json.dumps(schema_dict, indent=2)}\n\n"
                        "Output (only JSON schema):"
                    )
                    system_components.append(schema_info)
                except (ValidationError, ValueError, TypeError, KeyError) as e:
                    await logger.aerror(f"Could not build schema for prompt: {e}", exc_info=True)

            combined_instructions = "\n\n".join(system_components) if system_components else ""
            llm_model, self.chat_history, self.tools = await self.get_agent_requirements()
            self.set(
                llm=llm_model,
                tools=self.tools or [],
                chat_history=self.chat_history,
                input_value=self.input_value,
                system_prompt=combined_instructions,
            )

            try:
                structured_agent = self.create_agent_runnable()
            except (NotImplementedError, ValueError, TypeError) as e:
                await logger.aerror(f"Error with structured chat agent: {e}")
                raise
            try:
                result = await self.run_agent(structured_agent)
            except (
                ExceptionWithMessageError,
                ValueError,
                TypeError,
                RuntimeError,
            ) as e:
                await logger.aerror(f"Error with structured agent result: {e}")
                raise
            if hasattr(result, "content"):
                content = result.content
            elif hasattr(result, "text"):
                content = result.text
            else:
                content = str(result)

        except (
            ExceptionWithMessageError,
            ValueError,
            TypeError,
            NotImplementedError,
            AttributeError,
        ) as e:
            await logger.aerror(f"Error with structured chat agent: {e}")
            content_str = "No content returned from agent"
            return Data(data={"content": content_str, "error": str(e)})

        try:
            structured_output = await self.build_structured_output_base(content)

            if isinstance(structured_output, list) and structured_output:
                if len(structured_output) == 1:
                    return Data(data=structured_output[0])
                return Data(data={"results": structured_output})
            if isinstance(structured_output, dict):
                return Data(data=structured_output)
            return Data(data={"content": content})

        except (ValueError, TypeError) as e:
            await logger.aerror(f"Error in structured output processing: {e}")
            return Data(data={"content": content, "error": str(e)})

    async def get_memory_data(self):
        messages = (
            await MemoryComponent(**self.get_base_args())
            .set(
                session_id=self.graph.session_id,
                context_id=self.context_id,
                order="Ascending",
                n_messages=self.n_messages,
            )
            .retrieve_messages()
        )
        return [
            message for message in messages if getattr(message, "id", None) != getattr(self.input_value, "id", None)
        ]

    def _preprocess_schema(self, schema):
        """Preprocess schema to ensure correct data types for build_model_from_schema."""
        processed_schema = []
        for field in schema:
            processed_field = {
                "name": str(field.get("name", "field")),
                "type": str(field.get("type", "str")),
                "description": str(field.get("description", "")),
                "multiple": field.get("multiple", False),
            }
            if isinstance(processed_field["multiple"], str):
                processed_field["multiple"] = processed_field["multiple"].lower() in [
                    "true",
                    "1",
                    "t",
                    "y",
                    "yes",
                ]
            processed_schema.append(processed_field)
        return processed_schema

    def update_input_types(self, build_config: dotdict) -> dotdict:
        """Update input types for all fields in build_config."""
        for key, value in build_config.items():
            if isinstance(value, dict):
                if value.get("input_types") is None:
                    build_config[key]["input_types"] = []
            elif hasattr(value, "input_types") and value.input_types is None:
                value.input_types = []
        return build_config

    async def _get_tools(self) -> list[Tool]:
        component_toolkit = get_component_toolkit()
        tools_names = self._build_tools_names()
        agent_description = self.get_tool_description()
        description = f"{agent_description}{tools_names}"

        tools = component_toolkit(component=self).get_tools(
            tool_name="Call_Agent",
            tool_description=description,
            callbacks=self.get_langchain_callbacks(),
        )
        if hasattr(self, "tools_metadata"):
            tools = component_toolkit(component=self, metadata=self.tools_metadata).update_tools_metadata(tools=tools)

        return tools
