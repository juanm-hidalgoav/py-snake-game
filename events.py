import pygame
from config import *

def handle_events(x1, y1, x1_change, y1_change, block_size):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT and x1_change == 0:
                x1_change = -block_size
                y1_change = 0
            elif event.key == pygame.K_RIGHT and x1_change == 0:
                x1_change = block_size
                y1_change = 0
            elif event.key == pygame.K_UP and y1_change == 0:
                y1_change = -block_size
                x1_change = 0
            elif event.key == pygame.K_DOWN and y1_change == 0:
                y1_change = block_size
                x1_change = 0
    return x1, y1, x1_change, y1_change
