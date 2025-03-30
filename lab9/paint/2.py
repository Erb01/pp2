import pygame
pygame.init()

WIDTH = 800
HEIGHT = 600

screen = pygame.display.set_mode((WIDTH, HEIGHT))
base_layer = pygame.Surface((WIDTH, HEIGHT))
base_layer.fill((0, 0, 0)) 

colorRED = (255, 0, 0)
colorWHITE = (255, 255, 255)
colorBLACK = (0, 0, 0)

clock = pygame.time.Clock()

LMBpressed = False
THICKNESS = 2

currX = 0
currY = 0

prevX = 0
prevY = 0

def calculate_triangle(x1, y1, x2, y2):
    side_length = abs(x2 - x1)  
    if x2 < x1:
        side_length = -side_length 

    vertex1 = (x1, y1)
    vertex2 = (x1 + side_length, y1)
    vertex3 = (x1 + side_length // 2, y1 - abs(side_length))  
    return [vertex1, vertex2, vertex3]

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            LMBpressed = True
            prevX = event.pos[0]
            prevY = event.pos[1]
        if event.type == pygame.MOUSEMOTION and LMBpressed:
            currX = event.pos[0]
            currY = event.pos[1]
            screen.fill(colorBLACK)  
            screen.blit(base_layer, (0, 0)) 
            pygame.draw.polygon(screen, colorRED, calculate_triangle(prevX, prevY, currX, currY), THICKNESS)
        if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
            LMBpressed = False
            currX = event.pos[0]
            currY = event.pos[1]
            pygame.draw.polygon(base_layer, colorRED, calculate_triangle(prevX, prevY, currX, currY), THICKNESS)
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_EQUALS:
                print("increased thickness")
                THICKNESS += 1
            if event.key == pygame.K_MINUS:
                if THICKNESS > 1:
                    print("reduced thickness")
                    THICKNESS -= 1
    
    if LMBpressed:
        currX, currY = pygame.mouse.get_pos()
        screen.fill(colorBLACK)  
        screen.blit(base_layer, (0, 0)) 
        pygame.draw.polygon(screen, colorRED, calculate_triangle(prevX, prevY, currX, currY), THICKNESS)
    else:
        screen.fill(colorBLACK)
        screen.blit(base_layer, (0, 0))  

    pygame.display.flip()
    clock.tick(60)
pygame.quit()