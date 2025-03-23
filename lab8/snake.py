import pygame
import time
import random

pygame.init()

width = 800
height = 600
screen = pygame.display.set_mode((width, height))

score = 0
level = 1
speed = 200
fruit_eaten = False
fr_x = random.randrange(1, width // 10) * 10
fr_y = random.randrange(1, height // 10) * 10
fruit_coor = [fr_x, fr_y]

head_square = [100, 100]
squares = [
    [30, 100], [40, 100], [50, 100], [60, 100], [70, 100],
    [80, 100], [90, 100], [100, 100],
]

next_dir = "right"
direction = "right"

def game_over(font, size, color):
    g_o_font = pygame.font.SysFont(font, size)
    g_o_surface = g_o_font.render(f"Game Over, your score: {score}", True, color)
    g_o_rect = g_o_surface.get_rect(center=(width // 2, height // 2))

    screen.blit(g_o_surface, g_o_rect)
    pygame.display.update()
    pygame.time.delay(4000)
    pygame.quit()

def generate_food():
    global fruit_coor
    while True:
        fr_x = random.randrange(1, width // 10) * 10
        fr_y = random.randrange(1, height // 10) * 10
        fruit_coor = [fr_x, fr_y]
        if fruit_coor not in squares:
            break

done = False
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_DOWN:
                next_dir = "down"
            if event.key == pygame.K_UP:
                next_dir = "up"
            if event.key == pygame.K_LEFT:
                next_dir = "left"
            if event.key == pygame.K_RIGHT:
                next_dir = "right"

    if head_square in squares[:-1]:
        game_over("Times New Roman", 45, (128, 128, 128))

    if next_dir == "right" and direction != "left":
        direction = "right"
    if next_dir == "up" and direction != "down":
        direction = "up"
    if next_dir == "left" and direction != "right":
        direction = "left"
    if next_dir == "down" and direction != "up":
        direction = "down"

    if direction == "right":
        head_square[0] += 10
    if direction == "left":
        head_square[0] -= 10
    if direction == "up":
        head_square[1] -= 10
    if direction == "down":
        head_square[1] += 10

    if head_square[0] >= width:  
        head_square[0] = 0
    if head_square[0] < 0:  
        head_square[0] = width - 10
    if head_square[1] >= height:  
        head_square[1] = 0
    if head_square[1] < 0:  
        head_square[1] = height - 10

    new_square = [head_square[0], head_square[1]]
    squares.append(new_square)
    squares.pop(0)

    if head_square[0] == fruit_coor[0] and head_square[1] == fruit_coor[1]:
        fruit_eaten = True
        score += 10
        if score % 30 == 0:
            level += 1
            speed = max(50, speed - 20)

    if fruit_eaten:
        generate_food()
        fruit_eaten = False
        squares.insert(0, squares[0]) 

    screen.fill((0, 0, 0))

    score_font = pygame.font.SysFont("Times New Roman", 20)
    score_surface = score_font.render(f"Score: {score}  Level: {level}", True, (128, 128, 128))
    score_rect = score_surface.get_rect(topleft=(10, 10))
    screen.blit(score_surface, score_rect)

    pygame.draw.circle(screen, (0, 255, 0), (fruit_coor[0] + 5, fruit_coor[1] + 5), 5)

    for el in squares:
        pygame.draw.rect(screen, (255, 255, 255), pygame.Rect(el[0], el[1], 10, 10))

    pygame.display.flip()
    pygame.time.delay(speed)

pygame.quit()
