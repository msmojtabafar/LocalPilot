import json

from localpilot.assistant import LocalPilotAssistant
from localpilot.command_tool import CommandTool
from localpilot.llm import LocalLLM
from localpilot.tool_manager import ToolManager


class DummyClient:
    def __init__(self, response):
        self.response = response

    def generate(self, prompt):
        return self.response


def create_assistant(response):
    client = DummyClient(response)
    llm = LocalLLM(client)

    manager = ToolManager()
    manager.register(CommandTool())

    return LocalPilotAssistant(
        llm,
        manager,
    )


def test_assistant_normal_response():
    assistant = create_assistant("Hello from LocalPilot")

    result = assistant.respond("Hello")

    assert result == "Hello from LocalPilot"


def test_assistant_tool_call():
    response = json.dumps({
        "tool": "command",
        "args": ["echo", "hello"],
    })

    assistant = create_assistant(response)

    result = assistant.respond(
        "Run echo hello",
        confirmed=True,
    )

    assert result["returncode"] == 0
    assert result["stdout"].strip() == "hello"


def test_assistant_empty_message():
    assistant = create_assistant("Hello")

    assert assistant.respond("") is None


def test_conversation_is_saved():
    assistant = create_assistant("Hello")

    assistant.respond("Test message")

    messages = assistant.context.get_messages()

    assert messages[0]["role"] == "user"
    assert messages[0]["content"] == "Test message"
    assert messages[1]["role"] == "assistant"
