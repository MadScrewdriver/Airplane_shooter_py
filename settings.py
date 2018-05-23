import pygame
from screeninfo import get_monitors
from Basic_Component import BasicComponent


class GlobalConstants:
    MARGIN = int(get_monitors()[0].height * 0.025)
    SCREEN_LENGTH = int(get_monitors()[-1].height * 0.75)
    SCREEN_WITH = int(get_monitors()[-1].height * 0.5)
    SCREEN = pygame.display.set_mode((SCREEN_WITH, SCREEN_LENGTH))
    ENEMIES = []
    BULLETS = []
    BULLET_SIZE = int(SCREEN_WITH / 54)
    PLAYER = BasicComponent(SCREEN_WITH / 2 - (SCREEN_WITH / 3.90) / 2, SCREEN_LENGTH * (5 / 6),
                            SCREEN_WITH / 3.90, SCREEN_WITH / 5.27,
                            ["Pictures/Player/BasicAirplane/" + p + ".png" for p in ["straight", "left", "right"]],
                            SCREEN)


class BulletConstants(GlobalConstants):
    def __init__(self):
        self.BULLET_SPEED = -self.SCREEN_WITH / 80


class RocketConstants(GlobalConstants):
    def __init__(self):
        self.SPEED = self.SCREEN_WITH / 120


class EnemiesConstants(GlobalConstants):
    def __init__(self):
        self.ENEMY_WITH = self.SCREEN_WITH / 3.90
        self.ENEMY_HEIGHT = self.SCREEN_WITH / 5.27


class BackgroundConstants(GlobalConstants):
    def __init__(self):
        self.BG_SPEED = 2
