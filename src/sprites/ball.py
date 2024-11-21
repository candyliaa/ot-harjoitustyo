import pygame


class Ball:
    def __init__(self, x, y, speed=10, color=(255, 255, 255), size=10):
        self.__initial_x = x
        self.__initial_y = y
        self.x = x
        self.y = y

        self.x_dir = 1
        self.y_dir = 1

        self.speed = speed
        self.color = color

        self.size = size

    def update(self, window_size):
        if self.x <= 0 - self.size:
            self.reset()
            scored = "own"
        elif self.x >= window_size[0] + self.size:
            self.reset()
            scored = "enemy"
        else:
            scored = None

        if self.y <= 0 + self.size:
            self.y_dir = 1
        if self.y >= window_size[1] - self.size:
            self.y_dir = -1

        self.x += self.speed * self.x_dir
        self.y += self.speed * self.y_dir
        
        return scored

    def draw_ball(self, game_window):
        pygame.draw.circle(game_window, self.color,
                           (self.x, self.y), self.size)

    def get_ball_rect(self, game_window):
        return pygame.draw.circle(game_window, self.color,
                           (self.x, self.y), self.size)

    def collision(self):
        self.x_dir *= -1

    def reset(self):
        self.x = self.__initial_x
        self.y = self.__initial_y
        self.x_dir *= -1
