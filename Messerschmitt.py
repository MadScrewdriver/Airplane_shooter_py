from Basic_Component import BasicComponent
from Settings import MesserschmittConstants


class Messerschmitt(BasicComponent, MesserschmittConstants):
    def __init__(self, x, y):
        self.x = x
        self.y = y
        super(MesserschmittConstants).__init__()
        super().__init__(self.x, self.y, self.ENEMY_WITH, self.ENEMY_HEIGHT,
                         self.ENEMY_PIC_PATHS, self.SCREEN, "Messerschmitt")

    def detect_collision(self, second_object):
        body = BasicComponent(self.enemy_object.x + ((12 / 27) * self.ENEMY_WITH),
                              self.enemy_object.y,
                              self.ENEMY_WITH * (3 / 27),
                              self.ENEMY_HEIGHT,
                              [],
                              self.SCREEN, "body")

        wings = BasicComponent(self.enemy_object.x,
                               self.enemy_object.y + ((8 / 21) * self.ENEMY_WITH),
                               self.ENEMY_WITH,
                               self.ENEMY_HEIGHT * (3 / 21),
                               [],
                               self.SCREEN, "wings")

        stabilizer = BasicComponent(self.enemy_object.x + (10 / 27) * self.ENEMY_WITH,
                                    self.enemy_object.y,
                                    self.ENEMY_WITH * (7 / 27),
                                    self.ENEMY_HEIGHT * (2 / 21),
                                    [],
                                    self.SCREEN, "stabilizer")

        if super().detect_collision(body) or super().detect_collision(wings) or \
                super().detect_collision(stabilizer):
            return True
        else:
            return False
