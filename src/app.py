import pygame
from sprites.ball import Ball
from sprites.paddle import Paddle
from sprites.colors import color_dict
from config import window_size, game_window, frames_per_second

def main():

    pygame.init()
    clock = pygame.time.Clock()

    pygame.display.set_caption("Pong!")
    game_window.fill(color_dict["black"])

    ball = Ball(window_size, game_window, window_size[0]//2, window_size[1]//2)

    own_paddle = Paddle(window_size, game_window, window_size[0]-100, window_size[1]//2, color=(0, 255, 0))
    enemy_paddle = Paddle(window_size, game_window, 50, window_size[1]//2, color=(0, 255, 0))

    own_movement = 0
    enemy_movement = 0
    
    while True:
        ball.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                break
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    own_movement = 1
                elif event.key == pygame.K_DOWN:
                    own_movement = -1
                elif event.key == pygame.K_w:
                    own_movement = 1
                elif event.key == pygame.K_s:
                    own_movement = -1
            own_paddle.update(own_movement)
    
        own_paddle.display_paddle()
        enemy_paddle.display_paddle()
        ball.display_ball()

        pygame.display.update()
        game_window.fill(color_dict["black"])
        clock.tick(frames_per_second)

if __name__ == "__main__":
    main()
