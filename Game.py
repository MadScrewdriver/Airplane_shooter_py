import pygame
import sys
from Player import Rocket
from Bullet import Bullets
from Enemy import Enemy
from pygame.locals import *
from win32api import GetSystemMetrics
from Get_work_Area import get_work_area


class Game(object):

    def __init__(self):
        pygame.init()

        # Config
        self.max_fps = 100
        self.screen_with = int(GetSystemMetrics(0) * 0.28)
        self.screen_lenght = int(GetSystemMetrics(1) * 0.7)
        self.screen = pygame.display.set_mode((self.screen_with, self.screen_lenght))
        self.clock = pygame.time.Clock()
        self.delta = 0.0

        # Initialization
        self.player = Rocket(self)
        self.bullet = Bullets(self, self.player)
        self.enemy = Enemy(self, self.player, self.bullet)
        print(self.screen_with)

        while True:
            self.update()
            self.screen.fill((0, 60, 0))

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

    def update(self):
        self.screen_with = int(GetSystemMetrics(0) * 0.28)
        self.screen_lenght = int(GetSystemMetrics(1) * 0.7)

    def tick(self):
        self.bullet.tick()
        self.player.tick()

    def draw(self):
        self.bullet.draw()
        self.player.draw()
        self.enemy.draw()


if __name__ == '__main__':
    Game()




