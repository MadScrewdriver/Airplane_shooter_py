import pygame
from settings import BackgroundConstants
from Basic_Component import BasicComponent


class Background(BackgroundConstants):

    def __init__(self):
        self.background_1 = BasicComponent(0, -self.SCREEN_LENGTH * 2, self.SCREEN_WITH,
                                           self.SCREEN_LENGTH * 3,
                                           ["Pictures/Background/background.png" for _ in range(2)],
                                           self.SCREEN)

        self.background_2 = BasicComponent(0, 0, self.SCREEN_WITH, self.SCREEN_LENGTH * 3,
                                           ["Pictures/Background/background.png" for _ in range(2)], self.SCREEN)
        self.two = False
        self.score_font = pygame.font.Font('Pixel_font.ttf', 45)

        super().__init__()

    def tick(self):
        self.background_1.y += self.BG_SPEED

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
        # pygame.draw.rect(self.SCREEN, (0, 0, 0), pygame.Rect((0, self.SCREEN_LENGTH * 0.93),
        #                                                      (self.SCREEN_WITH, self.SCREEN_LENGTH * 0.07)))

        score_test = self.score_font.render(str(score), 1, (255, 255, 255))
        self.SCREEN.blit(score_test, (self.SCREEN_WITH * 0.02, self.SCREEN_LENGTH * 0.94))

