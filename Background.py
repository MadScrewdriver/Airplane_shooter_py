import pygame
from Hearts import Heart
from Settings import BackgroundConstants
from Basic_Component import BasicComponent


class Background(BackgroundConstants):

    def __init__(self, l=3):
        super().__init__()
        self.background_1 = BasicComponent(0, -self.SCREEN_LENGTH * 2, self.SCREEN_WITH,
                                           self.SCREEN_LENGTH * 3,
                                           self.BACK_PIC_PATHS,
                                           self.SCREEN, "background", 0, self.BG_SPEED)

        self.background_2 = BasicComponent(0, 0, self.SCREEN_WITH, self.SCREEN_LENGTH * 3,
                                           self.BACK_PIC_PATHS, self.SCREEN, "background", 0, self.BG_SPEED)

        for h in range(1, l + 1):
            self.LIVES.append(Heart(self.SCREEN_WITH - (self.SCREEN_WITH * (0.02 * h)) - (self.HEART_WITH * h),
                                    self.SCREEN_LENGTH * 0.94))

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
        if lives > len(self.LIVES):
            for add in range(1, lives - len(self.LIVES) + 1):
                self.LIVES.append(Heart(self.SCREEN_WITH - (self.SCREEN_WITH * (0.02 * len(self.LIVES))) -
                                        (self.HEART_WITH * len(self.LIVES)), self.SCREEN_LENGTH * 0.94))

        for l in range(1, len(self.LIVES) + 1):
            live = self.LIVES[l - 1]
            if (lives == l and not stop) or lives > l:
                live.draw()



