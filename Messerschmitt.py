from Mask import Mask
from Settings import MesserschmittConstants
from Basic_Component import BasicComponent


class Messerschmitt(BasicComponent, MesserschmittConstants):
    def __init__(self, x, y):
        self.x = x
        self.y = y
        super(MesserschmittConstants).__init__()
        super().__init__(self.x, self.y, self.ENEMY_WITH, self.ENEMY_HEIGHT,
                                       self.ENEMY_PIC_PATHS, self.SCREEN, "Messerschmitt")

    def detect_collision(self, second_object):
        body = Mask(self.x + ((12 / 27) * self.ENEMY_WITH),
                    self.y,
                    self.ENEMY_WITH * (3 / 27),
                    self.ENEMY_HEIGHT)

        wings = Mask(self.x,
                     self.y + ((8 / 21) * self.ENEMY_WITH),
                     self.ENEMY_WITH,
                     self.ENEMY_HEIGHT * (3 / 21))

        stabilizer = Mask(self.x + (10 / 27) * self.ENEMY_WITH,
                          self.y,
                          self.ENEMY_WITH * (7 / 27),
                          self.ENEMY_HEIGHT * (2 / 21))

        if body.rectangle_collision(second_object) or wings.rectangle_collision(second_object) or \
                stabilizer.rectangle_collision(second_object):
            return True
        else:
            return False
