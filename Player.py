import pygame
from Basic_Component import BasicComponent


class Rocket(object):

    def __init__(self, game):
        pygame.init()
        self.game = game
        self.size = self.game.screen.get_size()
        self.speed = self.size[0] / 120
        self.margin = game.margin
        self.touch_r = False
        self.touch_l = False
        self.touch_u = False
        self.touch_d = False
        self.last_matrix = self.size
        self.pressed = pygame.key.get_pressed()
        self.right = self.pressed[pygame.K_RIGHT]
        self.left = self.pressed[pygame.K_LEFT]
        self.up = self.pressed[pygame.K_UP]
        self.down = self.pressed[pygame.K_DOWN]
        self.player = BasicComponent(self.size[0] / 2 - (self.size[0] / 3.90) / 2, self.size[1] * (5/6),
                                     self.size[0] / 3.90, self.size[0] / 5.27,
                                     ["ap1.png", "ap2.png", "ap3.png"], self.game.screen)

        print(self.player.get_height())
        print(self.player.get_width())

    def update(self):
        self.size = self.game.screen.get_size()
        self.speed = self.size[0] / 120
        self.pressed = pygame.key.get_pressed()
        self.right = self.pressed[pygame.K_RIGHT]
        self.left = self.pressed[pygame.K_LEFT]
        self.up = self.pressed[pygame.K_UP]
        self.down = self.pressed[pygame.K_DOWN]

        if self.size[0] != self.last_matrix:
            self.player.x = (self.player.x / self.last_matrix[0]) * self.size[0]
            self.player.y = (self.player.y / self.last_matrix[1]) * self.size[1]

        self.last_matrix = self.size

    def tick(self):

        self.touch_l = self.player.x <= self.margin / 2
        self.touch_r = self.player.x + self.player.get_width() >= self.size[0] - (self.margin / 2)
        self.touch_u = self.player.y <= self.size[1] * (1 / 2)
        self.touch_d = self.player.y >= self.size[1] - self.margin - self.player.get_height()

        # Input
        if self.right and not self.touch_r:
            self.player.x += self.speed

        if self.left and not self.touch_l:
            self.player.x -= self.speed

        if self.up and not self.touch_u:
            self.player.y -= self.speed

        if self.down and not self.touch_d:
            self.player.y += self.speed

    def draw(self):
        self.update()

        if self.left and not self.right:
            self.player.draw(1)

        elif self.right and not self.left:
            self.player.draw(2)

        else:
            self.player.draw()
