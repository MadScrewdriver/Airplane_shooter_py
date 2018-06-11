from Settings import GlobalConstants
from Basic_Component import BasicComponent


class Heart(GlobalConstants, BasicComponent):

    def __init__(self, x, y):
        super().__init__(x, y, self.HEART_WITH, self.HEART_HEIGHT, self.HEART_PIC_PATH, self.SCREEN, "Heart", 0, 0)