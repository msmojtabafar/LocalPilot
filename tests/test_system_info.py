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


def test_get_cpu_count():
    info = SystemInfo()

    assert info.get_cpu_count() is not None
    assert info.get_cpu_count() > 0


def test_get_memory():
    info = SystemInfo()

    memory = info.get_memory()

    assert memory is not None
    assert memory > 0
