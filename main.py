# This allows us to use code from the open-source
# pygame library throughout this file
import pygame
import sys

# Import all of the constants
from constants import *
from logger import log_state, log_event
from player import *
from asteroid import *
from asteroidfield import *
from shot import *


def main():
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    game_clock = pygame.time.Clock()
    dt = 0

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Player.containers = (updatable, drawable)
    Asteroid.containers = (updatable, drawable, asteroids)
    AsteroidField.containers = (updatable)
    Shot.containers = (updatable, drawable, shots)

    player = Player(x = SCREEN_WIDTH / 2, y = SCREEN_HEIGHT / 2)
    asteroid_field = AsteroidField()

    # Game Loop
    while(1):
        log_state()
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        screen.fill("black")

        for draw_object in drawable:
            draw_object.draw(screen)

        for update_object in updatable:
            update_object.update(dt)

        # Collision detection if player is hit
        for asteroid in asteroids:

            # See if asteroid was hit by shot
            for shot in shots:
                if shot.has_collided(asteroid):
                    log_event("asteroid_shot")
                    asteroid.split()
                    shot.kill()

            # See if player was hit
            if asteroid.has_collided(player):
                log_event("player_hit")
                print("Game over!")
                sys.exit()

        pygame.display.flip() # refresh entire screen

        dt = game_clock.tick(60) / 1000


if __name__ == "__main__":
    main()
