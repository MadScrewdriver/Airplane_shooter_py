import pygame
from pygame.math import Vector2


class Rocket(object):

    def __init__(self, game):
        self.game = game
        self.speed = 5
        self.size = self.game.screen.get_size()
        self.pos = Vector2(self.size[0] / 2, self.size[1] * (5/6))
        self.vel = Vector2(self.speed, 0)
        self.touch_r = False
        self.touch_l = False
        self.margin = self.size[0] / 20
        self.player_size = self.size[0] / (self.size[0] / 15)
        self.points = [Vector2(0, -self.player_size),
                       Vector2(self.player_size, self.player_size),
                       Vector2(-self.player_size, self.player_size)]

    def tick(self):
        # Input
        pressed = pygame.key.get_pressed()
        if pressed[pygame.K_RIGHT] and not self.touch_r:
            self.pos += self.vel

        elif pressed[pygame.K_LEFT] and not self.touch_l:
            self.pos -= self.vel

    def draw(self):

        if self.pos.x + self.points[2].x <= self.margin:
            points = [Vector2(self.margin + self.vel.x, self.size[1] * (5 / 6)) + p for p in self.points]
            self.touch_l = True
            self.touch_r = False

        elif self.pos.x + self.points[1].x >= self.size[0] - self.margin:
            points = [Vector2(self.size[0] - self.margin - self.vel.x, self.size[1] * (5 / 6)) + p for p in self.points]
            self.touch_r = True
            self.touch_l = False

        else:
            points = [self.pos + p for p in self.points]
            self.touch_r = False
            self.touch_l = False

        pygame.draw.polygon(self.game.screen, (0, 255, 0), points)
