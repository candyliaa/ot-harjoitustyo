from sprites.colors import color_dict

class Settings:
    """The settings class to handle reading data from the database.
    """
    def __init__(self, config, io):
        """The constructor for the class that initializes required values.

        Args:
            config: The config object that the current config is read from and potentially changed.
            io: The IO object to read user inputs.
        """
        self._io = io
        self._config = config
        difficulty = {
            0.4: "[green]Easy[/green]",
            0.6: "[yellow]Medium[/yellow]",
            0.8: "[orange]Hard[/orange]",
            1: "[red]Impossible[/red]"
        }[self._config.difficulty]

        self._settings_menu_commands = {
            "1": f"[1] Change ball speed (current: {self._config.ball_speed})",
            "2": f"[2] Change ball color (current: {self.look_up_color(color_dict, self._config.ball_color)})",
            "3": f"[3] Change paddle speed (current: {self._config.paddle_speed})",
            "4": f"[4] Change paddle color (current: {self.look_up_color(color_dict, self._config.paddle_color)})",
            "5": f"[5] Change AI difficulty (current: {difficulty})",
            "6": f"[6] Change amount of balls (current: {self._config.ball_amount})",
            "7": "[7] Save and exit"
        }

    def look_up_color(self, color_dict, color):
        for (k, v) in color_dict.items():
            if v == tuple(color): return f"[{k}]{k.title()}[/{k}]"
        return None

    def change_ball_speed(self):
        """A method to update the config object's ball_speed attribute according to user input.
        """
        try:
            new_speed = int(self._io.read("\nInput new speed value for ball (between 1 and 50, default 15): "))
        except:
            self._io.print("\n[red][!] Input is not a number! Returning to settings menu...[/red]\n")
            return
        if new_speed < 1 or new_speed > 50:
            self._io.print("\n[red][!] Speed value too small or too big![/red]\n")
            return
        self._config.ball_speed = new_speed
        self.print_successful_change()

    def change_ball_color(self):
        """A method to update config object's ball_color attribute according to user input.
        """
        self._io.print("[1] [red]Red[/red]\n[2] [green]Green[/green]\n[3] [blue]Blue[/blue]\n[4] [yellow]Yellow[/yellow]\n[5] [purple]Magenta[/purple]\n[6] [white]White[/white] (default)")
        new_color = self._io.read("\nInput new color for ball: ")
        if new_color not in ["1", "2", "3", "4", "5", "6"]:
            self._io.print("\n[red][!] Invalid color![/red]\n")
            return
        if new_color == "1":
            self._config.ball_color = color_dict["red"]
        elif new_color == "2":
            self._config.ball_color = color_dict["green"]
        elif new_color == "3":
            self._config.ball_color = color_dict["blue"]
        elif new_color == "4":
            self._config.ball_color = color_dict["yellow"]
        elif new_color == "5":
            self._config.ball_color = color_dict["magenta"]
        elif new_color == "6":
            self._config.ball_color = color_dict["white"]
        self.print_successful_change()

    def change_paddle_speed(self):
        """A method to update config object's paddle_speed attribute according to user input.
        """
        try:
            new_speed = int(self._io.read("\nInput new speed value for paddle (between 1 and 30, default 10): "))
        except:
            self._io.print("\n[red][!] Input is not a number! Returning to settings menu...[/red]\n")
            return
        if new_speed < 1 or new_speed > 30:
            self._io.print("\n[red][!] Speed value too small or too big![/red]\n")
            return
        self._config.paddle_speed = new_speed
        self.print_successful_change()

    def change_paddle_color(self):
        """A method to update config object's paddle_color attribute according to user input.
        """
        self._io.print("[1] [red]Red[/red]\n[2] [blue]Blue[/blue]\n[3] [yellow]Yellow[/yellow]\n[4] [purple]Magenta[/purple]\n[5] [green]Green[/green] (default)")
        new_color = self._io.read("\nInput new color for paddles: ")
        if new_color not in ["1", "2", "3", "4", "5"]:
            self._io.print("\n[red][!] Invalid color![/red]\n")
            return
        if new_color == "1":
            self._config.paddle_color = color_dict["red"]
        elif new_color == "2":
            self._config.paddle_color = color_dict["blue"]
        elif new_color == "3":
            self._config.paddle_color = color_dict["yellow"]
        elif new_color == "4":
            self._config.paddle_color = color_dict["magenta"]
        elif new_color == "5":
            self._config.paddle_color = color_dict["green"]

    def change_difficulty(self):
        """A method to update config object's difficulty attribute according to user input.
        """
        self._io.print("[1] [green]Easy[/green]\n[2] [yellow]Medium[/yellow] (default)\n[3] [orange]Hard[/orange]\n[4] [red]Impossible[/red]")
        new_difficulty = self._io.read("\nInput new difficulty: ")
        if new_difficulty not in ["1", "2", "3", "4"]:
            self._io.print("\n[red][!] Invalid difficulty![/red]\n")
            return
        if new_difficulty == "1":
            self._config.difficulty = 0.4
        elif new_difficulty == "2":
            self._config.difficulty = 0.6
        elif new_difficulty == "3":
            self._config.difficulty = 0.8
        elif new_difficulty == "4":
            self._config.difficulty = 1
        self.print_successful_change()

    def change_ball_amount(self):
        """A method to update config object's ball_amount attribute according to user input.
        """
        try:
            new_amount = int(self._io.read("\nInput amount of balls: (1 to 10)\n"))
        except:
            self._io.print("\n[red][!] Input is not a number! Returning to settings menu...[/red]\n")
            return
        if new_amount not in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]:
            self._io.print("\n[red][!] Invalid amount![/red]\n")
            return
        self._config.ball_amount = new_amount
        self.print_successful_change()

    def execute(self):
        """A loop to interact on the cli with the user.
        """
        
        while True:
            self.print_instructions()
            command = self._io.read("\nInput command: ")

            if not command in self._settings_menu_commands:
                self._io.print("\n[red][!] Invalid command![/red]\n")
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
                self.change_ball_amount()

            elif command == "7":
                self._io.print("\n[green]Settings saved![/green]")
                self._io.print("[yellow]Returning to main menu...[/yellow]")
                break

    def print_instructions(self):
        self._io.print("\nSettings page\n---------------")
        for instruction in self._settings_menu_commands.values():
            self._io.print(instruction)
    
    def print_successful_change(self):
        self._io.print("\n[green]Setting successfully changed![/green]\n[yellow][\] Change is seen on the CLI upon restart![/yellow]\n")
