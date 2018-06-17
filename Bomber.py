import time
from random import *
from Bomb import Bomb
from Basic_Component import BasicComponent
from Settings import GlobalConstants
from Mask import Mask


class Bomber(BasicComponent, GlobalConstants):
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.shoot_t = 0
        self.diff = uniform(3, 5)

        super().__init__(self.x, self.y, self.BOMBER_WIDTH, self.BOMBER_HEIGHT,
                         self.BOM_PIC_PATH, self.SCREEN, "Bomber", 0, self.BOMBER_SPEED)

    def shoot(self):

        if time.time() - self.shoot_t >= self.diff:
            self.BULLETS.append(Bomb(int(self.x + self.get_width() * (5 / 27)),
                                     int(self.y + self.BOMBER_HEIGHT / 2)))

            self.BULLETS.append(Bomb(int(self.x + self.get_width() * (20 / 27)),
                                     int(self.y + self.BOMBER_HEIGHT / 2)))
            self.shoot_t = time.time()
            self.diff = uniform(3, 5)

    def detect_collision(self, second_object):
        body = Mask(self.x + ((26 / 61) * self.BOMBER_WIDTH),
                    self.y,
                    self.BOMBER_WIDTH * (9 / 61),
                    self.BOMBER_HEIGHT)

        wings = Mask(self.x,
                     self.y + ((24 / 48) * self.BOMBER_HEIGHT),
                     self.BOMBER_WIDTH,
                     self.BOMBER_HEIGHT * (11 / 61))

        stabilizer = Mask(self.x + (21 / 61) * self.BOMBER_WIDTH,
                          self.y,
                          self.BOMBER_WIDTH * (19 / 61),
                          self.BOMBER_HEIGHT * (6 / 48))

        if body.rectangle_collision(second_object) or wings.rectangle_collision(second_object) or \
                stabilizer.rectangle_collision(second_object):
            return True
        else:
            return False

