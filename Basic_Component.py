import pygame
from pygame.math import Vector2


class BasicComponent(Vector2):
    def __init__(self, x, y, width, height, image, screen, name, move_x, move_y):
        self._height = height
        self._width = width
        self._image = [pygame.image.load(i) for i in image]
        self._screen = screen
        self._name = name
        self._move_x = move_x
        self._move_y = move_y

        super().__init__(x, y)

    def get_name(self):
        return self._name

    def get_height(self):
        return self._height

    def get_width(self):
        return self._width

    def move(self):
        self.x += self._move_x
        self.y += self._move_y

    def rectangle_collision(self, second_object):

        x1 = self.x
        y1 = self.y
        w1 = self._width
        h1 = self._height
        x2 = second_object.x
        y2 = second_object.y
        w2 = second_object.get_width()
        h2 = second_object.get_height()

        # print(int(x1), int(y1), int(w1), int(h1), self.get_name(),
        # int(x2), int(y2), int(w2), int(h2), second_object.get_name())

        if x2 + w2 >= x1 >= x2 and y2 + h2 >= y1 >= y2:
            return True

        elif x2 + w2 >= x1 + w1 >= x2 and y2 + h2 >= y1 >= y2:
            return True

        elif x2 + w2 >= x1 >= x2 and y2 + h2 >= y1 + h1 >= y2:
            return True

        elif x2 + w2 >= x1 + w1 >= x2 and y2 + h2 >= y1 + h1 >= y2:
            return True

        elif x1 + w1 >= x2 >= x1 and y1 + h1 >= y2 >= y1:
            return True

        elif x1 + w1 >= x2 + w2 >= x1 and y1 + h1 >= y2 >= y1:
            return True

        elif x1 + w1 >= x2 >= x1 and y1 + h1 >= y2 + h2 >= y1:
            return True

        elif x1 + w1 >= x2 + w2 >= x1 and y1 + h1 >= y2 + h2 >= y1:
            return True

        else:
            return False

    def draw(self, img_num=0):
        self._screen.blit(pygame.transform.scale(self._image[img_num],
                                                 (int(self._width),
                                                  int(self._height))),
                                                (int(self.x),
                                                 int(self.y)))
