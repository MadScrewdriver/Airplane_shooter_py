from Basic_Component import BasicComponent
from Settings import BomberConstants


class Bomber(BasicComponent, BomberConstants):
    def __init__(self, x, y):
        self.x = x
        self.y = y
        super(BomberConstants).__init__()
        super().__init__(self.x, self.y, self.BOMBER_WITH, self.BOMBER_HEIGHT,
                         self.BOM_PIC_PATH, self.SCREEN, "Bomber")
