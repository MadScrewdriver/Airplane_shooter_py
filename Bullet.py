from Basic_Component import BasicComponent
from Settings import BulletConstants


class Bullets(BulletConstants):
    def __init__(self):
        self.bull_end = 0

        super().__init__()

    def shoot(self):
        self.BULLETS.append(BasicComponent(self.PLAYER.x + (self.PLAYER.get_width() / 2 - self.BULLET_SIZE / 2),
                                           self.PLAYER.y,
                                           self.BULLET_SIZE,
                                           self.BULLET_SIZE,
                                           self.BULL_PIC_PATHS,
                                           self.SCREEN, "fireball"
                                           ))

    def tick(self):

        self.bull_end = 0
        for bull_pos in range(len(self.BULLETS)):
            self.BULLETS[bull_pos].y += self.BULLET_SPEED

            if self.BULLETS[bull_pos].y < self.MARGIN / 2:
                self.bull_end += 1

        [self.BULLETS.pop(0) for _ in range(self.bull_end)]

    def draw(self):
        for bull_object in self.BULLETS:
            bull_object.draw(0)
