from pygame.math import Vector2
import pygame


class BasicComponent(Vector2):
    def __init__(self, x, y, high, width, image, screen):
        self.x = x
        self.y = y
        self.high = high
        self.width = width
        self.image = image
        self.screen = screen
        super().__init__(self.x, self.y)

    def high(self):
        return self.hight

    def width(self):
        return self.width

    def detect_collision(self, second_object):
        bigger = (self.width * self.high) > (second_object.width * second_object.high)

        if bigger:
            x1 = self.x
            y1 = self.y
            w1 = self.high
            h1 = self.width
            x2 = second_object.x
            y2 = second_object.y
            w2 = second_object.width
            h2 = second_object.high

        else:
            x1 = second_object.x
            y1 = second_object.y
            w1 = second_object.width
            h1 = second_object.high
            x2 = self.x
            y2 = self.y
            w2 = self.high
            h2 = self.width

        if x2 + w2 >= x1 >= x2 and y2 + h2 >= y1 >= y2:
            return True

        elif x2 + w2 >= x1 + w1 >= x2 and y2 + h2 >= y1 >= y2:
            return True

        elif x2 + w2 >= x1 >= x2 and y2 + h2 >= y1 + h1 >= y2:
            return True

        elif x2 + w2 >= x1 + w1 >= x2 and y2 + h2 >= y1 + h1 >= y2:
            return True

        else:
            return False

    def draw(self):
        self.screen.blit(pygame.transform.scale(self.image,
                                                (int(self.x),
                                                 int(self.y))), (int(self.width),
                                                                 int(self.high)))
