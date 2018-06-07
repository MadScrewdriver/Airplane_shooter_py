import pygame
import os
from screeninfo import get_monitors
from Basic_Component import BasicComponent


class Score:
    def __init__(self):
        self.score = 0

    def add_score(self):
        self.score += 10

    def get_score(self):
        return self.score


class GlobalConstants:

    # --------------------PATHS----------------------------------------------------
    B_A_PATH = os.path.join("Pictures", "Player", "BasicAirplane")
    T_I_PATH = os.path.join("Pictures", "TitleIcon", "title_icon.png")
    BULL_PATH = os.path.join("Pictures", "Bullets", "Fireball")
    BACK_PATH = os.path.join("Pictures", "Background")
    B_E_PATH = os.path.join("Pictures", "Enemy", "BasicEnemy")
    R_PATH = os.path.join("Pictures", "Enemy", "Rocket")
    BOM_PATH = os.path.join("Pictures", "Enemy", "Bomber")
    EXPLO_PATH = os.path.join("Pictures", "Explosion")
    PIX_FONT_PATH = os.path.join("Fonts", "Pixel_font.ttf")

    BOM_PIC_PATH = [os.path.join(BOM_PATH, "bomber.png")]
    Fire_PIC_PATHS = [os.path.join(BULL_PATH, "bullet.png")]
    ROC_PIC_PATH = [os.path.join(R_PATH, "rocket.png")]
    BACK_PIC_PATHS = [os.path.join(BACK_PATH, "background.png")]
    ENEMY_PIC_PATHS = [os.path.join(B_E_PATH, "straight.png")]
    PLAYER_PIC_PATHS = (lambda x=B_A_PATH: [os.path.join(x, p + ".png") for p in ["straight", "left", "right"]])()

    # --------------------OTHER VARIABLES-------------------------------------------
    MARGIN = int(get_monitors()[0].height * 0.025)
    SCREEN_LENGTH = int(get_monitors()[-1].height * 0.75)
    SCREEN_WITH = int(get_monitors()[-1].height * 0.5)
    MIN_DISTANCE = int(SCREEN_WITH / 54)
    ENEMY_WITH = int(SCREEN_WITH / 3.90)
    ENEMY_HEIGHT = int(SCREEN_WITH / 5.27)
    BOMBER_WITH = int(SCREEN_WITH / 3.65)
    BOMBER_HEIGHT = int(SCREEN_WITH / 4.61)
    SCREEN = pygame.display.set_mode((SCREEN_WITH, SCREEN_LENGTH))
    ENEMIES = []
    BULLETS = []
    BULLET_SIZE = int(SCREEN_WITH / 54)
    PLAYER = BasicComponent(SCREEN_WITH / 2 - (SCREEN_WITH / 3.90) / 2, SCREEN_LENGTH * (4 / 6),
                            SCREEN_WITH / 3.90, SCREEN_WITH / 5.27, PLAYER_PIC_PATHS, SCREEN, "player")


class FireballConstants(GlobalConstants):
    def __init__(self):
        self.BULLET_SPEED = -self.SCREEN_WITH / 80


class PlayerConstants(GlobalConstants):
    def __init__(self):
        self.SPEED = self.SCREEN_WITH / 120


class MesserschmittConstants(GlobalConstants):
    def __init__(self):
        self.Messerschmitt_SPEED = self.SCREEN_WITH / 150


class BomberConstants(GlobalConstants):
    def __init__(self):
        self.BOMBER_SPEED = self.SCREEN_WITH / 150


class BackgroundConstants(GlobalConstants):
    def __init__(self):
        self.BG_SPEED = self.SCREEN_WITH / 270


class LevelsConstants(GlobalConstants):
    def __init__(self):
        pass


class MasksConstants(GlobalConstants):
    def __init__(self):
        pass
