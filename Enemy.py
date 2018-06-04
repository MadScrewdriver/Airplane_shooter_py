import pygame
import os
from random import randint
from Basic_Component import BasicComponent
from settings import EnemiesConstants


class Enemy(EnemiesConstants):

    def __init__(self):
        self.num_of_e = 0
        self.explosions = []
        self.enemy_destroy = []
        self.bullets_destroy = []
        self.enemy_object = None

        super().__init__()

    def move_enemy(self):
        for e in range(len(self.ENEMIES)):
            enemy_pos = self.ENEMIES[e]
            enemy_pos.y += self.ENEMY_SPEED

            if enemy_pos.y == self.SCREEN_LENGTH:
                self.enemy_destroy.append(e)

    def tick(self):
        self.blast()
        self.move_enemy()

    def add_enemies(self):
        if self.num_of_e < 5:
            for n in range(5 - self.num_of_e):
                self.ENEMIES.append(BasicComponent(
                    randint(int(self.MARGIN), int(self.SCREEN_WITH - (self.MARGIN + self.SCREEN_WITH / 3.90))),
                    int(-self.ENEMY_HEIGHT),
                    self.ENEMY_WITH,
                    self.ENEMY_HEIGHT,
                    self.ENEMY_PIC_PATHS, self.SCREEN))

                self.num_of_e += 1

    def remove_enemies(self):
        a = 0
        for i in self.enemy_destroy:
            self.num_of_e -= 1
            self.ENEMIES.pop(i - a)
            a += 1

        b = 0
        for i in self.bullets_destroy:
            self.BULLETS.pop(i - b)
            b += 1

        self.enemy_destroy = []
        self.bullets_destroy = []

    def touch(self, score):

        for e in range(len(self.ENEMIES)):
            self.enemy_object = self.ENEMIES[e]
            self.enemy_object.draw(0)
            for b_p in range(len(self.BULLETS)):
                bullets_pos = self.BULLETS[b_p]

                body = BasicComponent(self.enemy_object.x + ((12 / 27) * self.ENEMY_WITH),
                                      self.enemy_object.y,
                                      self.ENEMY_WITH * (3 / 27),
                                      self.ENEMY_HEIGHT,
                                      [],
                                      self.SCREEN)

                wings = BasicComponent(self.enemy_object.x,
                                       self.enemy_object.y + ((8 / 21) * self.ENEMY_WITH),
                                       self.ENEMY_WITH,
                                       self.ENEMY_HEIGHT * (3 / 21),
                                       [],
                                       self.SCREEN)

                stabilizer = BasicComponent(self.enemy_object.x + (10 / 27) * self.ENEMY_WITH,
                                            self.enemy_object.y,
                                            self.ENEMY_WITH * (7 / 27),
                                            self.ENEMY_HEIGHT * (2 / 21),
                                            [],
                                            self.SCREEN)

                if bullets_pos.detect_collision(body) or bullets_pos.detect_collision(wings) or \
                        bullets_pos.detect_collision(stabilizer):

                    if e not in self.enemy_destroy:
                        self.explosions.append([self.enemy_object, 16])
                        self.enemy_destroy.append(e)
                        if b_p not in self.bullets_destroy:
                            self.bullets_destroy.append(b_p)

                    score += 10

        self.remove_enemies()
        return score

    def blast(self):
        explosion_end = []

        for ex in range(len(self.explosions)):
            if self.explosions[ex][1] == 1:
                explosion_end.append(ex)

            else:
                self.explosions[ex][1] -= 1

        c = 0
        for i in explosion_end:
            self.explosions.pop(i - c)
            c += 1

    def draw(self):
        self.add_enemies()

        for en in self.ENEMIES:
            en.draw(0)

        for exp in self.explosions:
            explosion_pic = pygame.image.load(os.path.join(self.EXPLO_PATH, str(exp[1]) + ".png"))
            self.SCREEN.blit(pygame.transform.scale(explosion_pic,
                                                    (int(self.PLAYER.get_width()),
                                                     int(self.PLAYER.get_height()))),
                             (int(exp[0].x),
                              int(exp[0].y)))






