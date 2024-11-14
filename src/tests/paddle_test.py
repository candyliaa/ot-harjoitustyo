import unittest
from sprites.paddle import Paddle
from config import window_size, game_window, speed

class TestPaddle(unittest.TestCase):
    def setUp(self):
        self.start_x = window_size[0]-100
        self.start_y = window_size[1]//2
        self.paddle = Paddle(window_size, game_window, self.start_x, self.start_y, speed=speed, color=(0, 255, 0))

    def test_paddle_in_correct_x_position_at_start(self):
        self.assertEqual(self.start_x, self.paddle.x)
    
    def test_paddle_in_correct_y_position_at_start(self):
        self.assertEqual(self.start_y, self.paddle.y)

    def test_paddle_moves_correct_amount_on_up_input(self):
        self.paddle.update(1)
        self.assertEqual(self.start_y + 5, self.paddle.y)

    def test_paddle_moves_correct_amount_on_down_input(self):
        self.paddle.update(-1)
        self.assertEqual(self.start_y - 5, self.paddle.y)

    def test_paddle_does_not_go_off_screen_up(self):
        self.paddle.y = -5
        self.paddle.update(-1)
        self.assertEqual(0, self.paddle.y)

    def test_paddle_does_not_go_off_screen_down(self):
        self.paddle.y = window_size[1] + 1
        self.paddle.update(1)
        self.assertEqual(window_size[1] - self.paddle.size, self.paddle.y)
