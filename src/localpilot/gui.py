import tkinter as tk
from tkinter import scrolledtext


class LocalPilotGUI:
    def __init__(self, assistant=None):
        self.assistant = assistant

        self.root = tk.Tk()
        self.root.title("LocalPilot")
        self.root.geometry("900x600")

        self._build_ui()

    def _build_ui(self):
        self.chat = scrolledtext.ScrolledText(
            self.root,
            wrap=tk.WORD,
            state="disabled",
        )
        self.chat.pack(
            fill=tk.BOTH,
            expand=True,
            padx=10,
            pady=10,
        )

        bottom = tk.Frame(self.root)
        bottom.pack(fill=tk.X, padx=10, pady=(0, 10))

        self.input = tk.Entry(bottom)
        self.input.pack(side=tk.LEFT, fill=tk.X, expand=True)
        self.input.bind("<Return>", self._send)

        self.send_button = tk.Button(
            bottom,
            text="Send",
            command=self._send,
        )
        self.send_button.pack(side=tk.RIGHT, padx=(10, 0))

    def _add_message(self, role, message):
        self.chat.configure(state="normal")
        self.chat.insert(
            tk.END,
            f"{role}: {message}\n\n",
        )
        self.chat.configure(state="disabled")
        self.chat.see(tk.END)

    def _send(self, event=None):
        message = self.input.get().strip()

        if not message:
            return

        self.input.delete(0, tk.END)
        self._add_message("You", message)

        response = self._get_response(message)

        if response is not None:
            self._add_message("LocalPilot", response)

    def _get_response(self, message):
        if self.assistant is None:
            return "LocalPilot is ready."

        try:
            return self.assistant(message)
        except Exception:
            return "An error occurred while processing your request."

    def run(self):
        self.root.mainloop()
