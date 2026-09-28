from PySide6.QtWidgets import QApplication

from .assistant import LocalPilotAssistant
from .command_tool import CommandTool
from .file_tool import FileTool
from .gui import LocalPilotGUI
from .llm import LocalLLM
from .ollama_client import OllamaClient
from .process_tool import ProcessTool
from .tool_manager import ToolManager


def main():
    app = QApplication([])

    ollama = OllamaClient(
        model="llama3.2:3b",
        host="http://localhost:11434",
    )

    llm = LocalLLM(ollama)

    tool_manager = ToolManager()

    tool_manager.register(CommandTool())
    tool_manager.register(FileTool())
    tool_manager.register(ProcessTool())

    tool_manager.registry.permission_manager.set_permission(
        "file",
        "safe",
    )

    tool_manager.registry.permission_manager.set_permission(
        "process",
        "safe",
    )

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
