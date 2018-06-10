from Mask import Mask
from Basic_Component import BasicComponent
from Settings import GlobalConstants


class Messerschmitt(BasicComponent, GlobalConstants):

    def __init__(self, x, y):
        self.x = x
        self.y = y
        super().__init__(self.x, self.y, self.MESSERSCHMITT_WITH, self.MESSERSCHMITT_HEIGHT,
                         self.ENEMY_PIC_PATHS, self.SCREEN, "Messerschmitt", 0, self.MESSERSCHMITT_SPEED)

    def detect_collision(self, second_object):
        body = Mask(self.x + ((12 / 27) * self.MESSERSCHMITT_WITH),
                    self.y,
                    self.MESSERSCHMITT_WITH * (3 / 27),
                    self.MESSERSCHMITT_HEIGHT)

        wings = Mask(self.x,
                     self.y + ((10 / 21) * self.MESSERSCHMITT_HEIGHT),
                     self.MESSERSCHMITT_WITH,
                     self.MESSERSCHMITT_HEIGHT * (4 / 21))

        stabilizer = Mask(self.x + (10 / 27) * self.MESSERSCHMITT_WITH,
                          self.y,
                          self.MESSERSCHMITT_WITH * (7 / 27),
                          self.MESSERSCHMITT_HEIGHT * (2 / 21))

        if body.rectangle_collision(second_object) or wings.rectangle_collision(second_object) or \
                stabilizer.rectangle_collision(second_object):
            return True

        return False
