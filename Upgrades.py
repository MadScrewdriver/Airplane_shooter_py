import pygame
from Settings import GlobalConstants
from Basic_Component import BasicComponent
from RandomUp import RandomUp


class Upgrade(GlobalConstants):
    def __init__(self, player):
        self.spitfire = player

    def add_upgrade(self, x, y):
        self.UPGRADES.append(RandomUp(x, y))

    def tick(self):
        up_destroy = []
        for u in range(len(self.UPGRADES)):
            up = self.UPGRADES[u]
            up.move()

            if self.spitfire.detect_collision(up) :
                up_destroy.append(u)
                print(True)

        for d in up_destroy:
            self.UPGRADES.pop(d)

    def draw(self):
        for upg in self.UPGRADES:
            upg.draw()
