import pygame
from pygame.math import Vector2


class Bullets(object):
    def __init__(self, game, player):
        pygame.init()
        self.game = game
        self.size = self.game.screen.get_size()
        self.b_s = self.size[0]
        self.bullets = []
        self.player = player
        self.pos = self.player.pos
        self.bull_end = 0
        self.bull_size = self.size[0] / 400
        self.bullet_speed = Vector2(0, -self.b_s)

    def update(self):
        self.size = self.game.screen.get_size()
        self.b_s = self.size[0] / 200
        self.bull_size = self.size[0] / 256
        self.bullet_speed = Vector2(0, -self.b_s)

    def shoot(self):
        self.bullets.append([Vector2(0, -self.bull_size) + self.pos,
                            Vector2(self.bull_size, self.bull_size) + self.pos,
                            Vector2(-self.bull_size, self.bull_size) + self.pos])

    def tick(self):
        self.update()

        self.bull_end = 0
        print(self.bullet_speed)
        for bull_pos in range(len(self.bullets)):
            self.bullets[bull_pos] = [p + self.bullet_speed for p in self.bullets[bull_pos]]

            if self.bullets[bull_pos][0].y < self.player.margin / 2:
                self.bull_end += 1

        [self.bullets.pop(0) for _ in range(self.bull_end)]

    def draw(self):
        self.update()

        for bull_pos in range(len(self.bullets)):
            pygame.draw.polygon(self.game.screen, (255, 255, 0), self.bullets[bull_pos])

