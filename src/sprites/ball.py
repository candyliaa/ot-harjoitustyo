import pygame


class Ball:
    def __init__(self, x, y, speed=20, color=(255, 255, 255), size=10):
        self.x = x
        self.y = y

        self.x_dir = 1
        self.y_dir = 1

        self.speed = speed
        self.color = color

        self.size = size

    def update(self, window_size):
        if self.x <= 0 + 10:
            self.x_dir = 1
        elif self.x >= window_size[0] - 10:
            self.x_dir = -1

        if self.y <= 0 + 10:
            self.y_dir = 1
        if self.y >= window_size[1] - 10:
            self.y_dir = -1

        self.x += self.speed * self.x_dir
        self.y += self.speed * self.y_dir

    def draw_ball(self, game_window):
        pygame.draw.circle(game_window, self.color,
                           (self.x, self.y), self.size)

    def get_ball_rect(self, game_window):
        return pygame.draw.circle(game_window, self.color,
                           (self.x, self.y), self.size)

    def collision(self):
        self.x_dir *= -1
