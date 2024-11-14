import pygame

class Paddle:
    def __init__(self, window_size, game_window, x, y, speed=1, color=(), size=300):
        self.x = x
        self.y = y
        self.size = size

        window_size = window_size
        game_window = game_window

        self.speed = speed
        self.color = color

        self.paddle_rect = pygame.Rect(game_window, self.x, self.y, 50, size)
        self.paddle = pygame.draw.rect(game_window, self.color, self.paddle_rect)

    def update(self, movement=0):
        self.y += self.speed * movement
        if self.y <= 0:
            self.y = 0
        if self.y + self.size >= window_size[1]:
            self.y = window_size[1]
