import pygame


class Background(object):

    def __init__(self, game):
        self.game = game
        self.screen = game.screen
        self.background_1 = pygame.image.load("Bg.png")
        self.background_2 = pygame.image.load("Bg.png")
        self.screen_with = game.screen_with
        self.screen_length = game.screen_length
        self.bg_speed = 2
        self.bg_1_pos = -self.screen_length * 2
        self.bg_2_pos = 0
        self.two = False

    def tick(self):
        self.bg_1_pos += self.bg_speed

        if self.screen_length >= self.bg_1_pos >= 0:
            self.two = True
            self.bg_2_pos = (self.bg_1_pos - self.screen_length * 3)

        if self.bg_1_pos > self.screen_length and self.two:
            self.two = False
            self.bg_1_pos = self.bg_2_pos

    def draw(self):

        if self.two:
            self.screen.blit(pygame.transform.scale(self.background_2, (self.screen_with, self.screen_length * 3)),
                             (0, self.bg_2_pos))

        self.screen.blit(pygame.transform.scale(self.background_1, (self.screen_with, self.screen_length * 3)),
                         (0, self.bg_1_pos))

