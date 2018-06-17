import pygame
import os
from screeninfo import get_monitors


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
    R_BULL_PATH = os.path.join("Pictures", "Bullets", "Red_fireball")
    B_Bull_PATH = os.path.join("Pictures", "Bullets", "Bomb")
    BACK_PATH = os.path.join("Pictures", "Background")
    B_E_PATH = os.path.join("Pictures", "Enemy", "BasicEnemy")
    R_PATH = os.path.join("Pictures", "Enemy", "Rocket")
    BOM_PATH = os.path.join("Pictures", "Enemy", "Bomber")
    EXPLO_PATH = os.path.join("Pictures", "Explosion")
    PIX_FONT_PATH = os.path.join("Fonts", "Pixel_font.ttf")
    HEART_PATH = os.path.join("Pictures", "Heart")
    HOUSE_PATH = os.path.join("Pictures", "House")

    HOUSE_PIC_PATH = [os.path.join(HOUSE_PATH, "house.png")]
    B_BULL_PIC_PATHS = [os.path.join(B_Bull_PATH, "bomb.png")]
    HEART_PIC_PATH = [os.path.join(HEART_PATH, "heart.png")]
    R_BULL_PIC_PATHS = [os.path.join(R_BULL_PATH, "red_fireball.png")]
    BOM_PIC_PATH = [os.path.join(BOM_PATH, "bomber.png")]
    Fire_PIC_PATHS = [os.path.join(BULL_PATH, "bullet.png")]
    ROC_PIC_PATH = [os.path.join(R_PATH, "rocket.png")]
    BACK_PIC_PATHS = [os.path.join(BACK_PATH, "background.png")]
    ENEMY_PIC_PATHS = [os.path.join(B_E_PATH, "straight.png")]
    PLAYER_PIC_PATHS = (lambda x=B_A_PATH: [os.path.join(x, p + ".png") for p in ["straight", "left", "right"]])()

    # --------------------OTHER VARIABLES-------------------------------------------
    SCREEN_WIDTH = int(get_monitors()[-1].height / 1.8)
    SCREEN_LENGTH = int(get_monitors()[-1].height / 1.2)
    MARGIN = int(SCREEN_WIDTH / 20)
    FONT_SIZE = int(SCREEN_WIDTH / 12)
    GAP_BETWEEN_H_H = SCREEN_WIDTH / 30000
    MIN_DISTANCE = int(SCREEN_WIDTH / 54)
    SPITFIRE_WIDTH = int(SCREEN_WIDTH / 3.90)
    SPITFIRE_HEIGHT = int(SCREEN_WIDTH / 5.27)
    MESSERSCHMITT_WIDTH = int(SCREEN_WIDTH / 3.90)
    MESSERSCHMITT_HEIGHT = int(SCREEN_WIDTH / 5.27)
    BOMBER_WIDTH = int(SCREEN_WIDTH / 3.65)
    BOMBER_HEIGHT = int(SCREEN_WIDTH / 4.61)
    HEART_WIDTH = int(SCREEN_WIDTH / 12.27)
    HEART_HEIGHT = int(SCREEN_WIDTH / 13.5)
    HOUSE_WIDTH = int(SCREEN_WIDTH / 13.5)
    HOUSE_HEIGHT = int(SCREEN_WIDTH / 13.5)
    ROCKET_WIDTH = int(SCREEN_WIDTH / 13.85)
    ROCKET_HEIGHT = int(SCREEN_WIDTH / 6)
    SCREEN = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_LENGTH))
    ENEMIES = []
    BULLETS = []
    EXPLOSIONS = []
    LIVES = []
    HOUSES = []
    BULLET_SIZE = int(SCREEN_WIDTH / 54)
    BOMB_WIDTH = int(SCREEN_WIDTH / 54)
    BOMB_HEIGHT = int(SCREEN_WIDTH / 20)
    BOMB_SPEED = SCREEN_WIDTH / 90
    MESSERSCHMITT_SPEED = SCREEN_WIDTH / 150
    BULLET_SPEED = SCREEN_WIDTH / 80
    BOMBER_SPEED = SCREEN_WIDTH / 150
    ROCKET_SPEED = SCREEN_WIDTH / 70


class PlayerConstants(GlobalConstants):
    def __init__(self):
        self.SPEED = self.SCREEN_WIDTH / 120


class BackgroundConstants(GlobalConstants):
    def __init__(self):
        self.BG_SPEED = self.SCREEN_WIDTH / 270


class LevelsConstants(GlobalConstants):
    def __init__(self):
        pass


class MaskConstants(GlobalConstants):
    def __init__(self):
        pass
