import pygame # type: ignore
import sys
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField

def main():
    pygame.init()
    # Creates the screen, clock, and dt variable (delta time)
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0
    # Creates two groups, one for updateable objects, the other for drawable objects
    # We place our Player class into both of those containers
    # We then define our player object
    updateable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    Player.containers = (updateable, drawable)
    player = Player(SCREEN_WIDTH/2,SCREEN_HEIGHT/2)

    asteroids = pygame.sprite.Group()
    Asteroid.containers = (asteroids, updateable, drawable)

    AsteroidField.containers = (updateable, )
    asteroid_field = AsteroidField()

    # Begins the game loop, draws a black screen based on the screen width and screen height constants.
    # Allows you to quit out
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        dt = clock.tick(60)/1000

        # Two loops using the newly defined pygame.sprite.Group objects to update and draw all objects in the group
        for obj in updateable:
            obj.update(dt)

        screen.fill("black")

        for obj in asteroids:
            if player.is_colliding(obj):
                print("Game over!")
                sys.exit()

        for obj in drawable:
            obj.draw(screen)

        pygame.display.flip()

if __name__ == "__main__":
    main()