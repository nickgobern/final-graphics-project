import pygame
from pygame.locals import *

def name():
    pygame.init()
    screen = pygame.display.set_mode((480, 360))
    name = "test"
    font = pygame.font.Font(None, 50)
    while True:
        
        screen.fill((0, 0, 0))
        block = font.render(name, True, (255, 255, 255))
        rect = block.get_rect()
        rect.center = screen.get_rect().center
        screen.blit(block, rect)
        pygame.display.flip()

if __name__ == "__main__":
    name()
    pygame.quit()