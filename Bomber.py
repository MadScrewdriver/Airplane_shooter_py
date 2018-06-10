from Basic_Component import BasicComponent
from Settings import GlobalConstants
from Mask import Mask


class Bomber(BasicComponent, GlobalConstants):
    def __init__(self, x, y):
        self.x = x
        self.y = y
        super().__init__(self.x, self.y, self.BOMBER_WITH, self.BOMBER_HEIGHT,
                         self.BOM_PIC_PATH, self.SCREEN, "Bomber", 0, self.BOMBER_SPEED)

    def detect_collision(self, second_object):
        body = Mask(self.x + ((13 / 29) * self.BOMBER_WITH),
                    self.y,
                    self.BOMBER_WITH * (3 / 29),
                    self.BOMBER_HEIGHT)

        wings = Mask(self.x,
                     self.y + ((11 / 23) * self.BOMBER_HEIGHT),
                     self.BOMBER_WITH,
                     self.BOMBER_HEIGHT * (4 / 23))

        stabilizer = Mask(self.x + (9 / 29) * self.BOMBER_WITH,
                          self.y,
                          self.BOMBER_WITH * (11 / 29),
                          self.BOMBER_HEIGHT * (3 / 23))

        if body.rectangle_collision(second_object) or wings.rectangle_collision(second_object) or \
                stabilizer.rectangle_collision(second_object):
            return True
        else:
            return False

