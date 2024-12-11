from rich.table import Table

class Stats:
    """The stats class to handle reading data from the database.
    """
    def __init__(self, io, stat_repo):
        """The constructor for the class which initializes required values.

        Args:
            io: The IO object used to read user inputs.
            stat_repo: The object used to read from the database.
        """
        self._io = io
        self._stat_repo = stat_repo
        self._stats_menu_commands = {
            "1": "[1] View score stats",
            "2": "[2] View misc. stats",
            "3": "[3] Main Menu"
        }

    def execute(self):
        """A loop to print relevant information on the cli to the user.
        """

        while True:
            self.print_instructions()
            command = input("\nInput command: ")

            if command not in self._stats_menu_commands.keys():
                self._io.print("\n[red][!] Invalid command![/red]\n")
                continue

            elif command == "1":
                scoretable = Table(title="Score stats")
                scoretable.add_column("Session no.")
                scoretable.add_column("Own score")
                scoretable.add_column("Enemy score")
                scores = self._stat_repo.get_scores()
                for score in scores:
                    scoretable.add_row(
                        str(score[0]),
                        str(score[1]),
                        str(score[2])
                    )
                scoretable.add_row(
                    "Total",
                    str(sum(score[1] for score in scores)),
                    str(sum(score[2] for score in scores))
                )
                self._io.print("")
                self._io.print(scoretable)

            elif command == "2":
                misctable = Table(title="Misc. stats")
                misctable.add_column("Ball bounces")
                misctable.add_column("Own travel distance")
                misctable.add_column("Enemy travel distance")
                misc_stats = self._stat_repo.get_misc_stats()
                misctable.add_row(
                    str(misc_stats[0][0]),
                    str(misc_stats[0][1]),
                    str(misc_stats[0][2]),
                )
                self._io.print("")
                self._io.print(misctable)
    
            elif command == "3":
                self._io.print("\n[yellow]Returning to main menu...[/yellow]")
                break

    def print_instructions(self):
        self._io.print("\nStats page\n------------")
        for instruction in self._stats_menu_commands.values():
            self._io.print(instruction)
