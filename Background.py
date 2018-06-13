import pygame
from Hearts import Heart
from House import House
from Settings import BackgroundConstants
from Basic_Component import BasicComponent


class Background(BackgroundConstants):

    def __init__(self):
        super().__init__()
        self.background_1 = BasicComponent(0, -self.SCREEN_LENGTH * 2, self.SCREEN_WIDTH,
                                           self.SCREEN_LENGTH * 3,
                                           self.BACK_PIC_PATHS,
                                           self.SCREEN, "background", 0, self.BG_SPEED)

        self.background_2 = BasicComponent(0, 0, self.SCREEN_WIDTH, self.SCREEN_LENGTH * 3,
                                           self.BACK_PIC_PATHS, self.SCREEN, "background", 0, self.BG_SPEED)

        self.two = False
        self.score_font = pygame.font.Font(self.PIX_FONT_PATH, self.FONT_SIZE)

    def tick(self):
        self.background_1.move()

        if self.SCREEN_LENGTH >= self.background_1.y >= 0:
            self.two = True
            self.background_2.y = (self.background_1.y - self.SCREEN_LENGTH * 3)

        if self.background_1.y > self.SCREEN_LENGTH and self.two:
            self.two = False
            self.background_1.y = self.background_2.y

    def draw(self, score):

        if self.two:
            self.background_2.draw(0)

        self.background_1.draw(0)

        score_test = self.score_font.render(str(score), 1, (255, 255, 255))
        self.SCREEN.blit(score_test, (self.MARGIN, self.MARGIN))

    def draw_lives(self, lives=3, stop=False):
        if lives > len(self.LIVES):
            for add in range(1, lives - len(self.LIVES) + 1):
                self.LIVES.append(Heart(self.SCREEN_WIDTH -
                                        (self.SCREEN_WIDTH * (self.GAP_BETWEEN_H_H * (len(self.LIVES) + 1))) -
                                        (self.HEART_WIDTH * (len(self.LIVES) + 1)), self.SCREEN_LENGTH * 0.94))

        for l in range(1, len(self.LIVES) + 1):
            live = self.LIVES[l - 1]
            if (lives == l and not stop) or lives > l:
                live.draw()

    def draw_houses(self, houses=3, stop=False):
        if houses > len(self.HOUSES):
            for add in range(1, houses - len(self.HOUSES) + 1):
                self.HOUSES.append(House((self.SCREEN_WIDTH * (self.GAP_BETWEEN_H_H * (len(self.HOUSES) + 1))) +
                                         (self.HEART_WIDTH * len(self.HOUSES)), self.SCREEN_LENGTH * 0.94))

        for l in range(1, len(self.HOUSES) + 1):
            live = self.HOUSES[l - 1]
            if (houses == l and not stop) or houses > l:
                live.draw()



