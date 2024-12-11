import unittest
from ui.cli_ui import Settings
from config import Config

class MockIO():
    def __init__(self, inputs):
        self.inputs = inputs
        self.output = []

    def read(self, input_str):
        return self.inputs.pop(0)
    
    def print(self, input_str):
        self.output.append(input_str)


class TestSettings(unittest.TestCase):
    def setUp(self):
        self.config = Config()

    def test_invalid_command_does_not_error(self):
        self.io = MockIO(["55", "7", "4"])
        self.settings = Settings(self.config, self.io)
        self.settings.execute()
        self.assertEqual("\n[red][!] Invalid command![/red]\n", self.io.output[8])

    def test_ball_speed_gets_changed(self):
        self.io = MockIO(["1", "20", "7", "4"])
        self.settings = Settings(self.config, self.io)
        self.settings.execute()
        self.assertEqual(self.config.ball_speed, 20)
    
    def test_too_big_ball_speed_does_not_get_applied(self):
        self.io = MockIO(["1", "100", "7", "4"])
        self.settings = Settings(self.config, self.io)
        self.settings.execute()
        self.assertNotEqual(self.config.ball_speed, 100)

    def test_too_small_ball_speed_does_not_get_applied(self):
        self.io = MockIO(["1", "0", "7", "4"])
        self.settings = Settings(self.config, self.io)
        self.settings.execute()
        self.assertNotEqual(self.config.ball_speed, 0)

    def test_not_number_ball_speed_does_not_break(self):
        self.io = MockIO(["1", "test", "7", "4"])
        self.settings = Settings(self.config, self.io)
        self.settings.execute()
        self.assertNotEqual(self.config.ball_speed, "test")

    def test_ball_color_gets_changed(self):
        config_colors = []
        for i in range(1, 7):
            self.io = MockIO(["2", str(i), "7", "4"])
            self.settings = Settings(self.config, self.io)
            self.settings.execute()
            config_colors.append(self.config.ball_color)
        self.assertEqual(config_colors, [(255, 0, 0), (0, 255, 0), (0, 0, 255), (255, 255, 0), (255, 0, 255), (255, 255, 255)])

    def test_invalid_ball_color_does_not_get_applied(self):
        self.io = MockIO(["2", "10", "7", "4"])
        self.settings = Settings(self.config, self.io)
        self.settings.execute()
        self.assertEqual(self.config.ball_color, (255, 255, 255))

    def test_paddle_speed_gets_changed(self):
        self.io = MockIO(["3", "15", "7", "4"])
        self.settings = Settings(self.config, self.io)
        self.settings.execute()
        self.assertEqual(self.config.paddle_speed, 15)

    def test_too_big_paddle_speed_does_not_get_applied(self):
        self.io = MockIO(["3", "100", "7", "4"])
        self.settings = Settings(self.config, self.io)
        self.settings.execute()
        self.assertNotEqual(self.config.paddle_speed, 100)

    def test_too_small_paddle_speed_does_not_get_applied(self):
        self.io = MockIO(["3", "0", "7", "4"])
        self.settings = Settings(self.config, self.io)
        self.settings.execute()
        self.assertNotEqual(self.config.paddle_speed, 0)

    def test_not_a_number_paddle_speed_does_not_get_applied(self):
        self.io = MockIO(["3", "test", "7", "4"])
        self.settings = Settings(self.config, self.io)
        self.settings.execute()
        self.assertEqual(self.config.paddle_speed, 10)

    def test_paddle_color_gets_changed(self):
        config_colors = []
        for i in range(1, 6):
            self.io = MockIO(["4", str(i), "7", "4"])
            self.settings = Settings(self.config, self.io)
            self.settings.execute()
            config_colors.append(self.config.paddle_color)
        self.assertEqual(config_colors, [(255, 0, 0), (0, 0, 255), (255, 255, 0), (255, 0, 255), (0, 255, 0)])

    def test_invalid_paddle_color_does_not_get_applied(self):
        self.io = MockIO(["4", "test", "7", "4"])
        self.settings = Settings(self.config, self.io)
        self.settings.execute()
        self.assertEqual(self.config.paddle_color, (0, 255, 0))

    def test_ai_difficulty_gets_changed(self):
        config_difficulties = []
        for i in range(1, 5):
            self.io = MockIO(["5", str(i), "7", "4"])
            self.settings = Settings(self.config, self.io)
            self.settings.execute()
            config_difficulties.append(self.config.difficulty)
        self.assertEqual(config_difficulties, [0.4, 0.6, 0.8, 1])

    def test_invalid_difficulty_does_not_get_applied(self):
        self.io = MockIO(["5", "5", "7", "4"])
        self.settings = Settings(self.config, self.io)
        self.settings.execute()
        self.assertEqual(self.config.difficulty, 0.6)

    def test_ball_amount_gets_changed(self):
        config_amounts = []
        for i in range(1, 11):
            self.io = MockIO(["6", str(i), "7", "4"])
            self.settings = Settings(self.config, self.io)
            self.settings.execute()
            config_amounts.append(self.config.ball_amount)
        self.assertEqual(config_amounts, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

    def test_no_zero_balls(self):
        self.io = MockIO(["6", "0", "7", "4"])
        self.settings = Settings(self.config, self.io)
        self.settings.execute()
        self.assertNotEqual(self.config.ball_amount, 0)

    def test_not_too_many_balls(self):
        self.io = MockIO(["6", "100", "7", "4"])
        self.settings = Settings(self.config, self.io)
        self.settings.execute()
        self.assertNotEqual(self.config.ball_amount, 100)
    
    def test_not_a_number_amount_does_not_get_applied(self):
        self.io = MockIO(["6", "test", "7", "4"])
        self.settings = Settings(self.config, self.io)
        self.settings.execute()
        self.assertEqual(self.config.ball_amount, 1)
