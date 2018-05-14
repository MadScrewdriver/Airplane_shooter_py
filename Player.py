import pygame
from pygame.math import Vector2


class Rocket(object):

    def __init__(self, game):
        pygame.init()
        self.game = game
        self.size = self.game.screen.get_size()
        self.speed = self.size[0] / 120
        self.vel_l_r = Vector2(self.speed, 0)
        self.vel_u_d = Vector2(0, self.speed)
        self.touch_r = False
        self.touch_l = False
        self.touch_u = False
        self.touch_d = False
        self.margin = self.size[0] / 20
        self.player_size = Vector2(self.size[0] / 3.90, self.size[0] / 5.27)
        print(self.player_size)
        self.pos = Vector2(self.size[0] / 2 - self.player_size.x / 2, self.size[1] * (5/6))
        self.last_matrix = self.size
        self.player = pygame.image.load("ap1.png")
        self.player_left = pygame.image.load("ap2.png")
        self.player_right = pygame.image.load("ap3.png")
        self.pressed = pygame.key.get_pressed()
        self.right = self.pressed[pygame.K_RIGHT]
        self.left = self.pressed[pygame.K_LEFT]
        self.up = self.pressed[pygame.K_UP]
        self.down = self.pressed[pygame.K_DOWN]
        self.t = self.left
        self.j = self.right
        self.last_press_side = True
        self.last_press_top = True
        self.c = False
        self.o = True
        self.b = False

    def update(self):
        self.size = self.game.screen.get_size()
        self.speed = self.size[0] / 120
        self.vel_l_r = Vector2(self.speed, 0)
        self.margin = self.size[0] / 20
        self.player_size = Vector2(self.size[0] / 3.90, self.size[0] / 5.27)
        self.pressed = pygame.key.get_pressed()
        self.t = self.left
        self.j = self.right
        self.right = self.pressed[pygame.K_RIGHT]
        self.left = self.pressed[pygame.K_LEFT]
        self.up = self.pressed[pygame.K_UP]
        self.down = self.pressed[pygame.K_DOWN]

        if self.right and self.j and self.left and not self.t:
            self.last_press_side = False

        if (not self.last_press_side and not self.right) or not self.left:
            self.last_press_side = True

        # if self.right and self.left and self.touch_r and not self.b:
        #     self.o = False
        #
        # if not self.o and not self.t and self.left:
        #     self.o = True
        #     self.b = True

        if self.size[0] != self.last_matrix:
            self.pos.x = (self.pos.x / self.last_matrix[0]) * self.size[0]
            self.pos.y = (self.pos.y / self.last_matrix[1]) * self.size[1]

        self.last_matrix = self.size

    def tick(self):

        self.touch_l = self.pos.x <= self.margin / 2
        self.touch_r = self.pos.x + self.player_size.x >= self.size[0] - (self.margin / 2)
        self.touch_u = self.pos.y <= self.size[1] * (1 / 2)
        self.touch_d = self.pos.y >= self.size[1] - self.margin - self.player_size[1]

        if self.touch_u and self.down:
            self.last_press_top = False

        elif not self.down:
            self.last_press_top = True

        # Input
        if self.right and not self.touch_r and self.last_press_side:
            self.pos += self.vel_l_r
            self.b = False

        elif self.left and not self.touch_l:
            self.pos -= self.vel_l_r
            self.b = False

        if self.up and not self.touch_u and self.last_press_top:
            self.pos -= self.vel_u_d

        elif self.down and not self.touch_d:
            self.pos += self.vel_u_d

    def draw(self):
        self.update()

        if self.left:
            self.game.screen.blit(pygame.transform.scale(self.player_left,
                                                         (int(self.player_size.x),
                                                          int(self.player_size.y))),
                                                         (int(self.pos.x),
                                                          int(self.pos.y)))
        elif self.right:
            self.game.screen.blit(pygame.transform.scale(self.player_right,
                                                         (int(self.player_size.x),
                                                          int(self.player_size.y))),
                                                         (int(self.pos.x),
                                                          int(self.pos.y)))
        else:
            self.game.screen.blit(pygame.transform.scale(self.player,
                                                         (int(self.player_size.x),
                                                          int(self.player_size.y))),
                                                        (int(self.pos.x),
                                                         int(self.pos.y)))
