import pygame

class Paddle:
    def __init__(self, window_size, game_window, x, y, speed=5, color=(), size=300):
        self.x = x
        self.y = y
        self.size = size

        self.window_size = window_size
        self.game_window = game_window

        self.speed = speed
        self.color = color

    def update(self, movement=0):
        self.y += self.speed * movement
        if self.y <= 0:
            self.y = 0
        if self.y + self.size >= self.window_size[1]:
            self.y = self.window_size[1]
    
    def display_paddle(self):
        paddle_rect = pygame.Rect(self.x, self.y, 40, self.size)
        pygame.draw.rect(self.game_window, self.color, paddle_rect)
