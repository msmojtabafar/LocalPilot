class CLI:
    def __init__(self):
        self.running = True

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
                self.handle_command(command)
            except (EOFError, KeyboardInterrupt):
                print()
                self.running = False
                print("Goodbye!")

    def handle_command(self, command):
        if command == "help":
            self.show_help()
        elif command == "status":
            print("LocalPilot is running.")
        elif command == "exit":
            self.running = False
            print("Goodbye!")
        elif command:
            print(f"Unknown command: {command}")
            print("Type 'help' for available commands.")

    def show_help(self):
        print("Available commands:")
        print("  help")
        print("  status")
        print("  exit")
