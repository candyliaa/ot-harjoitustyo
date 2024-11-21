import pygame
from sprites.ball import Ball
from sprites.paddle import Paddle
from sprites.colors import color_dict
from config import window_size, FPS


def main():

    running = True

    own_score = 0
    enemy_score = 0

    game_window = pygame.display.set_mode(window_size)

    pygame.init()
    clock = pygame.time.Clock()

    collision_timeout = 0

    pygame.display.set_caption("Pong!")
    game_window.fill(color_dict["black"])

    ball = Ball(window_size[0]//2, window_size[1]//2)

    own_paddle = Paddle(
        window_size[0]-100, window_size[1]//2, color=(0, 255, 0))
    enemy_paddle = Paddle(
        50, window_size[1]//2, color=(0, 255, 0))

    own_movement = 0
    enemy_movement = 0

    while running:
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

        scored = ball.update(window_size)
        own_paddle.update(window_size, own_movement)
        enemy_paddle.update(window_size, enemy_movement)

        if scored:
            if scored == "own":
                own_score += 1
            elif scored == "enemy":
                enemy_score += 1

        if collision_timeout == 0:
            if pygame.Rect.colliderect(ball.get_ball_rect(), own_paddle.get_paddle_rect()):
                ball.collision()
                collision_timeout = 10
            if pygame.Rect.colliderect(ball.get_ball_rect(), enemy_paddle.get_paddle_rect()):
                ball.collision()
                collision_timeout = 10

        own_paddle.display_paddle(game_window)
        enemy_paddle.display_paddle(game_window)
        ball.draw_ball(game_window)

        pygame.display.update()
        game_window.fill(color_dict["black"])
        clock.tick(FPS)

        if collision_timeout > 0:
            collision_timeout -= 1


if __name__ == "__main__":
    main()
