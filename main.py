# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame, player, circleshape
from constants import *

def main():
    running = True
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0

    # Creation of the player
    x_p = SCREEN_WIDTH / 2
    y_p = SCREEN_HEIGHT / 2
    mav = player.Player(x_p, y_p)
    
    
    # gameloop
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill("black")
        mav.draw(screen)
        pygame.display.flip()
        dt = clock.tick(60) / 1000

if __name__ == "__main__":
        main()
