import pygame
import random
from pygame.math import Vector2

class Bullets():
    def __init__(self, game, player):
        self.bullets = []
        self.bullet_speed = 0.75
        self.game = game
        self.player = player
        self.pos = self.player.pos
        self.bullet_speed = Vector2(0, -self.bullet_speed)
        self.bull_end = 0

    def shoot(self):
        self.bullets.append([Vector2(0, -5) + self.pos, Vector2(5, 5) + self.pos, Vector2(-5, 5) + self.pos])

    def draw(self):
        self.bull_end = 0
        for bull_pos in range(len(self.bullets)):
            self.bullets[bull_pos] = [p + self.bullet_speed for p in self.bullets[bull_pos]]
            pygame.draw.polygon(self.game.screen, (255, 0, 0), self.bullets[bull_pos])

            if self.bullets[bull_pos][0].y < 20:
                self.bull_end += 1

        [self.bullets.pop(0) for _ in range(self.bull_end)]
        # print(self.pos)

