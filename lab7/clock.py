import pygame
import time

pygame.init()

WIDTH, HEIGHT = 800, 600
CENTER = (WIDTH // 2, HEIGHT // 2)
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Micky Mouse Clock")

clock_face = pygame.image.load("clock.png")  
minute_hand = pygame.image.load("clock1.png")  
second_hand = pygame.image.load("clock2.png")  

minute_hand = pygame.transform.smoothscale(minute_hand, (800, 600))  
second_hand = pygame.transform.smoothscale(second_hand, (800, 600)) 

def blit_rotate_center(surf, image, center, angle):
    rotated_image = pygame.transform.rotate(image, angle)
    new_rect = rotated_image.get_rect(center=center)
    surf.blit(rotated_image, new_rect.topleft)

running = True
while running:
    screen.fill((255, 255, 255))  
    screen.blit(clock_face, (0, 0))  

    t = time.localtime()
    minutes = t.tm_min
    seconds = t.tm_sec

    minute_angle = -6 * minutes
    second_angle = -6 * seconds  
    blit_rotate_center(screen, minute_hand, CENTER, minute_angle)
    blit_rotate_center(screen, second_hand, CENTER, second_angle)

    pygame.display.flip()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    pygame.time.delay(1000)

pygame.quit()