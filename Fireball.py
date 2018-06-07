from Basic_Component import BasicComponent
from Settings import FireballConstants


class Fireball(BasicComponent, FireballConstants):
    def __init__(self, x, y):
        self.x = x
        self.y = y
        super(FireballConstants).__init__()
        super().__init__(self.x, self.y, self.BULLET_SIZE, self.BULLET_SIZE,
                         self.Fire_PIC_PATHS, self.SCREEN, "Fireball")

    def detect_collision(self, second_object):

        if self.rectangle_collision(second_object) and second_object.detect_collision(self):
            return True

        return False
