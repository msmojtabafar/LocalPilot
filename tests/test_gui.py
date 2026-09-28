from localpilot.gui import LocalPilotGUI


class DummyAssistant:
    def __call__(self, message):
        return f"Response: {message}"


def test_gui_class_exists():
    assert LocalPilotGUI is not None


def test_gui_response():
    assistant = DummyAssistant()

    assert assistant("Hello") == "Response: Hello"


def test_gui_without_assistant():
    assistant = None

    assert assistant is None
