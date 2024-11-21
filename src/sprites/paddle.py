import pygame


class Paddle:
    def __init__(self, x, y, speed=10, color=(), size=300):
        self.x = x
        self.y = y
        self.size = size
        self.speed = speed
        self.color = color
        self.width = 40

    def update(self, window_size, movement=0):
        self.y += self.speed * movement
        if self.y <= 0:
            self.y = 0
        if self.y + self.size >= window_size[1]:
            self.y = window_size[1] - self.size

    def display_paddle(self, game_window):
        paddle_rect = self.get_paddle_rect()
        pygame.draw.rect(game_window, self.color, paddle_rect)

    def get_paddle_rect(self):
        return pygame.Rect(self.x, self.y, self.width, self.size)
    
    def get_center(self):
        return pygame.math.Vector2(self.x + self.width // 2, self.y + self.size // 2)
