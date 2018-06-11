from Settings import PlayerConstants
from Basic_Component import BasicComponent
from Mask import Mask


class Spitfire(BasicComponent, PlayerConstants):
    def __init__(self, x, y):
        self.x = x
        self.y = y
        super(PlayerConstants).__init__()
        super().__init__(self.x, self.y, self.SPITFIRE_WITH, self.SPITFIRE_HEIGHT,
                         self.PLAYER_PIC_PATHS, self.SCREEN, "Spitfire", 0, 0)

    def detect_collision(self, second_object):

        body = Mask(self.x + ((12 / 27) * self.SPITFIRE_WITH),
                    self.y,
                    self.SPITFIRE_WITH * (3 / 27),
                    self.SPITFIRE_HEIGHT)

        wings = Mask(self.x + ((1 / 27) * self.SPITFIRE_WITH),
                     self.y + ((8 / 21) * self.SPITFIRE_HEIGHT),
                     self.SPITFIRE_WITH - ((2 / 27) * self.SPITFIRE_WITH),
                     self.SPITFIRE_HEIGHT * (3 / 21))

        stabilizer = Mask(self.x + (10 / 27) * self.SPITFIRE_WITH,
                          self.y + ((18 / 21) * self.SPITFIRE_HEIGHT),
                          self.SPITFIRE_WITH * (7 / 27),
                          self.SPITFIRE_HEIGHT * (2 / 21))

        if (body.rectangle_collision(second_object) or wings.rectangle_collision(second_object) or
                stabilizer.rectangle_collision(second_object)) and \
                (second_object.detect_collision(body) or
                 second_object.detect_collision(wings) or
                 second_object.detect_collision(stabilizer)):

            return True

        return False
