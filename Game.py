import pygame
import sys
from Player import Rocket
from Bullet import Bullets
from Enemy import Enemy
from Background import Background
from screeninfo import get_monitors


class Game(object):

    def __init__(self):

        # Config
        self.max_fps = 40
        self.screen_length = int(get_monitors()[0].height * 0.75)
        self.screen_with = int(get_monitors()[0].height * 0.5)
        self.screen = pygame.display.set_mode((self.screen_with, self.screen_length))
        self.clock = pygame.time.Clock()
        self.delta = 0.0
        pygame.display.set_caption("303 Polish Fighter Squadron")
        self.title_icon = pygame.image.load("title_icon.png")
        pygame.display.set_icon(self.title_icon)

        # Initialization
        self.player = Rocket(self)
        self.bullet = Bullets(self, self.player)
        self.enemy = Enemy(self, self.player, self.bullet)
        self.background = Background(self)
        print(self.screen_with, self.screen_length)

        while True:
            self.update()
            self.screen.fill((0, 0, 0))

            for event in pygame.event.get():
                if event.type == pygame.QUIT or event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                    sys.exit(0)

                if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                    self.bullet.shoot()

            # Ticking
            self.delta += self.clock.tick() / 1000.0
            while self.delta > 1 / self.max_fps:
                self.tick()
                self.delta -= 1 / self.max_fps

            # Drawing
            self.draw()
            pygame.display.flip()

    def update(self):
        self.screen_length = int(get_monitors()[0].height * 0.75)
        self.screen_with = int(get_monitors()[0].height * 0.5)

    def tick(self):
        self.background.tick()
        self.bullet.tick()
        self.player.tick()
        self.enemy.tick()

    def draw(self):
        self.background.draw()
        self.bullet.draw()
        self.player.draw()
        self.enemy.draw()


if __name__ == '__main__':
    pygame.init()
    Game()




