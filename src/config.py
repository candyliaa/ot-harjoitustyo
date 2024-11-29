from sprites.colors import color_dict

WINDOW_SIZE = (1280, 1024)

DIFFICULTY = 0.6

FPS = 30

PADDLE_SPEED = 10
PADDLE_SIZE = 200

BALL_SPEED = 15
BALL_SIZE = 10

class Config:
    def __init__(self):
        self.difficulty = DIFFICULTY
        self.fps = FPS

        self.window_size = WINDOW_SIZE

        self.ball_color = color_dict["white"]
        self.ball_speed = BALL_SPEED
        self.ball_size = BALL_SIZE

        self.paddle_color = color_dict["green"]
        self.paddle_speed = PADDLE_SPEED
        self.paddle_size = PADDLE_SIZE
