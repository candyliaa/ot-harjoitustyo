from sprites.colors import color_dict
import json

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

    def write(self):
        with open("config.json", "w") as f:
            json.dump(vars(self), f)

    @staticmethod
    def read():
        with open("config.json", "r") as f:
            json_object = json.load(f)

        config = Config()
        config.difficulty = json_object["difficulty"]
        config.fps = json_object["fps"]
        config.window_size = json_object["window_size"]

        config.ball_color = json_object["ball_color"]
        config.ball_speed = json_object["ball_speed"]
        config.ball_size = json_object["ball_size"]

        config.paddle_color = json_object["paddle_color"]
        config.paddle_speed = json_object["paddle_speed"]
        config.paddle_size = json_object["paddle_size"]

        return config
