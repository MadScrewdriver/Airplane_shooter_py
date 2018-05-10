import pygame
from pygame.math import Vector2


class Bullets(object):
    def __init__(self, game, player):
        pygame.init()
        self.game = game
        self.size = self.game.screen.get_size()
        self.b_s = self.size[0] / 60
        self.bullets = []
        self.player = player
        self.pos = Vector2(self.player.pos.x + self.player.player_size.x / 2 - 4, self.player.pos.y)
        self.bull_end = 0
        self.bull_size = self.size[0] / 400
        self.bullet_speed = Vector2(0, -self.b_s)
        self.bullet_size = 15

    def update(self):
        self.size = self.game.screen.get_size()
        self.b_s = self.size[0] / 80
        self.bull_size = self.size[0] / 256
        self.bullet_speed = Vector2(0, -self.b_s)
        self.pos = Vector2(self.player.pos.x + self.player.player_size.x / 2 - (self.bullet_size / 2),
                           self.player.pos.y)

    def shoot(self):
        self.bullets.append(Vector2(self.pos.x, self.pos.y))

    def tick(self):
        self.update()

        self.bull_end = 0
        for bull_pos in range(len(self.bullets)):
            self.bullets[bull_pos] += self.bullet_speed

            if self.bullets[bull_pos].y < self.player.margin / 2:
                self.bull_end += 1

        [self.bullets.pop(0) for _ in range(self.bull_end)]

    def draw(self):
        self.update()

        for bull_pos in self.bullets:
            self.game.screen.blit(pygame.transform.scale(pygame.image.load("bullet.png"),
                                                         (self.bullet_size, self.bullet_size)), bull_pos)
