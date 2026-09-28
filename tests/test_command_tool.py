from localpilot.command_tool import CommandTool


def test_command_tool_properties():
    tool = CommandTool()

    assert tool.name == "command"
    assert tool.description == "Execute a system command"


def test_command_execution():
    tool = CommandTool()

    result = tool.execute("echo", "hello")

    assert result["returncode"] == 0
    assert result["stdout"].strip() == "hello"
    assert result["stderr"] == ""


def test_command_error():
    tool = CommandTool()

    result = tool.execute("sh", "-c", "echo error >&2; exit 1")

    assert result["returncode"] == 1
    assert result["stderr"].strip() == "error"


def test_no_command():
    tool = CommandTool()

    result = tool.execute()

    assert result["returncode"] != 0
    assert "No command provided" in result["stderr"]


def test_invalid_command():
    tool = CommandTool()

    result = tool.execute("command_that_does_not_exist_12345")

    assert result["returncode"] != 0
    assert result["stderr"] != ""
