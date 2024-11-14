class Ball():
    def __init__(self, x=window_size[0]//2, y=window_size[1]//2, speed=1, color=(255, 255, 255), size=2):
        self.x = x
        self.y = y

        self.x_dir = 1
        self.y_dir = 2

        self.speed = speed
        self.color = color

        self.size = size

        self.ball = pygame.draw.circle(game_window, self.color, (self.x, self.y), self.size)

    def update(self):

        if self.x <= 0:
            self.x_dir = 1
        elif self.x >= window_size[0]:
            self.x_dir = -1

        if self.y <= 0:
            self.y_dir = 1
        if self.y <= window_size[1]:
            self.y_dir = -1

        self.x += self.speed * self.direction[0]
        self.y += self.speed * self.direction[1]

    def return_ball(self):
        return self.ball
