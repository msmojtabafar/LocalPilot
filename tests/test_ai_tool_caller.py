from localpilot.ai_tool_caller import AIToolCaller
from localpilot.tool import Tool
from localpilot.tool_manager import ToolManager


class DummyLLM:
    def __init__(self, response):
        self.response = response

    def generate(self, prompt):
        return self.response


class DummyTool(Tool):
    def __init__(self):
        super().__init__("dummy", "Dummy tool")

    def execute(self, *args):
        return "executed"


def test_plain_llm_response():
    caller = AIToolCaller(
        DummyLLM("Hello"),
        ToolManager(),
    )

    assert caller.call("hello") == "Hello"


def test_tool_call():
    manager = ToolManager()
    manager.register(DummyTool())

    caller = AIToolCaller(
        DummyLLM('{"tool": "dummy", "args": []}'),
        manager,
    )

    result = caller.call("run dummy", confirmed=True)

    assert result["allowed"] is True
    assert result["result"] == "executed"


def test_tool_call_requires_permission():
    manager = ToolManager()
    manager.register(DummyTool())

    caller = AIToolCaller(
        DummyLLM('{"tool": "dummy", "args": []}'),
        manager,
    )

    result = caller.call("run dummy")

    assert result["allowed"] is False
    assert result["error"] == "Permission denied"


def test_invalid_tool():
    caller = AIToolCaller(
        DummyLLM('{"tool": "unknown", "args": []}'),
        ToolManager(),
    )

    assert caller.call("run unknown") is None


def test_invalid_json():
    caller = AIToolCaller(
        DummyLLM("{invalid json"),
        ToolManager(),
    )

    assert caller.call("hello") == "{invalid json"


def test_invalid_args_are_normalized():
    manager = ToolManager()
    manager.register(DummyTool())

    caller = AIToolCaller(
        DummyLLM('{"tool": "dummy", "args": "test"}'),
        manager,
    )

    result = caller.call("run dummy", confirmed=True)

    assert result["allowed"] is True
