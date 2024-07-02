import pygame
from config import *

def draw_snake(screen, block_size, snake_list):
    for block in snake_list:
        pygame.draw.rect(screen, black, [block[0], block[1], block_size, block_size])

def display_score(screen, score):
    font = pygame.font.SysFont(None, 35)
    value = font.render("Your Score: " + str(score), True, white)
    screen.blit(value, [0, 0])

def draw_foods(screen, foods, block_size):
    for food in foods:
        x, y, color = food
        pygame.draw.rect(screen, color, [x, y, block_size, block_size])
