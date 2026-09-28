from .command_executor import CommandExecutor
from .command_registry import CommandRegistry


class CLI:
    def __init__(self):
        self.running = True
        self.registry = CommandRegistry()
        self.executor = CommandExecutor(self.registry)

        self._register_commands()

    def _register_commands(self):
        self.registry.register("help", self.show_help)
        self.registry.register("status", self.show_status)
        self.registry.register("exit", self.exit)

    def run(self):
        print("LocalPilot")
        print("Local AI Assistant")
        print()
        print("Type 'help' for available commands.")
        print("Type 'exit' to quit.")
        print()

        while self.running:
            try:
                command = input("> ").strip().lower()

                if command:
                    result = self.executor.execute(command)

                    if result is None:
                        print(f"Unknown command: {command}")
                        print("Type 'help' for available commands.")

            except (EOFError, KeyboardInterrupt):
                print()
                self.exit()

    def handle_command(self, command):
        result = self.executor.execute(command)

        if result is None:
            print(f"Unknown command: {command}")
            print("Type 'help' for available commands.")
            
    def show_help(self):
        print("Available commands:")
        for command in self.registry.commands():
            print(f"  {command}")

    def show_status(self):
        print("LocalPilot is running.")

    def exit(self):
        self.running = False
        print("Goodbye!")
