import pygame

pygame.init()

WIDTH = 800
HEIGHT = 600

screen = pygame.display.set_mode((WIDTH, HEIGHT))
base_layer = pygame.Surface((WIDTH, HEIGHT))
base_layer.fill((0, 0, 0)) 

colorRED = (255, 0, 0)
colorBLACK = (0, 0, 0)
THICKNESS = 5

clock = pygame.time.Clock()

drawing = False 
erasing = False  

prevX = 0
prevY = 0

def draw_line(surface, x1, y1, x2, y2, color, thickness):
    pygame.draw.line(surface, color, (x1, y1), (x2, y2), thickness)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                drawing = True
                erasing = False
                prevX, prevY = event.pos
            elif event.button == 3:  
                erasing = True
                drawing = False
                prevX, prevY = event.pos

        if event.type == pygame.MOUSEBUTTONUP:
            if event.button == 1:  
                drawing = False
            elif event.button == 3:  
                erasing = False

        if event.type == pygame.MOUSEMOTION:
            currX, currY = event.pos
            if drawing:
                draw_line(base_layer, prevX, prevY, currX, currY, colorRED, THICKNESS)
                prevX, prevY = currX, currY
            elif erasing:
                draw_line(base_layer, prevX, prevY, currX, currY, colorBLACK, THICKNESS)
                prevX, prevY = currX, currY

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_EQUALS:  
                THICKNESS += 1
                print("Increased thickness to", THICKNESS)
            if event.key == pygame.K_MINUS: 
                if THICKNESS > 1:
                    THICKNESS -= 1
                    print("Decreased thickness to", THICKNESS)
    
    screen.fill(colorBLACK)
    screen.blit(base_layer, (0, 0))
    pygame.display.flip()
    clock.tick(60)