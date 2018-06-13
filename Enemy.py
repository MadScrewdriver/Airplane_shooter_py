import pygame
import os
from Levels import Levels


class Enemy(Levels):

    def __init__(self, player):
        super().__init__()
        self.PLAYER = player
        self.num_of_e = 0
        self.enemy_destroy = []
        self.bullets_destroy = []
        self.explosion_end = []
        self.enemy_object = None
        self.score = 0

    def move_enemy(self):
        for e in range(len(self.ENEMIES)):
            enemy_pos = self.ENEMIES[e]

            if enemy_pos.y >= self.SCREEN_LENGTH - enemy_pos.get_height() - self.MARGIN * 3:
                self.enemy_destroy.clear()
                self.bullets_destroy.clear()
                self.explosion_end.clear()
                self.num_of_e = 0
                return True

            enemy_pos.move()

        return False

    def tick(self, score):
        self.blast()
        s = self.move_enemy()
        if not s:
            score, s = self.touch(score)

        return score, s

    def spawn_pos(self):

        if self.score < 0:
            self.level_1()

        elif self.score < 0:
            self.level_2()

        elif self.score < 100000:
            self.level_3()

    def add_enemies(self):
        
        if self.num_of_e == 0:
            self.spawn_pos()
            self.num_of_e = len(self.ENEMIES)

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

        self.enemy_destroy.clear()
        self.bullets_destroy.clear()

    def touch(self, score):
        stop = False

        for e in range(len(self.ENEMIES)):
            self.enemy_object = self.ENEMIES[e]
            self.enemy_object.draw(0)

            # collision bull with enemy and bull with bull
            for b_p in range(len(self.BULLETS)):
                bullets_pos = self.BULLETS[b_p]
                if bullets_pos.get_name() == "Fireball":
                    if bullets_pos.detect_collision(self.enemy_object):

                        if e not in self.enemy_destroy:
                            self.EXPLOSIONS.append([self.enemy_object, 16])
                            self.enemy_destroy.append(e)
                            if b_p not in self.bullets_destroy:
                                self.bullets_destroy.append(b_p)

                        score += 10

                    for bul in range(len(self.BULLETS)):
                        b = self.BULLETS[bul]
                        if (b.get_name() in ["Red_fireball", "Bomb"]) \
                                and bullets_pos.rectangle_collision(b):
                            if bul not in self.bullets_destroy and b_p not in self.bullets_destroy:
                                self.bullets_destroy.append(bul)
                                self.EXPLOSIONS.append([b, 16])
                                self.EXPLOSIONS.append([bullets_pos, 16])
                                self.bullets_destroy.append(b_p)

                if bullets_pos.get_name() in ["Red_fireball", "Bomb"]:
                    if self.PLAYER.detect_collision(bullets_pos):
                        stop = True
                        self.bullets_destroy.clear()
                        self.explosion_end.clear()
                        self.num_of_e = 0

            # collision with player

            if self.PLAYER.detect_collision(self.enemy_object):

                if [self.enemy_object, 16] in self.EXPLOSIONS:
                    self.EXPLOSIONS.remove([self.enemy_object, 16])

                stop = True
                self.bullets_destroy.clear()
                self.explosion_end.clear()
                self.num_of_e = 0

            if 0 <= self.enemy_object.y <= (4/6) * self.SCREEN_LENGTH:
                self.enemy_object.shoot()

        self.remove_enemies()
        return score, stop

    def blast(self):
        self.explosion_end = []

        for ex in range(len(self.EXPLOSIONS)):
            if self.EXPLOSIONS[ex][1] == 1:
                self.explosion_end.append(ex)

            else:
                self.EXPLOSIONS[ex][1] -= 1

        c = 0
        for i in self.explosion_end:
            self.EXPLOSIONS.pop(i - c)
            c += 1

    def draw(self, score, stop):
        self.score = score

        for exp in self.EXPLOSIONS:
            explosion_pic = pygame.image.load(os.path.join(self.EXPLO_PATH, str(exp[1]) + ".png"))
            self.SCREEN.blit(pygame.transform.scale(explosion_pic,
                                                    (int(exp[0].get_width()),
                                                     int(exp[0].get_height()))),
                             (int(exp[0].x),
                              int(exp[0].y)))

        if not stop:
            self.add_enemies()
            for en in self.ENEMIES:
                en.draw()








