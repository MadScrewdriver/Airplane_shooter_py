from Basic_Component import BasicComponent
from Settings import GlobalConstants


class RedFireball(BasicComponent, GlobalConstants):
    def __init__(self, x, y):
        self.x = x
        self.y = y
        super().__init__(self.x, self.y, self.BULLET_SIZE, self.BULLET_SIZE,
                         self.R_BULL_PIC_PATHS, self.SCREEN, "Red_fireball", 0, self.BULLET_SPEED)

    def detect_collision(self, second_object):

        if self.rectangle_collision(second_object):
            return True

        return False