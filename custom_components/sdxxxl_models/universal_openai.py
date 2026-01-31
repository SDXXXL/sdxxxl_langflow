import json
import urllib.request
import urllib.error
from typing import Any, List
from langchain_openai import ChatOpenAI, OpenAIEmbeddings

from lfx.base.models.model import LCModelComponent
from lfx.field_typing import Embeddings, LanguageModel
from lfx.schema.dotdict import dotdict
from lfx.inputs.inputs import MessageInput, StrInput, BoolInput, IntInput
from lfx.io import DropdownInput, MultilineInput, SecretStrInput, SliderInput, Output
from lfx.field_typing.range_spec import RangeSpec


DEFAULT_OPENAI_MODELS = [
    "gpt-4o",
    "gpt-4o-mini",
    "gpt-4-turbo",
    "gpt-3.5-turbo",
    "o1-preview",
    "o1-mini",
    "gpt-4",
    "gpt-4-32k",
    "gpt-3.5-turbo-16k",
    "gpt-3.5-turbo-1106",
    "gpt-4-0125-preview",
    "gpt-4-turbo-preview",
]

MODEL_SOURCES = [
    "default",
    "auto-fetch",
    "custom"
]

OUTPUT_TYPES = [
    "llm",
    "embeddings"
]

OUTPUT_MODES = [
    "response",
    "model"
]

PLACEHOLDER_MESSAGES = {
    "missing_base_url": "Please enter API Base URL first",
    "missing_api_key": "API Key required for this endpoint",
    "fetch_failed": "Enter model name manually",
    "fetch_success": "Success: Found {count} models",
    "empty_response": "Warning: API returned empty model list",
    "invalid_json": "Error: Invalid JSON response",
    "timeout": "Error: Request timed out (15s)",
    "connection_failed": "Error: Connection failed - {reason}",
    "http_error": "Error: HTTP {code} - {reason}",
    "unknown_error": "Error: {message}",
}

CUSTOM_MODEL_OPTION = "custom-model"


class UniversalOpenAIComponent(LCModelComponent):
    display_name = "Universal OpenAI Compatible Model"
    description = "Connect to any OpenAI compatible API service with auto model list fetching"
    documentation: str = "https://platform.openai.com/docs/api-reference"
    icon = "globe"
    category = "models"
    priority = 100

    def _fetch_models_from_api(self) -> tuple[List[str], str]:
        base_url = self.base_url.rstrip("/")
        models_url = f"{base_url}/models"
        api_key = self.api_key if self.api_key else None

        try:
            # Configure proxy for the request
            proxy_handler = None
            if self.enable_proxy == "true" and self.proxy_url:
                formatted_proxy_url = self._format_proxy_url(self.proxy_url)
                proxy_handler = urllib.request.ProxyHandler({
                    'http': formatted_proxy_url,
                    'https': formatted_proxy_url
                })
            
            # Create opener with or without proxy
            if proxy_handler:
                opener = urllib.request.build_opener(proxy_handler)
            else:
                opener = urllib.request.build_opener()
            
            req = urllib.request.Request(models_url)
            if api_key:
                req.add_header("Authorization", f"Bearer {api_key}")
            req.add_header("Content-Type", "application/json")

            with opener.open(req, timeout=15) as response:
                data = json.loads(response.read().decode())
                models = self._parse_models_from_response(data)
                
                if models:
                    models.append(CUSTOM_MODEL_OPTION)
                    return models, PLACEHOLDER_MESSAGES["fetch_success"].format(count=len(models) - 1)
                else:
                    return [], PLACEHOLDER_MESSAGES["empty_response"]

        except urllib.error.HTTPError as e:
            return [], self._format_http_error(e)
        except urllib.error.URLError as e:
            return [], PLACEHOLDER_MESSAGES["connection_failed"].format(reason=e.reason)
        except TimeoutError:
            return [], PLACEHOLDER_MESSAGES["timeout"]
        except json.JSONDecodeError:
            return [], PLACEHOLDER_MESSAGES["invalid_json"]
        except Exception as e:
            return [], PLACEHOLDER_MESSAGES["unknown_error"].format(message=str(e))

    def _parse_models_from_response(self, data: dict) -> List[str]:
        models = []
        
        if "data" in data:
            for item in data.get("data", []):
                model_id = item.get("id", "")
                if model_id:
                    models.append(model_id)
        elif "models" in data:
            for item in data.get("models", []):
                model_id = item.get("id") or item.get("name") or item.get("model")
                if model_id:
                    models.append(model_id)
        elif isinstance(data, list):
            for item in data:
                model_id = item.get("id") or item.get("name") or item.get("model")
                if model_id:
                    models.append(model_id)
        
        return models

    def _format_http_error(self, e: urllib.error.HTTPError) -> str:
        error_messages = {
            401: "Error: 401 Unauthorized - Check API key",
            403: "Error: 403 Forbidden - Check permissions",
            404: "Error: 404 Not Found - /models endpoint not supported",
        }
        if e.code in error_messages:
            return error_messages[e.code]
        return PLACEHOLDER_MESSAGES["http_error"].format(code=e.code, reason=e.reason)

    def _format_proxy_url(self, proxy_url: str) -> str:
        """Validate and format proxy URL. Only HTTP protocol is supported."""
        if not proxy_url:
            return ""
        
        proxy_url = proxy_url.strip()
        
        if not proxy_url.startswith('http://'):
            raise ValueError(
                f"Invalid proxy URL format: '{proxy_url}'. "
                "Only HTTP proxies are supported. Please use format: http://127.0.0.1:7890"
            )
        
        return proxy_url

    inputs = [
        StrInput(
            name="base_url",
            display_name="API Base URL",
            info="Base API address, e.g., https://api.openai.com/v1 or http://localhost:8000/v1",
            value="https://api.openai.com/v1",
            required=True,
        ),
        SecretStrInput(
            name="api_key",
            display_name="API Key",
            info="API key, leave empty if authentication is not required",
            required=False,
        ),
        DropdownInput(
            name="output_type",
            display_name="Output Type",
            options=OUTPUT_TYPES,
            value="llm",
            info="Select the output type: LLM for text generation or Embeddings for vector embeddings",
            real_time_refresh=True,
        ),
        DropdownInput(
            name="output_mode",
            display_name="Output Mode",
            options=OUTPUT_MODES,
            value="response",
            info="response: returns model response text; model: returns language model object for chaining",
            real_time_refresh=True,
        ),
        DropdownInput(
            name="model_source",
            display_name="Model Source",
            options=MODEL_SOURCES,
            value="default",
            info="default: preset model list; auto-fetch: fetch from API; custom: enter model name manually",
            real_time_refresh=True,
        ),
        DropdownInput(
            name="model_name",
            display_name="Model Name",
            options=DEFAULT_OPENAI_MODELS,
            value=DEFAULT_OPENAI_MODELS[0],
            info="Select the model to use",
            real_time_refresh=True,
        ),
        StrInput(
            name="custom_model_name",
            display_name="Custom Model Name",
            info="Enter the full model name when using custom model source",
            value="",
            show=False,
        ),
        MessageInput(
            name="input_value",
            display_name="Input",
            info="Input text to send to the model",
            show=True,
        ),
        MultilineInput(
            name="system_message",
            display_name="System Message",
            info="System prompt to set model behavior",
            advanced=False,
            show=True,
        ),
        SliderInput(
            name="temperature",
            display_name="Temperature",
            value=0.7,
            info="Controls randomness of output, higher values make output more random (0-2)",
            range_spec=RangeSpec(min=0, max=2, step=0.01),
            advanced=True,
            show=True,
        ),
        SliderInput(
            name="max_tokens",
            display_name="Max Tokens",
            value=4096,
            info="Maximum number of tokens to generate",
            range_spec=RangeSpec(min=1, max=32768, step=1),
            advanced=True,
            show=True,
        ),
        BoolInput(
            name="stream",
            display_name="Stream Output",
            info="Enable streaming response",
            value=False,
            advanced=True,
            show=True,
        ),
        IntInput(
            name="dimensions",
            display_name="Embedding Dimensions",
            value=1536,
            info="The number of dimensions the resulting output embeddings should have. Only supported by certain models.",
            advanced=True,
            show=False,
        ),
        IntInput(
            name="chunk_size",
            display_name="Chunk Size",
            value=1000,
            info="The chunk size to use when processing documents for embeddings.",
            advanced=True,
            show=False,
        ),
        DropdownInput(
            name="enable_proxy",
            display_name="Enable Proxy",
            options=["false", "true"],
            value="false",
            info="Enable proxy server for API requests",
            advanced=False,
            real_time_refresh=True,
        ),
        StrInput(
            name="proxy_url",
            display_name="Proxy URL (http only)",
            info="HTTP proxy server address (e.g., http://127.0.0.1:7890)",
            value="",
            show=False,
            dynamic=True,
        ),
    ]

    outputs = [
        Output(display_name="Model Response", name="text_output", method="text_response"),
        Output(display_name="Language Model", name="model_output", method="build_model"),
        Output(display_name="Embedding Model", name="embeddings", method="build_embeddings"),
    ]

    def build_model(self) -> LanguageModel:
        base_url = self.base_url.rstrip("/")
        model_name = self.model_name
        api_key = self.api_key if self.api_key else None
        
        if model_name == CUSTOM_MODEL_OPTION and self.custom_model_name:
            model_name = self.custom_model_name

        # Configure proxy if enabled
        openai_proxy = None
        if self.enable_proxy == "true" and self.proxy_url:
            openai_proxy = self._format_proxy_url(self.proxy_url)

        return ChatOpenAI(
            base_url=base_url,
            api_key=api_key,
            model=model_name,
            temperature=self.temperature,
            max_tokens=self.max_tokens,
            streaming=self.stream,
            openai_api_key=api_key,
            openai_api_base=base_url,
            timeout=60,
            max_retries=2,
            openai_proxy=openai_proxy,
        )

    def build_embeddings(self) -> Embeddings:
        base_url = self.base_url.rstrip("/")
        model_name = self.model_name
        api_key = self.api_key if self.api_key else None

        if model_name == CUSTOM_MODEL_OPTION and self.custom_model_name:
            model_name = self.custom_model_name

        openai_proxy = None
        if self.enable_proxy == "true" and self.proxy_url:
            openai_proxy = self._format_proxy_url(self.proxy_url)

        return OpenAIEmbeddings(
            model=model_name,
            base_url=base_url,
            api_key=api_key,
            dimensions=self.dimensions or None,
            chunk_size=self.chunk_size,
            openai_proxy=openai_proxy,
        )

    def _get_base_url_from_build_config(self, build_config: dotdict) -> str:
        base_url_field = build_config.get("base_url", {})
        if isinstance(base_url_field, dict):
            return base_url_field.get("value", "")
        return str(base_url_field)

    def _update_model_name_field(
        self, build_config: dotdict, options: List[str], value: str, info: str, show: bool
    ) -> None:
        build_config["model_name"]["options"] = options
        build_config["model_name"]["value"] = value
        build_config["model_name"]["info"] = info
        build_config["model_name"]["show"] = show

    async def update_build_config(
        self, build_config: dotdict, field_value: Any, field_name: str | None = None
    ) -> dotdict:
        # Handle output type changes
        if field_name == "output_type":
            if field_value == "embeddings":
                build_config["input_value"]["show"] = False
                build_config["system_message"]["show"] = False
                build_config["temperature"]["show"] = False
                build_config["max_tokens"]["show"] = False
                build_config["stream"]["show"] = False
                build_config["dimensions"]["show"] = True
                build_config["chunk_size"]["show"] = True
                build_config["output_mode"]["show"] = False
            else:
                build_config["input_value"]["show"] = True
                build_config["system_message"]["show"] = True
                build_config["temperature"]["show"] = True
                build_config["max_tokens"]["show"] = True
                build_config["stream"]["show"] = True
                build_config["dimensions"]["show"] = False
                build_config["chunk_size"]["show"] = False
                build_config["output_mode"]["show"] = True
                build_config["output_mode"]["value"] = "response"
            return build_config

        # Handle output mode changes
        if field_name == "output_mode":
            if field_value == "model":
                build_config["input_value"]["show"] = False
                build_config["system_message"]["show"] = False
            else:
                build_config["input_value"]["show"] = True
                build_config["system_message"]["show"] = True
            return build_config

        # Handle proxy field updates
        if field_name == "enable_proxy":
            if field_value == "true":
                build_config["proxy_url"]["show"] = True
                build_config["proxy_url"]["info"] = "Proxy server address (e.g., http://127.0.0.1:7890, 127.0.0.1:7890, socks5://127.0.0.1:1080)"
            else:
                build_config["proxy_url"]["show"] = False
                build_config["proxy_url"]["value"] = ""
            return build_config
        
        # Handle proxy URL field updates (format the URL)
        if field_name == "proxy_url" and field_value:
            formatted_url = self._format_proxy_url(field_value)
            if formatted_url != field_value:
                build_config["proxy_url"]["value"] = formatted_url
            return build_config
        
        # Handle model source updates
        if field_name != "model_source":
            return build_config

        base_url = self._get_base_url_from_build_config(build_config)
        api_key = self.api_key if self.api_key else None

        if field_value == "default":
            self._update_model_name_field(
                build_config,
                DEFAULT_OPENAI_MODELS,
                DEFAULT_OPENAI_MODELS[0],
                "Select from preset list",
                True
            )
            build_config["custom_model_name"]["show"] = False

        elif field_value == "auto-fetch":
            if not base_url:
                self._update_model_name_field(
                    build_config,
                    [PLACEHOLDER_MESSAGES["missing_base_url"]],
                    "",
                    PLACEHOLDER_MESSAGES["missing_base_url"],
                    True
                )
                build_config["custom_model_name"]["show"] = False
                return build_config

            if not api_key:
                self._update_model_name_field(
                    build_config,
                    [PLACEHOLDER_MESSAGES["missing_api_key"]],
                    "",
                    PLACEHOLDER_MESSAGES["missing_api_key"],
                    True
                )
                build_config["custom_model_name"]["show"] = False
                return build_config

            models, status_msg = self._fetch_models_from_api()

            if models:
                self._update_model_name_field(
                    build_config,
                    models,
                    models[0],
                    status_msg,
                    True
                )
                build_config["custom_model_name"]["show"] = False
            else:
                self._update_model_name_field(
                    build_config,
                    [PLACEHOLDER_MESSAGES["fetch_failed"]],
                    "",
                    status_msg,
                    True
                )
                build_config["custom_model_name"]["show"] = False

        elif field_value == "custom":
            build_config["model_name"]["show"] = False
            build_config["custom_model_name"]["show"] = True
            build_config["custom_model_name"]["info"] = PLACEHOLDER_MESSAGES["fetch_failed"]

        return build_config

    def update_outputs(self, frontend_node: dict, field_name: str, field_value: Any) -> dict:
        """Dynamically update output ports based on output_mode selection."""
        if field_name in {"output_mode", "output_type"}:
            output_mode = getattr(self, "output_mode", "response")
            output_type = field_value if field_name == "output_type" else getattr(self, "output_type", "llm")

            frontend_node["outputs"] = []

            if output_type == "embeddings":
                frontend_node["outputs"].append(
                    Output(
                        display_name="Embedding Model",
                        name="embeddings",
                        method="build_embeddings",
                    )
                )
            else:
                if output_mode == "response":
                    frontend_node["outputs"].append(
                        Output(
                            display_name="Model Response",
                            name="text_output",
                            method="text_response",
                        )
                    )
                frontend_node["outputs"].append(
                    Output(
                        display_name="Language Model",
                        name="model_output",
                        method="build_model",
                    )
                )

        return frontend_node

    def validate_configuration(self) -> List[str]:
        errors = []
        
        if not self.base_url:
            errors.append("API Base URL is required")
        elif not self.base_url.startswith(("http://", "https://")):
            errors.append("API Base URL must start with http:// or https://")
        
        if self.model_name == CUSTOM_MODEL_OPTION and not self.custom_model_name:
            errors.append("Custom model name is required")
        
        return errors
