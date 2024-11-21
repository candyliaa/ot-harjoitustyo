import pygame

class Ball:
    def __init__(self, x, y, speed=10, color=(255, 255, 255), size=10):
        self.__initial_x = x
        self.__initial_y = y

        self.position = pygame.math.Vector2(x, y)
        self.direction = pygame.math.Vector2(1, 1)

        self.speed = speed
        self.color = color

        self.size = size

    def update(self, window_size):
        if self.position.x <= 0 - self.size:
            self.reset()
            scored = "own"
        elif self.position.x >= window_size[0] + self.size:
            self.reset()
            scored = "enemy"
        else:
            scored = None

        if self.position.y <= 0 + self.size or self.position.y >= window_size[1] - self.size:
            self.direction.y = -self.direction.y

        self.position += self.speed * self.direction

        return scored

    def draw_ball(self, game_window):
        pygame.draw.circle(game_window, self.color,
                           (self.position.x, self.position.y), self.size)

    def get_ball_rect(self):
        return pygame.Rect(self.position.x - self.size, self.position.y - self.size, self.size * 2, self.size * 2)

    def collision(self, paddle):
        if abs(self.position.y - paddle.get_center().y) < 15:
            self.direction.x *= -1
        else:
            self.direction = (self.position - paddle.get_center()).normalize()

    def reset(self):
        self.position.x = self.__initial_x
        self.position.y = self.__initial_y
        self.direction.x *= -1
