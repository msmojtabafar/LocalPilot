import os

from localpilot.process_tool import ProcessTool


def test_process_tool_properties():
    tool = ProcessTool()

    assert tool.name == "process"
    assert tool.description == (
        "List running processes and get process information"
    )


def test_list_processes():
    tool = ProcessTool()

    result = tool.execute("list")

    assert isinstance(result, list)
    assert len(result) > 0

    current_pid = os.getpid()

    process = next(
        (
            item
            for item in result
            if item["pid"] == current_pid
        ),
        None,
    )

    assert process is not None
    assert process["name"] != ""


def test_process_info():
    tool = ProcessTool()

    result = tool.execute(
        "info",
        os.getpid(),
    )

    assert result is not None
    assert result["pid"] == os.getpid()
    assert result["name"] != ""


def test_invalid_pid():
    tool = ProcessTool()

    result = tool.execute(
        "info",
        999999999,
    )

    assert result is None


def test_invalid_action():
    tool = ProcessTool()

    assert tool.execute("invalid") is None
