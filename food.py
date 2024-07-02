import random
import pygame

def generate_foods(screen_width, screen_height, block_size, existing_foods, max_food_count=3):
    current_food_count = len(existing_foods)
    new_foods = existing_foods[:]
    if current_food_count < max_food_count:
        for _ in range(max_food_count - current_food_count):
            x = round(random.randrange(0, screen_width - block_size) / 10.0) * 10.0
            y = round(random.randrange(0, screen_height - block_size) / 10.0) * 10.0
            color = [random.randint(0, 255) for _ in range(3)]
            new_foods.append((x, y, color))
    return new_foods

def draw_foods(screen, foods, block_size):
    for food in foods:
        x, y, color = food
        pygame.draw.rect(screen, color, [x, y, block_size, block_size])

def check_food_collision(foods, x1, y1, block_size):
    new_foods = []
    eaten_count = 0
    for food in foods:
        food_x, food_y, color = food
        if x1 < food_x + block_size and x1 + block_size > food_x and y1 < food_y + block_size and y1 + block_size > food_y:
            eaten_count += 1
        else:
            new_foods.append(food)
    return new_foods, eaten_count
