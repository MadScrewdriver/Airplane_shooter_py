from Fireball import Fireball
from Settings import GlobalConstants


class Bullets(GlobalConstants):
    def __init__(self, player):
        self.PLAYER = player
        self.bull_end = []

        super().__init__()

    def shoot(self):
        self.BULLETS.append(Fireball(self.PLAYER.x + (self.PLAYER.get_width() / 2 - self.BULLET_SIZE / 2),
                                     self.PLAYER.y))

    def tick(self):

        self.bull_end.clear()
        for bull_pos in range(len(self.BULLETS)):
            self.BULLETS[bull_pos].move()

            if (self.BULLETS[bull_pos].y < self.MARGIN / 2 and self.BULLETS[bull_pos].get_name() == "Fireball") or \
                    (self.BULLETS[bull_pos].get_name() == "Red_fireball" and self.BULLETS[bull_pos].y >=
                     self.SCREEN_LENGTH - self.MARGIN):
                self.bull_end.append(bull_pos)

        j = 0
        for b in sorted(self.bull_end):
            self.BULLETS.pop(b - j)
            j += 1

    def draw(self):
        for bull_object in self.BULLETS:
            bull_object.draw(0)
