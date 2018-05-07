import pygame
import sys
from Player import Rocket
from Bullet import Bullets


class Game(object):

    def __init__(self):
        # Config
        self.max_fps = 50
        self.screen = pygame.display.set_mode((1280, 720))
        self.clock = pygame.time.Clock()
        self.delta = 0.0

        # Initialization
        pygame.init()
        self.player = Rocket(self)
        self.bullet = Bullets(self, self.player)

        while True:
            self.screen.fill((0, 0, 0))
            # events

            for event in pygame.event.get():
                if event.type == pygame.QUIT or event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                    sys.exit(0)

                if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                    self.bullet.shoot()

            # Ticking
            self.delta += self.clock.tick() / 1000.0
            while self.delta > 1 / self.max_fps:
                self.tick()
                self.delta -= 1 / self.max_fps

            # Drawing

            self.draw()
            pygame.display.flip()

    def tick(self):
        self.player.tick()

    def draw(self):
        self.player.draw()
        self.bullet.draw()


if __name__ == '__main__':
    Game()




