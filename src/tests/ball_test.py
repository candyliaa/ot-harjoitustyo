import unittest
import pygame
import random
from sprites.ball import Ball
from config import Config



class TestBall(unittest.TestCase):
    def setUp(self):
        random.seed(1)
        self.config = Config()
        self.start_x = self.config.window_size[0]//2
        self.start_y = self.config.window_size[1]//2
        self.ball = Ball((self.start_x, self.start_y), self.config.ball_speed, self.config.ball_color, self.config.ball_size)

    def test_ball_in_correct_position_at_start(self):
        self.assertEqual(self.ball.position, pygame.math.Vector2(self.config.window_size[0]//2, self.config.window_size[1]//2))

    def test_ball_resets_when_leaves_right(self):
        self.ball.position.x = self.config.window_size[0] + 5 * self.ball.size
        self.ball.update(self.config.window_size)
        self.assertEqual(self.ball.position[0], self.config.window_size[0]//2)

    def test_ball_resets_when_leaves_left(self):
        self.ball.position.x = -self.ball.size
        self.ball.update(self.config.window_size)
        self.assertEqual(self.ball.position[0], self.config.window_size[0]//2)

    def test_ball_bounces_from_ceiling(self):
        self.ball.position.y = 0
        self.ball.update(self.config.window_size)
        self.assertNotEqual(self.ball.position, pygame.math.Vector2(self.ball.position.x, 0))

    def test_ball_bounces_from_floor(self):
        self.ball.position.y = self.config.window_size[1] - self.ball.size
        self.ball.update(self.config.window_size)
        self.assertNotEqual(self.ball.position, pygame.math.Vector2(self.ball.position.x, self.config.window_size[1] - self.ball.size))
