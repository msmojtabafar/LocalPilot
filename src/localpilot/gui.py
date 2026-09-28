from PySide6.QtCore import Qt, QThread, Signal
from PySide6.QtGui import QFont
from PySide6.QtWidgets import (
    QApplication,
    QHBoxLayout,
    QLabel,
    QLineEdit,
    QMainWindow,
    QPushButton,
    QScrollArea,
    QSizePolicy,
    QVBoxLayout,
    QWidget,
)


class AIWorker(QThread):
    finished = Signal(object)

    def __init__(self, assistant, message):
        super().__init__()
        self.assistant = assistant
        self.message = message

    def run(self):
        try:
            response = self.assistant.respond(self.message)
        except Exception as error:
            response = f"خطا: {error}"

        self.finished.emit(response)


class MessageWidget(QWidget):
    def __init__(self, role, message):
        super().__init__()

        layout = QVBoxLayout(self)
        layout.setContentsMargins(0, 4, 0, 4)

        label = QLabel(str(message))
        label.setWordWrap(True)
        label.setTextInteractionFlags(
            Qt.TextSelectableByMouse
        )
        label.setFont(QFont("DejaVu Sans", 11))
        label.setSizePolicy(
            QSizePolicy.Expanding,
            QSizePolicy.Minimum,
        )

        if role == "user":
            label.setAlignment(
                Qt.AlignRight | Qt.AlignVCenter
            )

            label.setStyleSheet("""
                QLabel {
                    background: #2b6de0;
                    color: white;
                    border-radius: 14px;
                    padding: 12px 16px;
                }
            """)

        else:
            label.setAlignment(
                Qt.AlignLeft | Qt.AlignVCenter
            )

            label.setStyleSheet("""
                QLabel {
                    background: #2a2d32;
                    color: #f1f1f1;
                    border-radius: 14px;
                    padding: 12px 16px;
                }
            """)

        layout.addWidget(label)


class LocalPilotGUI(QMainWindow):
    def __init__(self, assistant=None):
        super().__init__()

        self.assistant = assistant
        self.worker = None
        self.waiting = False

        self.setWindowTitle("LocalPilot")
        self.resize(1000, 700)

        self._build_ui()

    def _build_ui(self):
        central = QWidget()
        self.setCentralWidget(central)

        main_layout = QVBoxLayout(central)
        main_layout.setContentsMargins(0, 0, 0, 0)
        main_layout.setSpacing(0)

        # Header
        header = QLabel("LocalPilot")
        header.setFont(
            QFont("DejaVu Sans", 18, QFont.Bold)
        )
        header.setAlignment(Qt.AlignCenter)
        header.setFixedHeight(70)

        header.setStyleSheet("""
            QLabel {
                background: #181a1f;
                color: white;
                padding: 10px;
            }
        """)

        main_layout.addWidget(header)

        # Chat area
        self.scroll = QScrollArea()
        self.scroll.setWidgetResizable(True)
        self.scroll.setFrameShape(QScrollArea.NoFrame)

        self.messages = QWidget()

        self.messages_layout = QVBoxLayout(
            self.messages
        )

        self.messages_layout.setContentsMargins(
            25, 20, 25, 20
        )

        self.messages_layout.setSpacing(8)
        self.messages_layout.addStretch()

        self.scroll.setWidget(self.messages)

        main_layout.addWidget(self.scroll)

        # Bottom
        bottom = QWidget()

        bottom_layout = QHBoxLayout(bottom)
        bottom_layout.setContentsMargins(
            20, 15, 20, 15
        )

        self.input = QLineEdit()
        self.input.setPlaceholderText(
            "پیام خود را بنویسید..."
        )

        self.input.setFont(
            QFont("DejaVu Sans", 12)
        )

        self.input.setLayoutDirection(
            Qt.RightToLeft
        )

        self.input.returnPressed.connect(
            self._send
        )

        self.input.setStyleSheet("""
            QLineEdit {
                background: #25282e;
                color: white;
                border: 1px solid #444850;
                border-radius: 12px;
                padding: 12px 15px;
            }

            QLineEdit:focus {
                border: 1px solid #2b6de0;
            }

            QLineEdit:disabled {
                background: #1d1f23;
                color: #777;
            }
        """)

        self.send_button = QPushButton("ارسال")

        self.send_button.setFont(
            QFont("DejaVu Sans", 11)
        )

        self.send_button.setFixedWidth(100)

        self.send_button.clicked.connect(
            self._send
        )

        self.send_button.setStyleSheet("""
            QPushButton {
                background: #2b6de0;
                color: white;
                border: none;
                border-radius: 12px;
                padding: 12px;
            }

            QPushButton:hover {
                background: #3b7df0;
            }

            QPushButton:pressed {
                background: #1f5bc0;
            }

            QPushButton:disabled {
                background: #444850;
                color: #888;
            }
        """)

        bottom_layout.addWidget(self.input)
        bottom_layout.addWidget(self.send_button)

        main_layout.addWidget(bottom)

    def _add_message(self, role, message):
        widget = MessageWidget(
            role,
            message,
        )

        self.messages_layout.insertWidget(
            self.messages_layout.count() - 1,
            widget,
        )

        self.scroll_to_bottom()

    def scroll_to_bottom(self):
        scrollbar = self.scroll.verticalScrollBar()

        scrollbar.setValue(
            scrollbar.maximum()
        )

    def _send(self):
        if self.waiting:
            return

        message = self.input.text().strip()

        if not message:
            return

        self.input.clear()

        self._add_message(
            "user",
            message,
        )

        self.waiting = True

        self.input.setDisabled(True)
        self.send_button.setDisabled(True)

        self._add_message(
            "assistant",
            "در حال پردازش...",
        )

        if self.assistant is None:
            self._finish_response(
                "LocalPilot آماده است."
            )
            return

        self.worker = AIWorker(
            self.assistant,
            message,
        )

        self.worker.finished.connect(
            self._finish_response
        )

        self.worker.start()

    def _finish_response(self, response):
        self.waiting = False

        self.input.setDisabled(False)
        self.send_button.setDisabled(False)

        self._remove_last_message()

        self._add_message(
            "assistant",
            self._format_response(response),
        )

        self.input.setFocus()

        if self.worker is not None:
            self.worker.deleteLater()
            self.worker = None

    def _remove_last_message(self):
        if self.messages_layout.count() <= 1:
            return

        item = self.messages_layout.itemAt(
            self.messages_layout.count() - 2
        )

        if item is None:
            return

        widget = item.widget()

        if widget is not None:
            widget.deleteLater()

        self.messages_layout.removeItem(item)

    def _format_response(self, response):
        if isinstance(response, dict):
            lines = []

            for key, value in response.items():
                lines.append(
                    f"{key}: {value}"
                )

            return "\n".join(lines)

        return str(response)

    def closeEvent(self, event):
        if self.worker is not None:
            self.worker.quit()
            self.worker.wait(1000)

        event.accept()


def run_gui(assistant=None):
    app = QApplication.instance()

    if app is None:
        app = QApplication([])

    app.setStyleSheet("""
        QMainWindow {
            background: #111318;
        }

        QScrollArea {
            background: #111318;
        }

        QWidget {
            background: #111318;
        }
    """)

    window = LocalPilotGUI(assistant)
    window.show()

    return app.exec()
