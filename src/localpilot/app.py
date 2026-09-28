from PySide6.QtWidgets import QApplication

from .assistant import LocalPilotAssistant
from .gui import LocalPilotGUI
from .llm import LocalLLM
from .ollama_client import OllamaClient
from .tool_manager import ToolManager


def main():
    app = QApplication([])

    ollama = OllamaClient(
        model="llama3.2:3b",
        host="http://localhost:11434",
    )

    llm = LocalLLM(ollama)

    tool_manager = ToolManager()

    assistant = LocalPilotAssistant(
        llm=llm,
        tool_manager=tool_manager,
    )

    window = LocalPilotGUI(
        assistant=assistant,
    )

    window.show()

    app.exec()


if __name__ == "__main__":
    main()
