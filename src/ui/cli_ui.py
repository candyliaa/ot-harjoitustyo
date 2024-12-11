from ui.settings import Settings
from ui.stats import Stats

class PongCLI:
    """The class that displays main menu options upon launching the app.
    """
    def __init__(self, config, io, stats):
        """The constructor of the class that initializes required values.

        Args:
            config: The config object that is passed to the settings object.
            io: The IO object used to read inputs from the user.
            stats: The stats repository object used to read from and write to the database.
        """
        self._io = io
        self._config = config
        self._start_menu_commands = {
            "1": "[1] Start game",
            "2": Stats(io, stats),
            "3": Settings(config, io),
            "4": "[4] Quit",
        }

    def start(self):
        """A loop to interact on the cli with the user.

        Returns:
            A bool according to which the app starts the game or quits out.
        """
        self._io.print("\n[italic]Welcome to Pong![/italic]")
        self.start_game = False
        while True:
            self.start_menu_instructions()
            command = str(self._io.read("\nInput command: "))
            if not command in self._start_menu_commands:
                self._io.print("\n[red][!] Invalid command![/red]\n")
                continue
            if command == "1":
                self.start_game = True
                return self.start_game
            if command == "4":
                self.start_game = False
                self._io.print("[italic]See you next time![/italic]")
                return self.start_game

            command_object = self._start_menu_commands[command]
            command_object.execute()

    def start_menu_instructions(self):
        self._io.print("\nMain Menu\n-----------\n[1] Start game\n[2] Stats\n[3] Settings\n[4] Quit")
