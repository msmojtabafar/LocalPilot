from localpilot.response_formatter import ResponseFormatter


def test_format_string():
    result = ResponseFormatter.format("سلام")

    assert result == "سلام"


def test_format_dict():
    result = ResponseFormatter.format({
        "pid": 1234,
        "name": "test",
    })

    assert "PID: 1234" in result
    assert "نام: test" in result


def test_format_process_list():
    result = ResponseFormatter.format([
        {
            "pid": 1,
            "name": "systemd",
        },
        {
            "pid": 1234,
            "name": "python",
        },
    ])

    assert "پردازش‌های در حال اجرا" in result
    assert "PID       نام پردازش" in result
    assert "1         systemd" in result
    assert "1234      python" in result


def test_format_empty_list():
    result = ResponseFormatter.format([])

    assert result == "موردی پیدا نشد."


def test_format_generic_list():
    result = ResponseFormatter.format([
        "one",
        "two",
        "three",
    ])

    assert "one" in result
    assert "two" in result
    assert "three" in result


def test_format_none():
    result = ResponseFormatter.format(None)

    assert result == ""
