import pygame
from sprites.ball import Ball
from sprites.paddle import Paddle
from sprites.colors import color_dict
from config import window_size, FPS

# pylint: disable=no-member
# Pylint argues that pygame has no member init, QUIT, key events etc. when they are mandatory.

def main():

    running = True

    game_window = pygame.display.set_mode(window_size)

    pygame.init()
    clock = pygame.time.Clock()

    pygame.display.set_caption("Pong!")
    game_window.fill(color_dict["black"])

    ball = Ball(window_size[0]//2, window_size[1]//2)

    own_paddle = Paddle(window_size, window_size[0]-100, window_size[1]//2, color=(0, 255, 0))
    enemy_paddle = Paddle(window_size, 50, window_size[1]//2, color=(0, 255, 0))

    own_movement = 0
    enemy_movement = 0

    while running:
        ball.update(window_size)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            keys = pygame.key.get_pressed()
            if keys[pygame.K_UP]:
                own_movement = -1
            elif keys[pygame.K_DOWN]:
                own_movement = 1
            elif keys[pygame.K_w]:
                own_movement = -1
            elif keys[pygame.K_s]:
                own_movement = 1
            else:
                own_movement = 0
        own_paddle.update(game_window, own_movement)

        own_paddle.display_paddle(game_window)
        enemy_paddle.display_paddle(game_window)
        ball.display_ball(game_window)

        pygame.display.update()
        game_window.fill(color_dict["black"])
        clock.tick(FPS)

if __name__ == "__main__":
    main()
