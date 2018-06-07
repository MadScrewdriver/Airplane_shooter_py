import pygame
import sys
import time
from Player import Player
from Bullet import Bullets
from Enemy import Enemy
from Background import Background
from Settings import GlobalConstants


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
        print(self.SCREEN_WITH, self.SCREEN_LENGTH)

        # Initialization
        self.player = Player()
        self.bullet = Bullets()
        self.enemy = Enemy()
        self.background = Background()
        self.time_start = time.time()
        self.shout_time = time.time()

        # Main loop
        while True:
            self.SCREEN.fill((0, 0, 0))

            for event in pygame.event.get():
                if event.type == pygame.QUIT or event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                    sys.exit(0)

                if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE and \
                        time.time() - self.shout_time >= 0.5:

                    self.bullet.shoot()
                    self.shout_time = time.time()

            # Ticking
            self.fps += 1
            self.delta += self.clock.tick() / 1000.0
            while self.delta > 1 / self.max_tps:
                self.tick()
                self.delta -= 1 / self.max_tps

            # Drawing
            self.draw()

            if time.time() - self.time_start >= 1:
                pygame.display.set_caption("303 Polish Fighter Squadron     fps: " + str(self.fps))
                self.fps = 0
                self.time_start = time.time()

            pygame.display.flip()

    def tick(self):
        self.background.tick()
        self.bullet.tick()
        self.player.tick()
        self.enemy.tick()
        self.score = self.enemy.touch(self.score)

    def draw(self):
        self.background.draw(self.score)
        self.bullet.draw()
        self.player.draw()
        self.enemy.draw(self.score)


if __name__ == '__main__':
    pygame.init()
    Game()




