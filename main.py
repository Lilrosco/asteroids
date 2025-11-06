# This allows us to use code from the open-source
# pygame library throughout this file
import pygame

# Import all of the constants
from constants import *
from logger import log_state
from player import *


def main():
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    black_background = (0, 0, 0)
    game_clock = pygame.time.Clock()
    dt = 0

    player = Player(x = SCREEN_WIDTH / 2, y = SCREEN_HEIGHT / 2)

    # Game Loop
    while(1):
        log_state()
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        pygame.Surface.fill(screen, black_background)

        player.update(dt)
        player.draw(screen)
        pygame.display.flip() # refresh entire screen

        dt = game_clock.tick(60) / 1000


if __name__ == "__main__":
    main()
