from rich import print

class ConsoleIO:
    def __init__(self):
        pass

    def read(self, input_str):
        return input(input_str)

    def print(self, input_str):
        print(input_str)
