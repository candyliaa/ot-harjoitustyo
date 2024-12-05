import unittest
from ui.cli_ui import PongCLI
from config import Config
from ui.console import ConsoleIO

class MockIO():
    def __init__(self, inputs):
        self.inputs = inputs

    def read(self, input_str):
        return self.inputs.pop(0)
    
    def print(self, input_str):
        pass
        

class TestPongCLI(unittest.TestCase):
    def setUp(self):
        self.config = Config()
        
    def test_ball_speed_gets_changed(self):
        self.io = MockIO(["3", "1", "20", "6", "4"])
        self.cli = PongCLI(self.config, self.io, None)
        self.cli.start()
        self.assertEqual(self.config.ball_speed, 20)

    def test_ball_color_gets_changed(self):
        self.io = MockIO(["3", "2", "2", "6", "4"])
        self.cli = PongCLI(self.config, self.io, None)
        self.cli.start()
        self.assertEqual(self.config.ball_color, (0, 255, 0))

    def test_paddle_speed_gets_changed(self):
        self.io = MockIO(["3", "3", "15", "6", "4"])
        self.cli = PongCLI(self.config, self.io, None)
        self.cli.start()
        self.assertEqual(self.config.paddle_speed, 15)

    def test_paddle_color_gets_changed(self):
        self.io = MockIO(["3", "4", "1", "6", "4"])
        self.cli = PongCLI(self.config, self.io, None)
        self.cli.start()
        self.assertEqual(self.config.paddle_color, (255, 0, 0))

    def test_ai_difficulty_gets_changed(self):
        self.io = MockIO(["3", "5", "3", "6", "4"])
        self.cli = PongCLI(self.config, self.io, None)
        self.cli.start()
        self.assertEqual(self.config.difficulty, 0.8)

    def test_game_gets_started(self):
        self.io = MockIO(["1"])
        self.cli = PongCLI(self.config, self.io, None)
        self.cli.start()
        self.assertEqual(self.cli.start_game, True)

    def test_game_does_not_get_started(self):
        self.io = MockIO(["4"])
        self.cli = PongCLI(self.config, self.io, None)
        self.cli.start()
        self.assertEqual(self.cli.start_game, False)
