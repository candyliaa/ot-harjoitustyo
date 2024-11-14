class Paddle():
    def __init__(self, x=window_size[0]-100, y=window_size[1]//2, speed=1, color=(), size=300):
        self.x = x
        self.y = y
        self.size = size

        self.speed = speed
        self.color = color

        self.paddle = pygame.draw.rect(game_window, self.color, self.paddle_rect)
        self.paddle_rect = pygame.Rect(game_window, self.x, self.y, 50, size)

    def update(self, movement=0):
        self.y += self.speed * movement
        if self.y <= 0:
            self.y = 0
        if self.y + self.size >= window_size[1]:
            self.y = window_size[1]
