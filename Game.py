import pygame
import sys
from Player import Rocket
from Bullet import Bullets
from Enemy import Enemy

class Game(object):

    def __init__(self):
        # Config
        self.max_fps = 120
        self.screen = pygame.display.set_mode((1280, 720))
        self.clock = pygame.time.Clock()
        self.delta = 0.0

        # Initialization
        pygame.init()
        self.player = Rocket(self)
        self.bullet = Bullets(self, self.player)
        self.enemy = Enemy(self, self.player, self.bullet)

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
        self.enemy.draw()


if __name__ == '__main__':
    Game()




