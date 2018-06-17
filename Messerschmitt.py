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

        super().__init__(self.x, self.y, self.MESSERSCHMITT_WIDTH, self.MESSERSCHMITT_HEIGHT,
                         self.ENEMY_PIC_PATHS, self.SCREEN, "Messerschmitt", 0, self.MESSERSCHMITT_SPEED)

    def shoot(self):

        if time.time() - self.shoot_t >= self.diff:
            self.BULLETS.append(RedFireball(int((self.x + self.get_width() / 2) - self.BULLET_WIDTH / 2),
                                            int(self.y + self.MESSERSCHMITT_HEIGHT)))
            self.shoot_t = time.time()
            self.diff = uniform(2, 4)

    def detect_collision(self, second_object):
        body = Mask(self.x + ((16 / 38) * self.MESSERSCHMITT_WIDTH),
                    self.y,
                    self.MESSERSCHMITT_WIDTH * (6 / 38),
                    self.MESSERSCHMITT_HEIGHT)

        wings = Mask(self.x,
                     self.y + ((19 / 35) * self.MESSERSCHMITT_HEIGHT),
                     self.MESSERSCHMITT_WIDTH,
                     self.MESSERSCHMITT_HEIGHT * (6 / 35))

        stabilizer = Mask(self.x + (13 / 38) * self.MESSERSCHMITT_WIDTH,
                          self.y,
                          self.MESSERSCHMITT_WIDTH * (12 / 38),
                          self.MESSERSCHMITT_HEIGHT * (3 / 35))

        if body.rectangle_collision(second_object) or wings.rectangle_collision(second_object) or \
                stabilizer.rectangle_collision(second_object):
            return True

        return False
