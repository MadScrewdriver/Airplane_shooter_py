from random import *
from Messerschmitt import Messerschmitt
from Bomber import Bomber
from Rocket import Rocket
from Settings import LevelsConstants


class Levels(LevelsConstants):
    def __init__(self):
        super().__init__()

    def level_1(self):
        self.ENEMIES.append(
            Messerschmitt(
                randint(int(self.MARGIN), int(self.SCREEN_WIDTH - (self.MARGIN + self.SCREEN_WIDTH / 3.90))),
                -self.MESSERSCHMITT_HEIGHT))

    def level_2(self):
        self.ENEMIES.append(
            Messerschmitt(
                randint(int(self.MARGIN), int(self.SCREEN_WIDTH - self.MARGIN - self.MESSERSCHMITT_WIDTH)),
                int(-1 * randint(self.MESSERSCHMITT_HEIGHT, self.MESSERSCHMITT_HEIGHT * 2))
                -self.MESSERSCHMITT_HEIGHT))

        left = self.ENEMIES[0].x - self.MARGIN - self.MIN_DISTANCE >= self.MESSERSCHMITT_WIDTH
        right = (self.SCREEN_WIDTH - self.MARGIN) - (
                    self.ENEMIES[0].x + self.MESSERSCHMITT_WIDTH) - self.MIN_DISTANCE >= self.MESSERSCHMITT_WIDTH

        if left and right:
            left = choice([True, False])

        if left:
            self.ENEMIES.append(
                Messerschmitt(
                    randint(int(self.MARGIN), int(self.ENEMIES[0].x - self.MIN_DISTANCE - self.MESSERSCHMITT_WIDTH)),
                    int(-self.MESSERSCHMITT_HEIGHT)
                    - self.MESSERSCHMITT_HEIGHT))

        else:
            self.ENEMIES.append(
                Messerschmitt(
                    randint(int(self.ENEMIES[0].x + self.MESSERSCHMITT_WIDTH + self.MIN_DISTANCE),
                            int(self.SCREEN_WIDTH - self.MARGIN - self.MESSERSCHMITT_WIDTH)),
                    int(-self.MESSERSCHMITT_HEIGHT)
                    - self.MESSERSCHMITT_HEIGHT))

    def level_3(self):
        array = randint(1, 4)

        if array == 1:
            self.ENEMIES.append(
                Messerschmitt(
                    self.MARGIN,
                    -self.MESSERSCHMITT_HEIGHT))

            self.ENEMIES.append(
                Messerschmitt(
                    self.MARGIN + self.MESSERSCHMITT_WIDTH + self.MIN_DISTANCE,
                    int(-self.MESSERSCHMITT_HEIGHT * 2)))

            self.ENEMIES.append(
                Bomber(
                    self.MARGIN + self.MESSERSCHMITT_WIDTH * 2 + self.MIN_DISTANCE * 2,
                    int(-self.MESSERSCHMITT_HEIGHT * 2 + -self.BOMBER_HEIGHT)))

        elif array == 2:
            self.ENEMIES.append(
                Messerschmitt(
                    self.SCREEN_WIDTH - self.MARGIN - self.MESSERSCHMITT_WIDTH,
                    int(-self.MESSERSCHMITT_HEIGHT)))

            self.ENEMIES.append(
                Messerschmitt(
                    self.SCREEN_WIDTH - self.MARGIN - self.MESSERSCHMITT_WIDTH * 2 - self.MIN_DISTANCE,
                    int(-self.MESSERSCHMITT_HEIGHT * 2)))

            self.ENEMIES.append(
                Bomber(
                    self.SCREEN_WIDTH - self.MARGIN - self.MESSERSCHMITT_WIDTH * 3 - self.MIN_DISTANCE * 2,
                    int(-self.MESSERSCHMITT_HEIGHT * 2 - self.BOMBER_HEIGHT)))

        elif array == 3:
            self.ENEMIES.append(
                Messerschmitt(
                    self.SCREEN_WIDTH / 2 - self.MESSERSCHMITT_WIDTH / 2,
                    int(-self.MESSERSCHMITT_HEIGHT)))

            self.ENEMIES.append(
                Bomber(
                    self.SCREEN_WIDTH / 2 - self.MESSERSCHMITT_WIDTH / 2 - self.MESSERSCHMITT_WIDTH - self.MIN_DISTANCE,
                    int(-self.MESSERSCHMITT_HEIGHT - self.BOMBER_HEIGHT)))

            self.ENEMIES.append(
                Messerschmitt(
                    self.SCREEN_WIDTH / 2 + self.MESSERSCHMITT_WIDTH / 2 + self.MIN_DISTANCE,
                    int(-self.MESSERSCHMITT_HEIGHT * 2)))

        elif array == 4:
            self.ENEMIES.append(
                Bomber(
                    int(self.SCREEN_WIDTH / 2 - self.MESSERSCHMITT_WIDTH / 2),
                    int(-self.MESSERSCHMITT_HEIGHT - self.BOMBER_HEIGHT)))

            self.ENEMIES.append(
                Messerschmitt(
                    int(self.SCREEN_WIDTH / 2 - self.MESSERSCHMITT_WIDTH / 2 - self.MIN_DISTANCE -
                        self.MESSERSCHMITT_WIDTH),
                    int(-self.MESSERSCHMITT_HEIGHT)))

            self.ENEMIES.append(
                Messerschmitt(
                    int(self.SCREEN_WIDTH / 2 + self.MESSERSCHMITT_WIDTH / 2 + self.MIN_DISTANCE),
                    int(-self.MESSERSCHMITT_HEIGHT)))

    def level_4(self):
        array = 1
        
        if array == 1:
            self.ENEMIES.append(
                Rocket(
                    randint(int(self.MARGIN), int(self.SCREEN_WIDTH - self.MARGIN - self.ROCKET_WIDTH)),
                    -1 * randint(int(self.ROCKET_HEIGHT * 2), int(self.ROCKET_HEIGHT * 5))))

            left = self.ENEMIES[0].x - self.MARGIN - self.MIN_DISTANCE >= self.MESSERSCHMITT_WIDTH
            right = (self.SCREEN_WIDTH - self.MARGIN) - (
                    self.ENEMIES[0].x + self.ROCKET_WIDTH) - self.MIN_DISTANCE >= self.MESSERSCHMITT_WIDTH

            if left:
                if self.ENEMIES[0].x - self.MARGIN - self.MIN_DISTANCE >= self.BOMBER_WIDTH:
                    self.ENEMIES.append(
                        Bomber(
                            randint(int(self.MARGIN),
                                    int(self.ENEMIES[0].x - self.MIN_DISTANCE - self.BOMBER_WIDTH)),
                            -1 * randint(int(self.BOMBER_HEIGHT), int(self.BOMBER_HEIGHT) * 2)))

                    if not right:

                        if self.ENEMIES[1].x - self.MARGIN - self.MIN_DISTANCE >= self.MESSERSCHMITT_WIDTH:

                            if self.ENEMIES[1].x - self.MARGIN - self.MIN_DISTANCE >= self.BOMBER_WIDTH:
                                self.ENEMIES.append(
                                    Bomber(
                                        randint(int(self.MARGIN),
                                                int(self.ENEMIES[1].x - self.MIN_DISTANCE - self.BOMBER_WIDTH)),
                                        -1 * randint(int(self.BOMBER_HEIGHT), int(self.BOMBER_HEIGHT) * 3)))

                            else:
                                self.ENEMIES.append(
                                    Messerschmitt(
                                        randint(int(self.MARGIN), int(self.ENEMIES[1].x -
                                                                      self.MIN_DISTANCE - self.MESSERSCHMITT_WIDTH)),
                                        -1 * randint(int(self.MESSERSCHMITT_HEIGHT), int(self.MESSERSCHMITT_HEIGHT) * 3)))

                else:
                    self.ENEMIES.append(
                        Messerschmitt(
                            randint(int(self.MARGIN), int(self.ENEMIES[0].x -
                                                          self.MIN_DISTANCE - self.MESSERSCHMITT_WIDTH)),
                            -1 * randint(int(self.MESSERSCHMITT_HEIGHT), int(self.MESSERSCHMITT_HEIGHT) * 2)))

            if right:

                if self.SCREEN_WIDTH - self.MARGIN - self.ENEMIES[0].x - self.ROCKET_WIDTH - self.MIN_DISTANCE >= \
                        self.BOMBER_WIDTH:

                    self.ENEMIES.append(
                        Bomber(
                            randint(int(self.ENEMIES[0].x + self.MIN_DISTANCE + self.ROCKET_WIDTH),
                                    int(self.SCREEN_WIDTH - self.BOMBER_WIDTH - self.MARGIN)),
                            -1 * randint(int(self.BOMBER_HEIGHT), int(self.BOMBER_HEIGHT) * 2)))

                    if not left:

                        if self.SCREEN_WIDTH - self.MARGIN - self.ENEMIES[1].x - self.BOMBER_WIDTH - self.MIN_DISTANCE \
                                >= self.MESSERSCHMITT_WIDTH:

                            if self.SCREEN_WIDTH - self.MARGIN - self.ENEMIES[1].x - self.BOMBER_WIDTH - \
                                    self.MIN_DISTANCE >= self.BOMBER_WIDTH:

                                self.ENEMIES.append(
                                    Bomber(
                                        randint(int(self.ENEMIES[1].x + self.BOMBER_WIDTH),
                                                int(self.SCREEN_WIDTH - self.MIN_DISTANCE -
                                                    self.BOMBER_WIDTH - self.MARGIN)),
                                        -1 * randint(int(self.BOMBER_HEIGHT), int(self.BOMBER_HEIGHT) * 3)))

                            else:
                                self.ENEMIES.append(
                                    Messerschmitt(
                                        randint(int(self.ENEMIES[1].x + self.BOMBER_WIDTH),
                                                int(self.SCREEN_WIDTH - self.MIN_DISTANCE -
                                                    self.MESSERSCHMITT_WIDTH - self.MARGIN)),
                                        -1 * randint(int(self.BOMBER_HEIGHT), int(self.BOMBER_HEIGHT) * 3)))
                else:
                    self.ENEMIES.append(
                        Messerschmitt(
                            randint(int(self.ENEMIES[0].x + self.ROCKET_WIDTH), self.SCREEN_WIDTH - self.MIN_DISTANCE -
                                    self.MESSERSCHMITT_WIDTH - self.MARGIN),
                            -1 * randint(int(self.MESSERSCHMITT_HEIGHT), int(self.MESSERSCHMITT_HEIGHT) * 2)))
