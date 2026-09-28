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
        self.registry.register("echo", self.echo)

    def run(self):
        print("LocalPilot")
        print("Local AI Assistant")
        print()
        print("Type 'help' for available commands.")
        print("Type 'exit' to quit.")
        print()

        while self.running:
            try:
                command = input("> ").strip()

                if command:
                    self.handle_command(command)

            except (EOFError, KeyboardInterrupt):
                print()
                self.exit()

    def handle_command(self, command):
        parts = command.split()
        name = parts[0].lower()
        args = parts[1:]

        result = self.executor.execute(name, args)

        if result is None and self.registry.get(name) is None:
            print(f"Unknown command: {name}")
            print("Type 'help' for available commands.")

    def show_help(self):
        print("Available commands:")
        for command in self.registry.commands():
            print(f"  {command}")

    def show_status(self):
        print("LocalPilot is running.")

    def echo(self, *args):
        print(" ".join(args))

    def exit(self):
        self.running = False
        print("Goodbye!")
