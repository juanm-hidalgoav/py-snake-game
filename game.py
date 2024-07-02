import pygame
import time
from config import *
from display import draw_snake, display_score, draw_foods
from events import handle_events
from food import generate_foods, check_food_collision
from score import save_score, get_top_5_scores, get_scores

def game_loop(screen, clock, user_name):
    game_over = False
    game_close = False

    x1, y1 = screen_width / 2, screen_height / 2
    x1_change, y1_change = 0, 0
    snake_list = []
    length_of_snake = 1
    growth_counter = 0
    score = 0
    block_size = initial_block_size

    foods = generate_foods(screen_width, screen_height, block_size, [])

    while not game_over:
        while game_close:
            display_end_screen(screen, user_name, score)
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_1:
                        game_loop(screen, clock, user_name)
                    elif event.key == pygame.K_2:
                        game_over = True
                        game_close = False

        x1, y1, x1_change, y1_change = handle_events(x1, y1, x1_change, y1_change, block_size)

        # Wrap around screen
        if x1 >= screen_width:
            x1 = 0
        elif x1 < 0:
            x1 = screen_width - block_size
        if y1 >= screen_height:
            y1 = 0
        elif y1 < 0:
            y1 = screen_height - block_size

        x1 += x1_change
        y1 += y1_change
        snake_head = [x1, y1]
        snake_list.append(snake_head)
        if len(snake_list) > length_of_snake:
            del snake_list[0]

        for segment in snake_list[:-1]:
            if segment == snake_head:
                game_close = True

        screen.fill(blue)
        draw_snake(screen, block_size, snake_list)
        draw_foods(screen, foods, block_size)
        display_score(screen, score)

        pygame.display.update()

        foods, eaten_count = check_food_collision(foods, x1, y1, block_size)
        growth_counter += eaten_count
        score += 10 * eaten_count
        foods = generate_foods(screen_width, screen_height, block_size, foods)

        if growth_counter > 0:
            length_of_snake += 1
            growth_counter -= 1

        clock.tick(snake_speed)

    save_score(user_name, score)
    display_end_screen(screen, user_name, score)

def display_end_screen(screen, user_name, score):
    screen.fill(blue)
    rank = get_player_rank(user_name, score)
    message = get_end_message(rank)

    font_style = pygame.font.SysFont(None, 50)
    wrapped_text = wrap_text(message, font_style, screen_width - 20)
    y_offset = screen_height / 6
    for line in wrapped_text:
        line_surface = font_style.render(line, True, red)
        line_rect = line_surface.get_rect(center=(screen_width / 2, y_offset))
        screen.blit(line_surface, line_rect)
        y_offset += line_rect.height + 10

    top_scores = get_top_5_scores()
    font_style = pygame.font.SysFont(None, 35)
    y_offset += 20
    for score_entry in top_scores:
        score_text = f"{score_entry['name']}: {score_entry['score']}"
        score_message = font_style.render(score_text, True, white)
        score_message_rect = score_message.get_rect(center=(screen_width / 2, y_offset))
        screen.blit(score_message, score_message_rect)
        y_offset += 40

    pygame.display.update()

def get_player_rank(name, score):
    scores = get_scores()
    scores.append({"name": name, "score": score})
    scores = sorted(scores, key=lambda x: x["score"], reverse=True)
    for rank, entry in enumerate(scores):
        if entry["name"] == name and entry["score"] == score:
            return rank + 1
    return len(scores)

def get_end_message(rank):
    messages = {
        1: "You did it!, one more for fun (press 1) or maybe another day (press 2)",
        2: "Nicely done!, just one more (press 1) or maybe another day (press 2)",
        3: "Bravo!, let's give a try again (press 1) or maybe another day (press 2)",
        4: "You're amazing! let's give a try again (press 1) or maybe another day (press 2)",
        5: "Great! let's give a try again (press 1) or maybe another day (press 2)"
    }
    return messages.get(rank, "You're almost there, don't give up! (press 1) I'm done (press 2)")

def wrap_text(text, font, max_width):
    words = text.split(' ')
    lines = []
    current_line = []
    current_width = 0

    for word in words:
        word_surface = font.render(word, True, (0, 0, 0))
        word_width, word_height = word_surface.get_size()
        if current_width + word_width >= max_width:
            lines.append(' '.join(current_line))
            current_line = [word]
            current_width = word_width
        else:
            current_line.append(word)
            current_width += word_width + font.size(' ')[0]

    if current_line:
        lines.append(' '.join(current_line))

    return lines
