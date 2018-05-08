import pygame
from pygame.math import Vector2
from random import randint
from math import sqrt


class Enemy(object):

    def __init__(self, game, player, bullets):
        pygame.init()
        self.game = game
        self.player = player
        self.enemies = []
        self.size = self.game.screen.get_size()
        self.enemies_r = self.size[0] / 50
        self.bullets = bullets
        self.num_of_e = 0

    def update(self):
        self.size = self.game.screen.get_size()
        self.enemies_r = self.size[0] / 50

    def draw(self):
        self.update()

        if self.num_of_e == 0:
            self.enemies.append(Vector2(randint(int(self.size[0] / 20),
                                                int(self.size[0] - self.size[0] / 20)
                                                ),
                                        int(self.size[1] * (2 / 10))
                                        )
                                )
            self.num_of_e += 1

        e_destroy = []
        for p in range(len(self.enemies)):
            circle_pos = self.enemies[p]
            pygame.draw.circle(self.game.screen, (255, 0, 0), (int(circle_pos.x), int(circle_pos.y)),
                               int(self.enemies_r))

            for bullets_pos in self.bullets.bullets:
                centre_bull = bullets_pos[0] - Vector2(0, self.bullets.bull_size)

                if sqrt((centre_bull.x - circle_pos.x) ** 2 + (centre_bull.y - circle_pos.y) ** 2) <= self.enemies_r \
                     + self.bullets.bull_size:
                    e_destroy.append(p)

        a = 0
        for i in e_destroy:
            self.num_of_e -= 1
            self.enemies.pop(i - a)
            a += 1






