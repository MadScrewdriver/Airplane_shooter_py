from Basic_Component import BasicComponent
from Settings import MaskConstants


class Mask(BasicComponent, MaskConstants):
    def __init__(self, x, y, width, height, m="Mask"):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        super(MaskConstants).__init__()
        super().__init__(self.x, self.y, self.width, self.height,
                         [], self.SCREEN, m, 0, 0)

    def detect_collision(self, second_object):

        if self.rectangle_collision(second_object):
            return True

        return False
