from Settings import GlobalConstants
from Basic_Component import BasicComponent


class Clouds(GlobalConstants):

    def __init__(self):
        super().__init__()
        self.clouds_1 = BasicComponent(0, -self.SCREEN_LENGTH * 1, self.SCREEN_WIDTH, self.SCREEN_LENGTH * 2,
                                       self.CLOUDS_PIC_PATHS, self.SCREEN, "Clouds", 0, self.CLOUDS_SPEED)

        self.clouds_2 = BasicComponent(0, 0, self.SCREEN_WIDTH, self.SCREEN_LENGTH * 2,
                                       self.CLOUDS_PIC_PATHS, self.SCREEN, "Clouds", 0, self.CLOUDS_SPEED)

        self.two = False

    def tick(self):
        self.clouds_1.move()

        if self.SCREEN_LENGTH >= self.clouds_1.y >= 0:
            self.two = True
            self.clouds_2.y = (self.clouds_1.y - self.SCREEN_LENGTH * 2)

        if self.clouds_1.y > self.SCREEN_LENGTH and self.two:
            self.two = False
            self.clouds_1.y = self.clouds_2.y

    def draw(self):

        if self.two:
            self.clouds_2.draw(0)

        self.clouds_1.draw(0)
