import pygame
import sys
from Player import Rocket
from Bullet import Bullets
from Enemy import Enemy
from Background import Background
from settings import GlobalConstants


class Game(GlobalConstants):

    def __init__(self):

        # Config
        self.max_fps = 40
        self.clock = pygame.time.Clock()
        self.delta = 0.0
        pygame.display.set_caption("303 Polish Fighter Squadron")
        self.title_icon = pygame.image.load("Pictures/TitleIcon/title_icon.png")
        pygame.display.set_icon(self.title_icon)
        print(self.SCREEN_WITH, self.SCREEN_LENGTH)

        # Initialization
        self.player = Rocket()
        self.bullet = Bullets()
        self.enemy = Enemy()
        self.background = Background()

        # Main loop
        while True:
            self.SCREEN.fill((0, 0, 0))

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




