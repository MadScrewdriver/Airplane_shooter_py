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
        self.max_fps = 120
        self.screen_with = 480
        self.screen_lenght = 720
        self.screen = pygame.display.set_mode((self.screen_with, self.screen_lenght), HWSURFACE | DOUBLEBUF | RESIZABLE)
        self.s_info = pygame.display.Info()
        self.clock = pygame.time.Clock()
        self.delta = 0.0

        # Initialization
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

                if event.type == VIDEORESIZE:
                    self.screen = pygame.display.set_mode(event.dict['size'], HWSURFACE | DOUBLEBUF | RESIZABLE)
                    self.s_info = pygame.display.Info()

                    if self.s_info.current_w / self.s_info.current_h != self.screen_with / self.screen_lenght:
                        self.screen = pygame.display.set_mode((int(get_work_area() *
                                                              (self.screen_with / self.screen_lenght)),
                                                              get_work_area()),
                                                              HWSURFACE | DOUBLEBUF | RESIZABLE)

                    if self.s_info.current_h > get_work_area():
                        self.screen = pygame.display.set_mode((self.s_info.current_w,
                                                               int(self.s_info.current_w *
                                                                   (self.screen_with /
                                                                    self.screen_lenght))),
                                                              HWSURFACE | DOUBLEBUF | RESIZABLE)

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




