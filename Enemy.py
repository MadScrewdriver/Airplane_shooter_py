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
        self.enemies_r = self.size[0] / 14
        self.bullets = bullets
        self.num_of_e = 0

    def update(self):
        self.size = self.game.screen.get_size()
        self.enemies_r = self.size[0] / 15

    def draw(self):
        self.update()

        if self.num_of_e == 0:
            self.enemies.append(Vector2(randint(int(self.player.margin + self.enemies_r),
                                                int(self.size[0] - (self.player.margin + self.enemies_r))
                                                ),
                                        int(self.size[1] * (2 / 10))
                                        )
                                )
            self.num_of_e += 1

        e_destroy = []
        p_destroy = []
        for p in range(len(self.enemies)):
            circle_pos = self.enemies[p]
            pygame.draw.circle(self.game.screen, (255, 0, 0), (int(circle_pos.x), int(circle_pos.y)),
                               int(self.enemies_r))

            for b_p in range(len(self.bullets.bullets)):
                bullets_pos = self.bullets.bullets[b_p]

                if sqrt((bullets_pos.x - circle_pos.x) ** 2 + (bullets_pos.y - circle_pos.y) ** 2) <= self.enemies_r \
                   + self.bullets.bullet_size / 2:

                    if p not in e_destroy:
                        e_destroy.append(p)

                    p_destroy.append(b_p)

        a = 0
        for i in e_destroy:
            self.num_of_e -= 1
            self.enemies.pop(i - a)
            a += 1

        b = 0
        for i in p_destroy:
            self.bullets.bullets.pop(i - b)
            b += 1
