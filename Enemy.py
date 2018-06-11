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
        self.stop = False

    def move_enemy(self):
        for e in range(len(self.ENEMIES)):
            enemy_pos = self.ENEMIES[e]

            if enemy_pos.y >= self.SCREEN_LENGTH - enemy_pos.get_height() - self.MARGIN * 3:
                self.enemy_destroy.clear()
                self.bullets_destroy.clear()
                self.explosion_end.clear()
                self.num_of_e = 0
                self.set_stop(True)
                return True

            enemy_pos.move()

        return False

    def tick(self):
        self.blast()
        return self.move_enemy()

    def spawn_pos(self):

        if self.score < 30:
            self.level_1()

        elif self.score < 110:
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
                        if b.get_name() == "Red_fireball" and bullets_pos.rectangle_collision(b):
                            if bul not in self.bullets_destroy and b_p not in self.bullets_destroy:
                                self.bullets_destroy.append(bul)
                                self.EXPLOSIONS.append([b, 16])
                                self.EXPLOSIONS.append([bullets_pos, 16])
                                self.bullets_destroy.append(b_p)

                if bullets_pos.get_name() == "Red_fireball":
                    if self.PLAYER.detect_collision(bullets_pos):
                        self.stop = True
                        self.bullets_destroy.clear()
                        self.explosion_end.clear()
                        self.num_of_e = 0

            # collision with player

            if self.PLAYER.detect_collision(self.enemy_object):

                if [self.enemy_object, 16] in self.EXPLOSIONS:
                    self.EXPLOSIONS.remove([self.enemy_object, 16])

                self.stop = True
                self.bullets_destroy.clear()
                self.explosion_end.clear()
                self.num_of_e = 0

            if self.enemy_object.y >= (3/4) * self.SPITFIRE_HEIGHT:
                self.enemy_object.shoot()

        self.remove_enemies()
        return score

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

    def set_stop(self, v):
        self.stop = v

    def draw(self, score):
        self.score = score

        for exp in self.EXPLOSIONS:
            explosion_pic = pygame.image.load(os.path.join(self.EXPLO_PATH, str(exp[1]) + ".png"))
            self.SCREEN.blit(pygame.transform.scale(explosion_pic,
                                                    (int(exp[0].get_width()),
                                                     int(exp[0].get_height()))),
                             (int(exp[0].x),
                              int(exp[0].y)))

        if not self.stop:
            self.add_enemies()
            for en in self.ENEMIES:
                en.draw()

        return self.stop







