import time
from random import *
from Red_fireball import RedFireball
from Mask import Mask
from Basic_Component import BasicComponent
from Settings import GlobalConstants


class Messerschmitt(BasicComponent, GlobalConstants):

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.shoot_t = 0
        self.diff = uniform(0.5, 3)

        super().__init__(self.x, self.y, self.MESSERSCHMITT_WITH, self.MESSERSCHMITT_HEIGHT,
                         self.ENEMY_PIC_PATHS, self.SCREEN, "Messerschmitt", 0, self.MESSERSCHMITT_SPEED)

    def shoot(self):

        if time.time() - self.shoot_t >= self.diff:
            self.BULLETS.append(RedFireball(int((self.x + self.get_width() / 2) - self.BULLET_SIZE / 2),
                                            int(self.y + self.MESSERSCHMITT_HEIGHT)))
            self.shoot_t = time.time()
            self.diff = uniform(2, 4)

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
