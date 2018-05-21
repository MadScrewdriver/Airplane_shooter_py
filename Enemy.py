import pygame
from random import randint
from Basic_Component import BasicComponent


class Enemy(object):

    def __init__(self, game, player, bullets):
        self.game = game
        self.margin = self.game.margin
        self.enemies = []
        self.player = player
        self.size = self.game.screen.get_size()
        self.bullets = bullets
        self.num_of_e = 0
        self.explo = []
        self.explo_end = []
        self.explo_pic = None
        self.e_destroy = []
        self.p_destroy = []
        self.enemy_object = None
        self.enemy_width = self.size[0] / 3.90
        self.enemy_height = self.size[0] / 5.27

    def update(self):
        self.size = self.game.screen.get_size()

    def tick(self):
        self.blast()

    def add_enemies(self):
        if self.num_of_e == 0:
            self.enemies.append(BasicComponent(
                randint(int(self.margin), int(self.size[0] - (self.margin + self.size[0] / 3.90))),
                int(self.size[1] * (2 / 10)),
                self.enemy_width,
                self.enemy_height,
                ["en.png"], self.game.screen))

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

            body = BasicComponent(self.enemy_object.x + ((12 / 27) * self.enemy_width),
                                  self.enemy_object.y,
                                  self.enemy_width * (3 / 27),
                                  self.enemy_height,
                                  [],
                                  self.game.screen)

            wings = BasicComponent(self.enemy_object.x,
                                   self.enemy_object.y + ((8 / 21) * self.enemy_width),
                                   self.enemy_width,
                                   self.enemy_height * (3 / 21),
                                   [],
                                   self.game.screen)

            stabilizer = BasicComponent(self.enemy_object.x + (10 / 27) * self.enemy_width,
                                        self.enemy_object.y,
                                        self.enemy_width * (7 / 27),
                                        self.enemy_height * (2 / 21),
                                        [],
                                        self.game.screen)

            if bullets_pos.detect_collision(body) or bullets_pos.detect_collision(wings) or \
                    bullets_pos.detect_collision(stabilizer):

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
            self.enemy_object = self.enemies[p]
            self.enemy_object.draw(0)
            self.touch(p)

        self.remove_enemies()

        for exp in self.explo:
            self.explo_pic = pygame.image.load("./explosion/" + str(exp[1]) + ".png")
            self.game.screen.blit(pygame.transform.scale(self.explo_pic,
                                                         (int(self.player.get_width()),
                                                          int(self.player.get_height()))),
                                  (int(exp[0].x),
                                   int(exp[0].y)))






