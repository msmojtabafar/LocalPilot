from localpilot.system_info import SystemInfo


def test_get_os():
    info = SystemInfo()

    assert info.get_os() == "Linux"


def test_get_python_version():
    info = SystemInfo()

    assert info.get_python_version() != ""


def test_get_hostname():
    info = SystemInfo()

    assert info.get_hostname() != ""
