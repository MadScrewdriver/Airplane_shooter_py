import pygame
from pygame.math import Vector2
from random import randint
from math import sqrt


def detect_collision(x2, y2, w2, h2, x1, y1, w1, h1):
    if x2 + w2 >= x1 >= x2 and y2 + h2 >= y1 >= y2:
        return True

    elif x2 + w2 >= x1 + w1 >= x2 and y2 + h2 >= y1 >= y2:
        return True

    elif x2 + w2 >= x1 >= x2 and y2 + h2 >= y1 + h1 >= y2:
        return True

    elif x2 + w2 >= x1 + w1 >= x2 and y2 + h2 >= y1 + h1 >= y2:
        return True

    else:
        return False


class Enemy(object):

    def __init__(self, game, player, bullets):
        self.game = game
        self.player = player
        self.enemies = []
        self.size = self.game.screen.get_size()
        self.enemies_size = Vector2(self.size[0] / 3.90, self.size[0] / 5.27)
        self.bullets = bullets
        self.num_of_e = 0
        self.explo = []
        self.explo_end = []
        self.explo_pic = None
        self.enemy = pygame.image.load("en.png")
        self.e_destroy = []
        self.p_destroy = []
        self.enemy_pos = None

    def update(self):
        self.size = self.game.screen.get_size()
        self.enemies_size = Vector2(self.size[0] / 3.90, self.size[0] / 5.27)

    def tick(self):
        self.blast()

    def add_enemies(self):
        if self.num_of_e == 0:
            self.enemies.append(Vector2(randint(int(self.player.margin), int(self.size[0] - (self.player.margin +
                                                                                             self.enemies_size.x))),
                                        int(self.size[1] * (2 / 10))
                                        )
                                )
            self.num_of_e += 1

    def remove_enemies(self):
        a = 0
        for i in self.e_destroy:
            self.num_of_e -= 1
            self.enemies.pop(i - a)
            a += 1

        b = 0
        for i in self.p_destroy:
            self.bullets.bullets.pop(i - b)
            b += 1

    def touch(self, p):

        for b_p in range(len(self.bullets.bullets)):
            bullets_pos = self.bullets.bullets[b_p]

            if detect_collision(self.enemy_pos.x + ((12 / 27) * self.enemies_size.x),
                                self.enemy_pos.y, self.enemies_size.x * (3 / 27), self.enemies_size.y,
                                bullets_pos.x, bullets_pos.y, self.bullets.bullet_size,
                                self.bullets.bullet_size) or \
                    \
                    detect_collision(self.enemy_pos.x, self.enemy_pos.y + ((8 / 21) * self.enemies_size.x),
                                     self.enemies_size.x, self.enemies_size.y * (3 / 21),
                                     bullets_pos.x, bullets_pos.y, self.bullets.bullet_size,
                                     self.bullets.bullet_size) or \
                    \
                    detect_collision(self.enemy_pos.x + ((10 / 27) * self.enemies_size.x),
                                     self.enemy_pos.y, self.enemies_size.x * (7 / 27), self.enemies_size.y * (2 / 21),
                                     bullets_pos.x, bullets_pos.y, self.bullets.bullet_size,
                                     self.bullets.bullet_size):

                if p not in self.e_destroy:
                    self.explo.append([self.enemies[p], 16])
                    self.e_destroy.append(p)

                    self.p_destroy.append(b_p)

    def blast(self):
        self.explo_end = []

        for ex in range(len(self.explo)):
            if self.explo[ex][1] == 1:
                self.explo_end.append(ex)

            else:
                self.explo[ex][1] -= 1

        c = 0
        for i in self.explo_end:
            self.explo.pop(i - c)
            c += 1

    def draw(self):
        self.update()
        self.add_enemies()

        self.e_destroy = []
        self.p_destroy = []

        for p in range(len(self.enemies)):
            self.enemy_pos = self.enemies[p]
            self.game.screen.blit(pygame.transform.scale(self.enemy,
                                                         (int(self.enemies_size.x),
                                                          int(self.enemies_size.y))),
                                  (int(self.enemy_pos.x),
                                   int(self.enemy_pos.y)))
            self.touch(p)

        self.remove_enemies()

        for exp in self.explo:
            self.explo_pic = pygame.image.load("./explosion/" + str(exp[1]) + ".png")
            self.game.screen.blit(pygame.transform.scale(self.explo_pic,
                                                         (int(self.player.player_size.x),
                                                          int(self.player.player_size.y))),
                                  (int(exp[0].x),
                                   int(exp[0].y)))






