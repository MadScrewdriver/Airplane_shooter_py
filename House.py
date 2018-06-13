from Settings import GlobalConstants
from Basic_Component import BasicComponent


class House(GlobalConstants, BasicComponent):

    def __init__(self, x, y):
        super().__init__(x, y, self.HOUSE_WIDTH, self.HOUSE_HEIGHT, self.HOUSE_PIC_PATH, self.SCREEN, "House", 0, 0)