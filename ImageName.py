import pygame
from pygame.locals import *
pygame.init()


# Create an 800x600 sized screen
screen = pygame.display.set_mode([50, 50]) 
# This sets the name of the window
pygame.display.set_caption('test')
#clock
clock = pygame.time.Clock()


background_image = pygame.image.load("pw1.ppm").convert()

done = False
while not done:
        for event in pygame.event.get():
            #if( pygame.key.get_pressed()[pygame.K_SPACE] != 0 ):
            #    toggle_fullscreen()
            if event.type == pygame.QUIT or(event.type is KEYDOWN and event.key == K_ESCAPE):
                done = True
        screen.blit(background_image, (0,0))
        pygame.display.flip()