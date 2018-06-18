import pygame
from random import uniform
from Settings import GlobalConstants
from Basic_Component import BasicComponent


class Clouds(GlobalConstants):

    def __init__(self):
        self.CLOUDS.append(
            BasicComponent(int(uniform(-150, self.SCREEN_WIDTH - 150)), -173, 306, 173,
                            self.CLOUDS_PIC_PATHS, self.SCREEN, "Cloud", 0, self.CLOUDS_SPEED))

    def tick(self):
        des = 0
        for p in range(len(self.CLOUDS)):
            c = self.CLOUDS[p]
            c.move()
            if p == len(self.CLOUDS) - 1 and c.y > c.get_height():
                self.CLOUDS.append(
                    BasicComponent(int(uniform(-150, self.SCREEN_WIDTH - 150)), -173, 306, 173,
                                   self.CLOUDS_PIC_PATHS, self.SCREEN, "Cloud", 0, self.CLOUDS_SPEED))

            if c.y >= self.SCREEN_LENGTH:
                des += 1

        for _ in range(des):
            self.CLOUDS.pop(0)

    def draw(self):
        for c in self.CLOUDS:
            c.draw()
