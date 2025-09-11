import pygame
import sys
from constants import *
from player import *
from asteroid import *
from asteroidfield import *

def main():
    # create groups and add the Player class to both
    drawable = pygame.sprite.Group()
    updatable = pygame.sprite.Group()
    Player.containers = (drawable, updatable)

    # create asteroids group and add the Asteroid class to it + the other 2 groups
    asteroids = pygame.sprite.Group()
    Asteroid.containers = (asteroids, drawable, updatable)
    # add AsteroidField to updatable, but not the others since its not an asteroid or a drawable
    AsteroidField.containers = (updatable)

    #create the player
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    # create an AsteroidField object
    asteroid_field = AsteroidField()

    #initialize pygame
    pygame.init
    
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            
        # fill (clear)
        pygame.Surface.fill(screen, "black")

        # update (move/rotate etc.)
        updatable.update(dt)

        # check for collisions between player and asteroids
        for asteroid in asteroids:
            if player.collide(asteroid):
                sys.exit("Game over!")

        # draw 
        for drawing in drawable:
            drawing.draw(screen)

        # flip (present) - makes drawing visible on screen
        pygame.display.flip()

        dt = clock.tick(60) / 1000




if __name__ == "__main__":
    main()
