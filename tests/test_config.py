from localpilot.config import Config


def test_app_name():
    assert Config.APP_NAME == "LocalPilot"


def test_debug_mode():
    assert Config.DEBUG is False
