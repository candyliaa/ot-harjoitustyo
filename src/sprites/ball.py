import pygame

class Ball:
    """Ball object for the pong game."""
    def __init__(self, pos, speed=15, color=(255, 255, 255), size=10):
        self.__initial_x = pos[0]
        self.__initial_y = pos[1]

        self.position = pygame.math.Vector2(pos[0], pos[1])
        self.direction = pygame.math.Vector2(1, 1)

        self.speed = speed
        self.color = color

        self.size = size

    def update(self, window_size):
        """Ball movement logic without player intervention."""
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
        """Draw the ball object in the pygame game window."""
        pygame.draw.circle(game_window, self.color,
                           (self.position.x, self.position.y), self.size)

    def get_ball_rect(self):
        """Return the rectangle for the ball which is used for collision detection."""
        return pygame.Rect(
            self.position.x - self.size, self.position.y - self.size, self.size * 2, self.size * 2
            )

    def collision(self, paddle):
        """Collision logic for a ball hitting a paddle."""
        self.direction.x *= -1
        self.direction += 0.6 * (self.position - paddle.get_center()).normalize()
        self.direction = self.direction.normalize()

    def reset(self):
        """Reset the position of the ball after scoring."""
        self.position.x = self.__initial_x
        self.position.y = self.__initial_y
        self.direction.x *= -1
