from Basic_Component import BasicComponent
from Settings import GlobalConstants


class Bomb(BasicComponent, GlobalConstants):
    def __init__(self, x, y):
        self.x = x
        self.y = y
        super().__init__(self.x, self.y, self.BOMB_WIDTH, self.BOMB_HEIGHT,
                         self.B_BULL_PIC_PATHS, self.SCREEN, "Bomb", 0, self.BOMB_SPEED)

    def detect_collision(self, second_object):
        return True
