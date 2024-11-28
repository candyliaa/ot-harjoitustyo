from console import ConsoleIO

class Stats:
    def __init__(self):
        self._io = ConsoleIO

    def execute(self):
        self._io.print("\nStats page")
        # Implement database and fetch stats...

class Settings:
    def __init__(self, config):
        self._io = ConsoleIO
        self.config = config
        self._settings_menu_commands = {
            "1": "1. Change ball speed (default 15)",
            "2": "2. Change ball color",
            "3": "3. Change paddle speed",
            "4": "4. Change paddle color",
            "5": "Change AI difficulty",
            "6": "Save and exit"
        }

    def execute(self):
        self._io.print("\nSettings page")
        self.print.instructions()

        while True:
            command = self._io.read("")

            if not command in self._settings_menu_commands:
                self._io.print("Invalid command!")
                self.print.instructions()
                continue

            if command == "1":
                new_speed = self._io.read("Input new speed value for ball (between 1 and 50): ")
                if new_speed < 1 or new_speed > 50:
                    self._io.print("Speed value too small or too big!")
                    continue

            elif command == "2":
                self._io.print("1. Red\n2. Green\n3. Blue\n4. Yellow\n5. Magenta")
                new_color = self._io.read("Input new color for ball: ")
                if new_color not in ["1", "2", "3", "4", "5"]:
                    self._io.print("Invalid color!")
                    continue

            elif command == "3":
                new_speed = self._io.read("Input new speed value for paddle (between 1 and 50): ")
                if new_speed < 1 or new_speed > 50:
                    self._io.print("Speed value too small or too big!")
                    continue

            elif command == "4":
                self._io.print("1. Red\n2. Green\n3. Blue\n4. Yellow\n5. Magenta")
                new_color = self._io.read("Input new color for paddle: ")
                if new_color not in ["1", "2", "3", "4", "5"]:
                    self._io.print("Invalid color!")
                    continue

            elif command == "5":
                # Implement this...
                pass
            elif command == "6":
                pass

    def instructions(self):
        self._io.print("1. Change ball speed (default 15)\n2. Change ball color\n3. Change paddle speed\n4. Change paddle color\n5. Change AI difficulty\n6. Save and exit")

class PongCLI:
    def __init__(self, config):
        self._io = ConsoleIO
        self.config = config
        self._start_menu_commands = {
            "1": "1. Start game",
            "2": Stats(),
            "3": Settings(config),
            "4": "4. Quit",
        }

    def start(self):
        self.io.print("Welcome to Pong!")
        self.start_menu_instructions()
        
        while True:
            command = self._io.read("")
            if not command in self._start_menu_commands:
                continue

            if command == "1":
                return True
            if command == "4":
                return False

            command_object = self._start_menu_commands[command]
            command_object.execute()

    def start_menu_instructions(self):
        self.io.print("1. Start game\n2. Stats\n3. Settings\n 4. Quit")
