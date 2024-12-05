from ui.console import ConsoleIO
from sprites.colors import color_dict

class Stats:
    def __init__(self, io, stat_repo):
        self._io = io
        self._stat_repo = stat_repo
        self._stats_menu_commands = {
            "1": "1. View score stats",
            "2": "2. View misc. stats",
            "3": "3. Main Menu"
        }

    def execute(self):
        self._io.print("\nStats page")

        while True:
            self.print_instructions()
            command = input("\nInput command: ")

            if command not in self._stats_menu_commands.keys():
                self._io.print("Invalid command!")
                continue

            elif command == "1":
                scores = self._stat_repo.get_scores()
                self._io.print(f"{'Session no.' : <15}{'Own score' : ^10}{'Enemy score' : >15}")
                for score in scores:
                    self._io.print(f"{score[0] : >10}{score[1] : ^20}{score[2] : >10}")

            elif command == "2":
                continue
    
            elif command == "3":
                self._io.print("Returning to main menu...\n")
                break

    def print_instructions(self):
        self._io.print("\n")
        for instruction in self._stats_menu_commands.values():
            self._io.print(instruction)

class Settings:
    def __init__(self, config, io):
        self._io = io
        self.config = config
        self._settings_menu_commands = {
            "1": "1. Change ball speed (default 15)",
            "2": "2. Change ball color",
            "3": "3. Change paddle speed",
            "4": "4. Change paddle color",
            "5": "Change AI difficulty",
            "6": "Save and exit"
        }

    def change_ball_speed(self):
        new_speed = int(self._io.read("\nInput new speed value for ball (between 1 and 50, default 15): "))
        if new_speed < 1 or new_speed > 50:
            self._io.print("Speed value too small or too big!")
            return
        self.config.ball_speed = new_speed
        self.print_successful_change()

    def change_ball_color(self):
        self._io.print("1. Red\n2. Green\n3. Blue\n4. Yellow\n5. Magenta")
        new_color = self._io.read("Input new color for ball: ")
        if new_color not in ["1", "2", "3", "4", "5"]:
            self._io.print("Invalid color!")
            return
        if new_color == "1":
            self.config.ball_color = color_dict["red"]
        elif new_color == "2":
            self.config.ball_color = color_dict["green"]
        elif new_color == "3":
            self.config.ball_color = color_dict["blue"]
        elif new_color == "4":
            self.config.ball_color = color_dict["yellow"]
        elif new_color == "5":
            self.config.ball_color = color_dict["magenta"]
        self.print_successful_change()

    def change_paddle_speed(self):
        new_speed = int(self._io.read("\nInput new speed value for paddle (between 1 and 30, default 10): "))
        if new_speed < 1 or new_speed > 30:
            self._io.print("Speed value too small or too big!")
            return
        self.config.paddle_speed = new_speed
        self.print_successful_change()

    def change_paddle_color(self):
        self._io.print("1. Red\n2. Green\n3. Blue\n4. Yellow\n5. Magenta")
        new_color = self._io.read("\nInput new color for paddles: ")
        if new_color not in ["1", "2", "3", "4", "5"]:
            self._io.print("Invalid color!")
            return
        if new_color == "1":
            self.config.paddle_color = color_dict["red"]
        elif new_color == "2":
            self.config.paddle_color = color_dict["green"]
        elif new_color == "3":
            self.config.paddle_color = color_dict["blue"]
        elif new_color == "4":
            self.config.paddle_color = color_dict["yellow"]
        elif new_color == "5":
            self.config.paddle_color = color_dict["magenta"]

    def change_difficulty(self):
        self._io.print("1. Easy\n2. Medium (default)\n3. Hard\n4. Impossible")
        new_difficulty = self._io.read("\nInput new difficulty: ")
        if new_difficulty not in ["1", "2", "3", "4"]:
            self._io.print("Invalid difficulty!")
            return
        if new_difficulty == "1":
            self.config.difficulty = 0.4
        elif new_difficulty == "2":
            self.config.difficulty = 0.6
        elif new_difficulty == "3":
            self.config.difficulty = 0.8
        elif new_difficulty == "4":
            self.config.difficulty = 1
        self.print_successful_change()

    def execute(self):
        self._io.print("\nSettings page")
        
        while True:
            self.print_instructions()
            command = self._io.read("Input command: ")

            if not command in self._settings_menu_commands:
                self._io.print("Invalid command!")
                continue

            if command == "1":
                self.change_ball_speed()
                
            elif command == "2":
                self.change_ball_color()

            elif command == "3":
                self.change_paddle_speed()

            elif command == "4":
                self.change_paddle_color()

            elif command == "5":
                self.change_difficulty()

            elif command == "6":
                self._io.print("Settings saved!")
                break

    def print_instructions(self):
        self._io.print("\n1. Change ball speed (default 15)\n2. Change ball color\n3. Change paddle speed\n4. Change paddle color\n5. Change AI difficulty\n6. Save and exit")
    
    def print_successful_change(self):
        self._io.print("\nSetting successfully changed!")

class PongCLI:
    def __init__(self, config, io, stats):
        self._io = io
        self.config = config
        self._start_menu_commands = {
            "1": "1. Start game",
            "2": Stats(io, stats),
            "3": Settings(config, io),
            "4": "4. Quit",
        }

    def start(self):
        self._io.print("\nWelcome to Pong!")
        self.start_game = False
        while True:
            self.start_menu_instructions()
            command = str(self._io.read("\nInput command: "))
            if not command in self._start_menu_commands:
                self._io.print("Invalid command!")
                continue

            if command == "1":
                self.start_game = True
                return self.start_game
            if command == "4":
                self.start_game = False
                return self.start_game

            command_object = self._start_menu_commands[command]
            command_object.execute()

    def start_menu_instructions(self):
        self._io.print("\n1. Start game\n2. Stats\n3. Settings\n4. Quit")
