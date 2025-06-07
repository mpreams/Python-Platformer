import os
import random
import math
import pygame
from os import listdir
from os.path import isfile, join

pygame.init()
pygame.display.set_caption("Platformer")

BG_COLOR = (135, 206, 235)  # Sky blue
WIDTH, HEIGHT = 1000, 800
FPS = 60
PLAYER_SPEED = 5

window = pygame.display.set_mode((WIDTH, HEIGHT))

def get_backgroud(name):
    """Load the background image and create a list of tile positions."""
    if not os.path.exists(join("assets", "Background", name)):
        image = pygame.image.load(join("assets", "Background", "Gray.png")) 
    else:    
        image = pygame.image.load(join("assets", "Background", name))
    _, _, width, height = image.get_rect()
    tiles = []

    for i in range(WIDTH // width + 1):
        for j in range(HEIGHT // height + 1):
            pos = (i * width, j * height)
            tiles.append(pos)
    return tiles, image    

def draw(window, background, bg_image):
    """Draw the background on the window."""
    window.fill(BG_COLOR)
    for tile in background:
        window.blit(bg_image, tile) # tile position is a tuple (x, y)
    pygame.display.update()    

def main(window):
    clock = pygame.time.Clock()
    background, bg_image = get_backgroud("Blue.png")

    running = True
    while running:
        clock.tick(FPS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
                running = False
                break

        draw(window, background, bg_image)    

    pygame.quit()
    quit()            

if __name__ == "__main__":
    main(window)