import random
import pygame
from sprites.ball import Ball
from sprites.paddle import Paddle
from sprites.colors import color_dict
from config import Config
from ui.cli_ui import PongCLI
from ui.console import ConsoleIO
from repositories.stats_repository import StatsRepository
from db_connection import get_database_connection

class Game:
    """Main class for running the game.
    Attributes:
        config: The config object which the game uses.
    """
    def __init__(self, config):
        """The constructor of the class, which initializes the required variables.

        Args:
            config: The config object which the game uses.
        """
        self.config = config
        # Initialize starting variables
        self._running = True

        self.own_score = 0
        self.enemy_score = 0

        # Stats variables that are written to database
        self.ball_bounces = 0

        self.game_window = pygame.display.set_mode(self.config.window_size)

        pygame.init()

        pygame.font.init()
        self._font = pygame.font.SysFont("Arial", 24)

        self._clock = pygame.time.Clock()

        self._collision_timeout = 0

        pygame.display.set_caption("Pong!")
        self.game_window.fill(color_dict["black"])

        self.balls = []
        for _ in range(self.config.ball_amount):
            self.balls.append(Ball((self.config.window_size[0]//2,
                            self.config.window_size[1]//2),
                            self.config.ball_speed,
                            self.config.ball_color,
                            self.config.ball_size))

        self.own_paddle = Paddle(
            (self.config.window_size[0]-100,
             self.config.window_size[1]//2),
             self.config.paddle_speed,
             self.config.paddle_color,
             self.config.paddle_size)
        self.enemy_paddle = Paddle(
            (50,
             self.config.window_size[1]//2),
             self.config.paddle_speed,
             self.config.paddle_color,
             self.config.paddle_size)

        self._own_movement = 0
        self._enemy_movement = 0

    def _update_objects(self):
        """Method to update the position of each game object in play.
        """
        for ball in self.balls:
            scored = ball.update(self.config.window_size)
            if scored:
                if scored == "own":
                    self.own_score += 1
                elif scored == "enemy":
                    self.enemy_score += 1
                elif scored == "bounce":
                    self.ball_bounces += 1
        self.own_paddle.update(self.config.window_size, self._own_movement)
        self.enemy_paddle.update(self.config.window_size, self._enemy_movement)

    def _display_game_objects(self):
        """Method to draw each game object in play to the game window.
        """
        self.own_paddle.display_paddle(self.game_window)
        self.enemy_paddle.display_paddle(self.game_window)
        for ball in self.balls:
            ball.draw_ball(self.game_window)

        self.game_window.blit(
            self._font.render(
                f"Points: {self.own_score}",
                False,
                color_dict["white"]
                ),
            (self.config.window_size[0] - 125, 10)
            )

        self.game_window.blit(
            self._font.render(
                f"Points: {self.enemy_score}",
                False,
                color_dict["white"]
                ),
            (25, 10)
            )

        pygame.display.update()
        self.game_window.fill(color_dict["black"])
        self._clock.tick(self.config.fps)

    def _move_enemy(self):
        """Method to move the enemy paddle according to the closest ball's y-position.
        """
        if random.random() < self.config.difficulty:
            closest_ball = self.balls[0]
            for ball in self.balls:
                if ball.position[0] < closest_ball.position[0]:
                    closest_ball = ball
            self._enemy_movement = self._enemy_movement_logic(self.enemy_paddle, closest_ball)

    def start_game(self):
        """The game loop.
        """
        while self._running:
            for event in pygame.event.get():
                if not self.keep_running(event):
                    self._running = False
                    return

            self._own_movement = self._get_input()

            self._move_enemy()

            self._update_objects()

            self._enemy_movement = 0

            for ball in self.balls:
                if ball.collision_timeout == 0:
                    if self._paddle_collision(self.own_paddle, self.enemy_paddle, ball):
                        ball.collision_timeout = 10

            self._display_game_objects()

            for ball in self.balls:
                if ball.collision_timeout > 0:
                    ball.collision_timeout -= 1

    def keep_running(self, event):
        """Check if the game should close.

        Args:
            event: The event which is checked for if it's QUIT.

        Returns:
            Bool: Return the bool that decides if the game should continue running.
        """
        if event.type == pygame.QUIT:
            return False
        return True

    def _get_input(self):
        """Check the player's input.

        Returns:
            An integer that decides if the player should move up, down or at all.
        """
        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP]:
            return -1
        if keys[pygame.K_DOWN]:
            return 1
        if keys[pygame.K_w]:
            return -1
        if keys[pygame.K_s]:
            return 1
        return 0

    def _enemy_movement_logic(self, enemy_paddle, ball):
        """Method to check which direction the enemy paddle should move in.

        Args:
            enemy_paddle: The enemy paddle object.
            ball: The ball object.

        Returns:
            An integer that decides if the enemy should move up or down.
        """
        if enemy_paddle.get_center().y + 25 < ball.position.y:
            return 1
        if enemy_paddle.get_center().y - 25 > ball.position.y:
            return -1
        return ball.direction.y

    def _paddle_collision(self, own_paddle, enemy_paddle, ball):
        """A method to detect if the ball has collided with either paddle.

        Args:
            own_paddle: The player's paddle object..
            enemy_paddle: The enemy's paddle object..
            ball: The ball object.

        Returns:
            A bool for if the ball hit a paddle.
        """
        if pygame.Rect.colliderect(ball.get_ball_rect(), own_paddle.get_paddle_rect()):
            ball.collision(own_paddle)
            self.ball_bounces += 1
            return True
        if pygame.Rect.colliderect(ball.get_ball_rect(), enemy_paddle.get_paddle_rect()):
            ball.collision(enemy_paddle)
            self.ball_bounces += 1
            return True
        return False

def main():
    """The main function to run the app.
    """
    config = Config.read()
    io = ConsoleIO()
    connection = get_database_connection()
    stats = StatsRepository(connection)
    cli = PongCLI(config, io, stats)
    start = cli.start()
    config.write()
    if start:
        pong_game = Game(config)
        pong_game.start_game()
        stats.write_score(pong_game.own_score, pong_game.enemy_score)
        stats.write_misc_stats(pong_game.ball_bounces,
                               pong_game.own_paddle.traveled,
                               pong_game.enemy_paddle.traveled
                               )
if __name__ == "__main__":
    main()
