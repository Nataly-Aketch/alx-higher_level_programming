#!/usr/bin/python3
"""this module defines a class rectangle"""


class Rectangle:
    """this class defines a rectangle based on task 2"""
    number_of_instances = 0
    print_symbol = '#'

    def __init__(self, width=0, height=0):
        """Initializes a class rectangle"""
        self.width = width
        self.height = height
        type(self).number_of_instances += 1

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        return self.__height * self.__width

    def perimeter(self):
        if 0 in (self.__width, self.__height):
            return 0
        return 2 * (self.__width + self.__height)

    def __str__(self):
        if self.__height == 0 or self.__width == 0:
            return ""
        return (self.__height - 1) * (str(self.print_symbol) *
                                      self.__width + '\n') + \
            str(self.print_symbol) * self.__width

    def __repr__(self):
        return "Rectangle(" + str(self.width) + ", " + str(self.height) + ")"

    def __del__(self):
        print("Bye rectangle...")
        type(self).number_of_instances -= 1

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        new_rect = [rect_1, rect_2]
        for i in range(2):
            if not isinstance(new_rect[i], Rectangle):
                raise TypeError("{} must be an instance of Rectangle"
                                .format("rect_1" if i == 0 else "rect_2"))

        if rect_1.area() > rect_2.area():
            return rect_1
        elif rect_1.area() < rect_2.area():
            return rect_2
        else:
            return rect_1

    @classmethod
    def square(cls, size=0):
        cls.__height = size
        cls.__width = size
        return cls(size, size)
