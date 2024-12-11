import pygame


class Paddle:
    """Paddle object for the pong game."""
    def __init__(self, pos, speed, color, size):
        """The constructor for the class which initializes required values.

        Args:
            pos: Position of the paddle.
            speed: Speed of the paddle.
            color: Color of the paddle.
            size: Size of the paddle.
        """
        self.x = pos[0]
        self.y = pos[1]
        self.size = size
        self.speed = speed
        self._color = color
        self._width = 40
        self.traveled = 0

    def update(self, window_size, movement=0):
        """Method to update the paddle's y-position.

        Args:
            window_size: The size of the game window.
            movement: An integer that tells the method which direction the paddle should move in.
        """
        self.y += self.speed * movement
        self.traveled += abs(self.speed * movement)
        self.y = max(self.y, 0)
        if self.y + self.size >= window_size[1]:
            self.y = window_size[1] - self.size

    def display_paddle(self, game_window):
        """Method to draw a paddle on the game window.

        Args:
            game_window: The pygame game window.
        """
        paddle_rect = self.get_paddle_rect()
        pygame.draw.rect(game_window, self._color, paddle_rect)

    def get_paddle_rect(self):
        """Method to return a rectangle representing the paddle.

        Returns:
            A pygame.Rect object which represents the paddle's hitbox.
        """
        return pygame.Rect(self.x, self.y, self._width, self.size)

    def get_center(self):
        """Method to return the center point of the paddle.

        Returns:
            A pygame.math.Vector2 object which represents the middle point of the paddle.
        """
        return pygame.math.Vector2(self.x + self._width // 2, self.y + self.size // 2)
