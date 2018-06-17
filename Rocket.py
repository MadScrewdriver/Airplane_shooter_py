from Mask import Mask
from Basic_Component import BasicComponent
from Settings import GlobalConstants


class Rocket(BasicComponent, GlobalConstants):

    def __init__(self, x, y):
        self.x = x
        self.y = y
        super().__init__(self.x, self.y, self.ROCKET_WIDTH, self.ROCKET_HEIGHT,
                         self.ROC_PIC_PATH, self.SCREEN, "V_2", 0, self.ROCKET_SPEED)

    def detect_collision(self, second_object):
        body = Mask(self.x + ((4 / 13) * self.ROCKET_WIDTH),
                    self.y,
                    self.ROCKET_WIDTH * (5 / 13),
                    self.ROCKET_HEIGHT)

        if body.rectangle_collision(second_object):
            return True

        return True
