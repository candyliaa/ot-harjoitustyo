import unittest
from sprites.paddle import Paddle
from config import Config


class TestPaddle(unittest.TestCase):
    def setUp(self):
        self.config = Config()
        self.start_x = self.config.window_size[0]-100
        self.start_y = self.config.window_size[1]//2
        self.paddle = Paddle((self.start_x, self.start_y,), self.config.paddle_speed, self.config.paddle_color, self.config.paddle_size)

    def test_paddle_in_correct_x_position_at_start(self):
        self.assertEqual(self.start_x, self.paddle.x)

    def test_paddle_in_correct_y_position_at_start(self):
        self.assertEqual(self.start_y, self.paddle.y)

    def test_paddle_moves_correct_amount_on_up_input(self):
        self.paddle.update(self.config.window_size, 1)
        self.assertEqual(self.start_y + self.paddle.speed, self.paddle.y)

    def test_paddle_moves_correct_amount_on_down_input(self):
        self.paddle.update(self.config.window_size, -1)
        self.assertEqual(self.start_y - self.paddle.speed, self.paddle.y)

    def test_paddle_does_not_go_off_screen_up(self):
        self.paddle.y = -5
        self.paddle.update(self.config.window_size, -1)
        self.assertEqual(0, self.paddle.y)

    def test_paddle_does_not_go_off_screen_down(self):
        self.paddle.y = self.config.window_size[1] + 1
        self.paddle.update(self.config.window_size, 1)
        self.assertEqual(self.config.window_size[1] - self.paddle.size, self.paddle.y)
