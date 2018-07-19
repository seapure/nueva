#pygame

import pygame
pygame.init()

window = pygame.display.set_mode((1080, 720))
is_end = False

def draw_image():
    window.blit(pygame.image.load("ryan.gif"), (180, 100))

while not is_end : 
    for event in pygame.event.get() :
        if event.type == pygame.QUIT :
            is_end = True

    window.fill((255, 255, 255))
    draw_image()
    pygame.display.update()

pygame.quit()
quit()  