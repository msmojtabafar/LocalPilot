from localpilot.file_tool import FileTool


def test_file_tool_properties():
    tool = FileTool()

    assert tool.name == "file"
    assert tool.description == "Read, write, list, and create files and directories"


def test_write_and_read(tmp_path):
    tool = FileTool()
    file_path = tmp_path / "test.txt"

    assert tool.execute("write", file_path, "hello") is True
    assert tool.execute("read", file_path) == "hello"


def test_list_directory(tmp_path):
    tool = FileTool()

    (tmp_path / "one.txt").write_text("one")
    (tmp_path / "two.txt").write_text("two")

    result = tool.execute("list", tmp_path)

    assert "one.txt" in result
    assert "two.txt" in result


def test_create_directory(tmp_path):
    tool = FileTool()
    directory = tmp_path / "new_directory"

    assert tool.execute("mkdir", directory) is True
    assert directory.exists()
    assert directory.is_dir()


def test_invalid_action(tmp_path):
    tool = FileTool()

    assert tool.execute("invalid", tmp_path) is None
