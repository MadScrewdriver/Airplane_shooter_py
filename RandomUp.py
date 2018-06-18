from Basic_Component import BasicComponent
from Settings import GlobalConstants


class RandomUp(BasicComponent, GlobalConstants):
    def __init__(self, x, y):
        self.x = x
        self.y = y
        super().__init__(x, y, 50, 50, self.UP_CA_PIC_PATHS, self.SCREEN, "Upgrade", 0, 8)

    def detect_collision(self, second_object):

        if self.rectangle_collision(second_object):
            return True

        return False
