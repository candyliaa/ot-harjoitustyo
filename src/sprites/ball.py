import pygame

class Ball:
    def __init__(self, window_size, game_window, x, y, speed=1, color=(255, 255, 255), size=10):
        self.x = x
        self.y = y

        self.window_size = window_size
        game_window = game_window

        self.x_dir = 1
        self.y_dir = 1

        self.speed = speed
        self.color = color

        self.size = size

        self.ball = pygame.draw.circle(game_window, self.color, (self.x, self.y), self.size)

    def update(self):

        if self.x <= 0:
            self.x_dir = 1
        elif self.x >= self.window_size[0]:
            self.x_dir = -1

        if self.y <= 0:
            self.y_dir = 1
        if self.y <= self.window_size[1]:
            self.y_dir = -1

        self.x += self.speed * self.x_dir
        self.y += self.speed * self.y_dir

    def display_ball(self):
        return self.ball
    
    def ball_collision(self):
        self.x_dir *= -1
