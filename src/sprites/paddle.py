import pygame


class Paddle:
    """Paddle object for the pong game."""
    def __init__(self, pos, speed, color, size):
        self.x = pos[0]
        self.y = pos[1]
        self.size = size
        self.speed = speed
        self.color = color
        self.width = 40
        self.traveled = 0

    def update(self, window_size, movement=0):
        """Logic for moving a paddle."""
        self.y += self.speed * movement
        self.traveled += abs(self.speed * movement)
        self.y = max(self.y, 0)
        if self.y + self.size >= window_size[1]:
            self.y = window_size[1] - self.size

    def display_paddle(self, game_window):
        """Draw paddle on the game window."""
        paddle_rect = self.get_paddle_rect()
        pygame.draw.rect(game_window, self.color, paddle_rect)

    def get_paddle_rect(self):
        """Return paddle rectangle used for collision detection."""
        return pygame.Rect(self.x, self.y, self.width, self.size)

    def get_center(self):
        """Return the center coordinates of the paddle."""
        return pygame.math.Vector2(self.x + self.width // 2, self.y + self.size // 2)
