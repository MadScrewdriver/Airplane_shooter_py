from Basic_Component import BasicComponent
from Settings import GlobalConstants


class Fireball(BasicComponent, GlobalConstants):
    def __init__(self, x, y):
        self.x = x
        self.y = y
        super().__init__(self.x, self.y, self.BULLET_SIZE, self.BULLET_SIZE,
                                             self.Fire_PIC_PATHS, self.SCREEN, "Fireball", 0, -self.BULLET_SPEED)

    def detect_collision(self, second_object):

        if self.rectangle_collision(second_object) and second_object.detect_collision(self):
            return True

        return False
