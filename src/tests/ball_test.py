import unittest
import pygame
from sprites.ball import Ball
from config import window_size, SPEED


class TestBall(unittest.TestCase):
    def setUp(self):
        self.start_x = window_size[0]//2
        self.start_y = window_size[1]//2
        self.ball = Ball((self.start_x, self.start_y))

    def test_ball_in_correct_position_at_start(self):
        self.assertEqual(self.ball.position, pygame.math.Vector2(window_size[0]//2, window_size[1]//2))

    def test_ball_resets_when_leaves_right(self):
        self.ball.position.x = window_size[0] + 2 * self.ball.size
        self.ball.update(window_size)
        self.assertEqual(self.ball.position, pygame.math.Vector2(window_size[0]//2 - self.ball.speed, window_size[1]//2 + self.ball.speed))

    def test_ball_resets_when_leaves_left(self):
        self.ball.position.x = -self.ball.size
        self.ball.update(window_size)
        self.assertEqual(self.ball.position, pygame.math.Vector2(window_size[0]//2 - self.ball.speed, window_size[1]//2 + self.ball.speed))

    def test_ball_bounces_from_ceiling(self):
        self.ball.position.y = 0
        self.ball.update(window_size)
        self.assertNotEqual(self.ball.position, pygame.math.Vector2(self.ball.position.x, 0))

    def test_ball_bounces_from_floor(self):
        self.ball.position.y = window_size[1] - self.ball.size
        self.ball.update(window_size)
        self.assertNotEqual(self.ball.position, pygame.math.Vector2(self.ball.position.x, window_size[1] - self.ball.size))
