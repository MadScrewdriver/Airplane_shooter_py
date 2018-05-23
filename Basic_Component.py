from pygame.math import Vector2
import pygame


class BasicComponent(Vector2):
    def __init__(self, x, y, width, height, image, screen):
        self._height = height
        self._width = width
        self._image = [pygame.image.load(i) for i in image]
        self._screen = screen

        super().__init__(x, y)

    def get_height(self):
        return self._height

    def get_width(self):
        return self._width

    def detect_collision(self, second_object):
        bigger = (self._width * self._height) > (second_object.get_width() * second_object.get_height())

        if bigger:
            x1 = second_object.x
            y1 = second_object.y
            w1 = second_object.get_width()
            h1 = second_object.get_height()
            x2 = self.x
            y2 = self.y
            h2 = self._height
            w2 = self._width

        else:
            x1 = self.x
            y1 = self.y
            w1 = self._height
            h1 = self._width
            x2 = second_object.x
            y2 = second_object.y
            w2 = second_object.get_width()
            h2 = second_object.get_height()

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

    def draw(self, img_num=0):
        self._screen.blit(pygame.transform.scale(self._image[img_num],
                                                 (int(self._width),
                                                  int(self._height))),
                                                (int(self.x),
                                                 int(self.y)))
