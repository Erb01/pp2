import pygame
import math

pygame.init()

WIDTH = 800
HEIGHT = 600

screen = pygame.display.set_mode((WIDTH, HEIGHT))
base_layer = pygame.Surface((WIDTH, HEIGHT))
base_layer.fill((0, 0, 0))  

colorRED = (255, 0, 0)
colorBLACK = (0, 0, 0)

clock = pygame.time.Clock()

LMBpressed = False
THICKNESS = 5

currX = 0
currY = 0

prevX = 0
prevY = 0

def calculate_radius(x1, y1, x2, y2):
    """Calculate the distance between two points to use as a circle's radius."""
    return int(math.sqrt((x2 - x1)**2 + (y2 - y1)**2))

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            print("LMB pressed!")
            LMBpressed = True
            prevX = event.pos[0]
            prevY = event.pos[1]
        if event.type == pygame.MOUSEMOTION and LMBpressed:
            currX = event.pos[0]
            currY = event.pos[1]
            screen.fill(colorBLACK)  
            screen.blit(base_layer, (0, 0)) 
            radius = calculate_radius(prevX, prevY, currX, currY)
            pygame.draw.circle(screen, colorRED, (prevX, prevY), radius, THICKNESS)
        if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
            print("LMB released!")
            LMBpressed = False
            currX = event.pos[0]
            currY = event.pos[1]
            radius = calculate_radius(prevX, prevY, currX, currY)
            pygame.draw.circle(base_layer, colorRED, (prevX, prevY), radius, THICKNESS)
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_EQUALS:
                print("increased thickness")
                THICKNESS += 1
            if event.key == pygame.K_MINUS:
                if THICKNESS > 1:
                    print("reduced thickness")
                    THICKNESS -= 1
    screen.fill(colorBLACK)
    screen.blit(base_layer, (0, 0))
    pygame.display.flip()
    clock.tick(60)