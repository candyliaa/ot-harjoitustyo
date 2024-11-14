import pygame
from sprites.ball import Ball
from sprites.paddle import Paddle
from sprites.colors import color_dict
from config import window_size, game_window

def main():

    pygame.init()

    pygame.display.set_caption("Pong!")

    game_window.fill(color_dict["black"])

    ball = Ball(window_size, game_window)

    own_paddle = Paddle(window_size, game_window, color=(0, 255, 0))
    enemy_paddle = Paddle(window_size, game_window, x=100, color=(0, 255, 0))

    paddles = [own_paddle, enemy_paddle]

    own_movement = 0
    enemy_movement = 0
    
    while True:
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

if __name__ == "__main__":
    main()



