from localpilot.permission_manager import PermissionManager


def test_default_permission_is_dangerous():
    manager = PermissionManager()

    assert manager.get_permission("command") == PermissionManager.DANGEROUS


def test_set_safe_permission():
    manager = PermissionManager()

    assert manager.set_permission(
        "file",
        PermissionManager.SAFE,
    )

    assert manager.get_permission("file") == PermissionManager.SAFE


def test_set_dangerous_permission():
    manager = PermissionManager()

    assert manager.set_permission(
        "process",
        PermissionManager.DANGEROUS,
    )

    assert manager.get_permission("process") == PermissionManager.DANGEROUS


def test_invalid_permission():
    manager = PermissionManager()

    assert not manager.set_permission("file", "invalid")


def test_safe_tool_is_allowed():
    manager = PermissionManager()
    manager.set_permission("file", PermissionManager.SAFE)

    assert manager.is_allowed("file")


def test_dangerous_tool_requires_confirmation():
    manager = PermissionManager()
    manager.set_permission("command", PermissionManager.DANGEROUS)

    assert not manager.is_allowed("command")
    assert manager.is_allowed("command", confirmed=True)
