import pygame
from Hearts import Heart
from Settings import BackgroundConstants
from Basic_Component import BasicComponent


class Background(BackgroundConstants):

    def __init__(self):
        super().__init__()
        self.background_1 = BasicComponent(0, -self.SCREEN_LENGTH * 2, self.SCREEN_WITH,
                                           self.SCREEN_LENGTH * 3,
                                           self.BACK_PIC_PATHS,
                                           self.SCREEN, "background", 0, self.BG_SPEED)

        self.background_2 = BasicComponent(0, 0, self.SCREEN_WITH, self.SCREEN_LENGTH * 3,
                                           self.BACK_PIC_PATHS, self.SCREEN, "background", 0, self.BG_SPEED)

        self.heart_1 = Heart(self.SCREEN_WITH - self.SCREEN_WITH * 0.02 - self.HEART_WITH,
                             self.SCREEN_LENGTH * 0.94)

        self.heart_2 = Heart(self.SCREEN_WITH - self.SCREEN_WITH * 0.04 - self.HEART_WITH * 2,
                             self.SCREEN_LENGTH * 0.94)

        self.heart_3 = Heart(self.SCREEN_WITH - self.SCREEN_WITH * 0.06 - self.HEART_WITH * 3,
                             self.SCREEN_LENGTH * 0.94)

        self.two = False
        self.score_font = pygame.font.Font(self.PIX_FONT_PATH, 45)

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
        self.SCREEN.blit(score_test, (self.SCREEN_WITH * 0.02, self.SCREEN_LENGTH * 0.94))

    def draw_lives(self, lives=3, stop=False):
        if (lives == 1 and not stop) or lives > 1:
            self.heart_1.draw()

        if (lives == 2 and not stop) or lives > 2:
            self.heart_2.draw()

        if (lives == 3 and not stop) or lives > 3:
            self.heart_3.draw()


