import pygame
import sys
import time
from Player import Player
from Bullet import Bullets
from Enemy import Enemy
from Background import Background
from Settings import GlobalConstants
from Spitfire import Spitfire


# Main class
class Game(GlobalConstants):

    def __init__(self):

        # Config
        self.max_tps = 40
        self.fps = 0
        self.clock = pygame.time.Clock()
        self.delta = 0.0
        self.title_icon = pygame.image.load(self.T_I_PATH)
        pygame.display.set_caption("303 Polish Fighter Squadron     fps: " + str(self.fps))
        pygame.display.set_icon(self.title_icon)
        self.score = 0
        self.pause = False
        self.house = False
        self.heart = False
        self.t = 0
        self.lives = 3
        self.houses = 3
        print(self.SCREEN_WIDTH, self.SCREEN_LENGTH)

        # Initialization
        self.SPITFIRE = Spitfire(self.SCREEN_WIDTH / 2 - (self.SCREEN_WIDTH / 3.90) / 2, self.SCREEN_LENGTH * (4 / 6))
        self.player = Player(self.SPITFIRE)
        self.bullet = Bullets(self.SPITFIRE)
        self.enemy = Enemy(self.SPITFIRE)
        self.background = Background()
        self.time_start = time.time()
        self.shout_time = time.time()

        # Main loop
        while True:
            self.SCREEN.fill((0, 0, 0))

            for event in pygame.event.get():
                if event.type == pygame.QUIT or event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                    sys.exit(0)

                if event.type == pygame.KEYDOWN and event.key == pygame.K_l:
                    self.lives = 5
                    self.houses = 5

                if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE and \
                        time.time() - self.shout_time >= 0.5:

                    self.bullet.shoot()
                    self.shout_time = time.time()

            # Ticking
            self.fps += 1
            self.delta += self.clock.tick() / 1000.0
            while self.delta > 1 / self.max_tps:
                if not self.pause:
                    self.tick()
                self.delta -= 1 / self.max_tps

            # Drawing
            if not self.pause:
                self.draw()

            else:
                self.stop()
                if time.time() - self.t >= 2:
                    if self.house:
                        self.houses -= 1

                    if self.heart:
                        self.lives -= 1

                    self.pause = False
                    self.house = False
                    self.heart = False
                    self.ENEMIES.clear()
                    self.EXPLOSIONS.clear()
                    self.BULLETS.clear()
                    self.SPITFIRE.x = self.SCREEN_WIDTH / 2 - (self.SCREEN_WIDTH / 3.90) / 2
                    self.SPITFIRE.y = self.SCREEN_LENGTH * (4 / 6)

                    if self.lives == 0 or self.houses == 0:
                        self.lives = 3
                        self.houses = 3

            if time.time() - self.time_start >= 1:
                pygame.display.set_caption("303 Polish Fighter Squadron     fps: " + str(self.fps))
                self.fps = 0
                self.time_start = time.time()

            pygame.display.flip()

    def tick(self):
        self.background.tick()
        self.bullet.tick()
        self.player.tick()
        ret = self.enemy.tick(self.score)
        self.score = ret[0]
        self.pause = ret[1]
        self.house = ret[2]
        self.heart = ret[3]

        if self.pause:
            self.set_t()

    def draw(self):
        self.background.draw(self.score)
        self.background.draw_lives(self.lives)
        self.background.draw_houses(self.houses)
        self.bullet.draw()
        self.player.draw()
        self.enemy.draw(self.score, self.pause)

    def set_t(self):
        self.t = time.time()

    def stop(self):
        self.background.draw(self.score)
        self.bullet.draw()
        self.enemy.draw(self.score, self.pause)

        if ((0 < time.time() - self.t < 0.25) or (0.5 < time.time() - self.t < 0.75) or
           (1 < time.time() - self.t < 1.25) or (1.5 < time.time() - self.t < 1.75)) and self.heart:
            self.background.draw_lives(self.lives, True)

        else:
            self.background.draw_lives(self.lives)

        if ((0 < time.time() - self.t < 0.25) or (0.5 < time.time() - self.t < 0.75) or
           (1 < time.time() - self.t < 1.25) or (1.5 < time.time() - self.t < 1.75)) and self.house:
            self.background.draw_houses(self.houses, True)

        else:
            self.background.draw_houses(self.houses)

        t = True
        for bull in self.BULLETS:

            if self.SPITFIRE.detect_collision(bull) and bull.get_name() in ["Red_fireball", "Bomb"]:
                if (0.25 < time.time() - self.t < 0.5) or (0.75 < time.time() - self.t < 1) or \
                        (1.25 < time.time() - self.t < 1.5) or (1.75 < time.time() - self.t < 2):
                    self.player.draw(True)
                t = False

        if t:
            self.player.draw(True)

        for en in self.ENEMIES:
            if self.SPITFIRE.detect_collision(en) or (en.y >= self.SCREEN_LENGTH - en.get_height() -
               self.MARGIN * 3):

                if (0.25 < time.time() - self.t < 0.5) or (0.75 < time.time() - self.t < 1) or \
                        (1.25 < time.time() - self.t < 1.5) or (1.75 < time.time() - self.t < 2):
                    en.draw()

            else:
                en.draw()


if __name__ == '__main__':
    pygame.init()
    Game()
