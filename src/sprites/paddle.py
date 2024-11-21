import pygame


class Paddle:
    def __init__(self, x, y, speed=10, color=(), size=300):
        self.x = x
        self.y = y
        self.size = size
        self.speed = speed
        self.color = color

    def update(self, window_size, movement=0):
        self.y += self.speed * movement
        if self.y <= 0:
            self.y = 0
        if self.y + self.size >= window_size[1]:
            self.y = window_size[1] - self.size

    def display_paddle(self, game_window):
        paddle_rect = pygame.Rect(self.x, self.y, 40, self.size)
        pygame.draw.rect(game_window, self.color, paddle_rect)
