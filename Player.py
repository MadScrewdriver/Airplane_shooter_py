import pygame
from settings import RocketConstants


class Rocket(RocketConstants):

    def __init__(self):
        self.touch_r = False
        self.touch_l = False
        self.touch_u = False
        self.touch_d = False
        self.pressed = pygame.key.get_pressed()
        self.right = self.pressed[pygame.K_RIGHT]
        self.left = self.pressed[pygame.K_LEFT]
        self.up = self.pressed[pygame.K_UP]
        self.down = self.pressed[pygame.K_DOWN]

        super().__init__()

    def update(self):
        self.pressed = pygame.key.get_pressed()
        self.right = self.pressed[pygame.K_RIGHT]
        self.left = self.pressed[pygame.K_LEFT]
        self.up = self.pressed[pygame.K_UP]
        self.down = self.pressed[pygame.K_DOWN]

    def tick(self):

        self.touch_l = self.PLAYER.x <= self.MARGIN / 2
        self.touch_r = self.PLAYER.x + self.PLAYER.get_width() >= self.SCREEN_WITH - (self.MARGIN / 2)
        self.touch_u = self.PLAYER.y <= self.SCREEN_LENGTH * (1 / 2)
        self.touch_d = self.PLAYER.y >= self.SCREEN_LENGTH - self.MARGIN - self.PLAYER.get_height()

        # Input
        if self.right and not self.touch_r:
            self.PLAYER.x += self.SPEED

        if self.left and not self.touch_l:
            self.PLAYER.x -= self.SPEED

        if self.up and not self.touch_u:
            self.PLAYER.y -= self.SPEED

        if self.down and not self.touch_d:
            self.PLAYER.y += self.SPEED

    def draw(self):
        self.update()

        if self.left and not self.right:
            self.PLAYER.draw(1)

        elif self.right and not self.left:
            self.PLAYER.draw(2)

        else:
            self.PLAYER.draw()
