
"""This is a game of "No te enojes" for everyone"""

import os
from pathlib import Path
import pygame

def main():

    WIDTH = 800
    HEIGHT = 600
    FPS = 180

    real_background_image = Path("img")

    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    background_image = pygame.image.load("./").convert()
    background_rect = background_image.get_rect()

    pygame.display.set_caption ("JumperJA!")

    running = True


    clock=pygame.time.Clock()
    while running:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        screen.blit(background_image, background_rect)
        pygame.display.flip()
    pygame.quit()


#Make a big table


#Make mini tables

#make pieces


#a simple menu


#the calculations


#The win!!

if __name__ == "__main__":
    main()