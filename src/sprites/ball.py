import pygame

class Ball:
    """Ball object for the pong game."""
    def __init__(self, pos, speed, color, size):
        """Constructor for the class that initializes required values.

        Args:
            pos: The position of the ball.
            speed: The speed of the ball.
            color: The color of the ball.
            size: The size of the ball.
        """
        self.__initial_x = pos[0]
        self.__initial_y = pos[1]

        self.position = pygame.math.Vector2(pos[0], pos[1])
        self.direction = pygame.math.Vector2(1, 1)

        self.speed = speed
        self.color = color

        self.size = size

    def update(self, window_size):
        """Updates the ball according to its movement physics.

        Args:
            window_size: The size of the game window.

        Returns:
            A string or None to signify what happened to the ball.
        """
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
            scored = "bounce"

        self.position += self.speed * self.direction

        return scored

    def draw_ball(self, game_window):
        """Method to draw the ball on the game window.

        Args:
            game_window: The pygame game window.
        """
        pygame.draw.circle(game_window, self.color,
                           (self.position.x, self.position.y), self.size)

    def get_ball_rect(self):
        """Method to return a rectangle of the ball used for collision detection.

        Returns:
            A pygame.Rect object that represents the ball's hitbox.
        """
        return pygame.Rect(
            self.position.x - self.size, self.position.y - self.size, self.size * 2, self.size * 2
            )

    def collision(self, paddle):
        """Method to detect collision of the ball and any paddle.

        Args:
            paddle: A paddle in the pong game.
        """
        self.direction.x *= -1
        self.direction += 0.6 * (self.position - paddle.get_center()).normalize()
        self.direction = self.direction.normalize()

    def reset(self):
        """Method to reset the ball's position after either player scores.
        """
        self.position.x = self.__initial_x
        self.position.y = self.__initial_y
        self.direction.x *= -1
