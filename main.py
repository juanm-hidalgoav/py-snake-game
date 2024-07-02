import pygame
from config import *
from game import game_loop
from input_box import get_user_name

pygame.init()
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Snake Game')
clock = pygame.time.Clock()

if __name__ == "__main__":
    user_name = get_user_name(screen)
    screen.fill(blue)  # Clear the screen before starting the game loop
    pygame.display.flip()  # Update the screen
    game_loop(screen, clock, user_name)
    pygame.quit()
