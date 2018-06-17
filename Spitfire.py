from Settings import PlayerConstants
from Basic_Component import BasicComponent
from Mask import Mask


class Spitfire(BasicComponent, PlayerConstants):
    def __init__(self, x, y):
        self.x = x
        self.y = y
        super(PlayerConstants).__init__()
        super().__init__(self.x, self.y, self.SPITFIRE_WIDTH, self.SPITFIRE_HEIGHT,
                         self.PLAYER_PIC_PATHS, self.SCREEN, "Spitfire", 0, 0)

    def detect_collision(self, second_object):

        body = Mask(self.x + ((17 / 40) * self.SPITFIRE_WIDTH),
                    self.y,
                    self.SPITFIRE_WIDTH * (6 / 40),
                    self.SPITFIRE_HEIGHT, "B")

        wings = Mask(self.x + ((2 / 40) * self.SPITFIRE_WIDTH),
                     self.y + ((10 / 35) * self.SPITFIRE_HEIGHT),
                     self.SPITFIRE_WIDTH - ((4 / 40) * self.SPITFIRE_WIDTH),
                     self.SPITFIRE_HEIGHT * (9 / 35), "W")

        stabilizer = Mask(self.x + (14 / 40) * self.SPITFIRE_WIDTH,
                          self.y + ((32 / 35) * self.SPITFIRE_HEIGHT),
                          self.SPITFIRE_WIDTH * (12 / 40),
                          self.SPITFIRE_HEIGHT * (3 / 35), "S")

        if (body.rectangle_collision(second_object) or wings.rectangle_collision(second_object) or
                stabilizer.rectangle_collision(second_object)) and \
                (second_object.detect_collision(body) or
                 second_object.detect_collision(wings) or
                 second_object.detect_collision(stabilizer)):

            return True

        return False