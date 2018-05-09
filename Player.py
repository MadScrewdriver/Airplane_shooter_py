import pygame
from pygame.math import Vector2
from win32api import GetSystemMetrics


class Rocket(object):

    def __init__(self, game):
        pygame.init()
        self.game = game
        self.size = self.game.screen.get_size()
        self.speed = self.size[0] / 170
        self.vel = Vector2(self.speed, 0)
        self.touch_r = False
        self.touch_l = False
        self.margin = self.size[0] / 20
        self.player_size = Vector2(self.size[0] / 3.90, self.size[0] / 5.27)
        self.pos = Vector2(self.size[0] / 2 - self.player_size.x / 2, self.size[1] * (5/6))
        self.last_matrix = self.size[0]
        self.player = pygame.image.load("ap1.png")
        self.player_left = pygame.image.load("ap2.png")
        self.player_right = pygame.image.load("ap3.png")
        self.pressed = pygame.key.get_pressed()

    def update(self):
        self.size = self.game.screen.get_size()
        self.speed = self.size[0] / 200
        self.vel = Vector2(self.speed, 0)
        self.margin = self.size[0] / 20
        self.player_size = Vector2(self.size[0] / 3.90, self.size[0] / 5.27)
        self.pos.y = self.size[1] * (5/6)

        if self.size[0] != self.last_matrix:
            self.pos.x = (self.pos.x / self.last_matrix) * self.size[0]

        self.last_matrix = self.size[0]
        self.pressed = pygame.key.get_pressed()

    def tick(self):
        # Input
        pressed = pygame.key.get_pressed()
        if pressed[pygame.K_RIGHT] and not self.touch_r:
            self.pos += self.vel

        elif pressed[pygame.K_LEFT] and not self.touch_l:
            self.pos -= self.vel

    def draw(self):
        self.update()

        if self.pos.x <= self.margin / 2:
            self.touch_l = True
            self.touch_r = False

        elif self.pos.x + self.player_size.x >= self.size[0] - (self.margin / 2):
            self.touch_r = True
            self.touch_l = False

        else:
            self.touch_r = False
            self.touch_l = False

        if self.pressed[pygame.K_LEFT]:
            self.game.screen.blit(pygame.transform.scale(self.player_left,
                                                         (int(self.player_size.x),
                                                          int(self.player_size.y))),
                                                         (int(self.pos.x),
                                                          int(self.pos.y)))
        elif self.pressed[pygame.K_RIGHT]:
            self.game.screen.blit(pygame.transform.scale(self.player_right,
                                                         (int(self.player_size.x),
                                                          int(self.player_size.y))),
                                                         (int(self.pos.x),
                                                          int(self.pos.y)))
        else:
            self.game.screen.blit(pygame.transform.scale(self.player,
                                                         (int(self.player_size.x),
                                                          int(self.player_size.y))),
                                                        (int(self.pos.x),
                                                         int(self.pos.y)))

