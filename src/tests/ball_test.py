import unittest
from sprites.ball import Ball
from config import window_size, SPEED


class TestBall(unittest.TestCase):
    def setUp(self):
        self.start_x = window_size[0]-100
        self.start_y = window_size[1]//2
        self.ball = Ball((self.start_x, self.start_y))
