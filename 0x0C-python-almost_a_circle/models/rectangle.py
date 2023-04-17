#!/usr/bin/python3
"""defines a class rectangle"""
from models.base import Base


class Rectangle(Base):
    """inherits from Base class"""
    def __init__(self, width, height, x=0, y=0, id=None):
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if type(value) != int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if type(value) != int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, value):
        if type(value) != int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, value):
        if type(value) != int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """calculates area of a triangle"""
        return self.__width * self.__height

    def display(self):
        """prints rectangle using #"""
        if self.__height == 0 or self.__height == 0:
            print("")
        [print("") for y in range(self.y)]
        for i in range(self.__height):
            [print(" ", end="") for x in range(self.x)]
            for i in range(self.__width):
                print("#", end="")
            print()

    def to_dictionary(self):
        """returns dictionary representation of a rectangle"""
        return {'id': self.id, 'width': self.width,
                'height': self.height, 'x': self.x, 'y': self.y}

    def __str__(self):
        """returns string representaion of the class rectangle"""
        return "[Rectangle] ({}) {}/{} - {}/{}".format(self.id, self.x,
                                                       self.y, self.width,
                                                       self.height)

    def update(self, *args, **kwargs):
        """assigns an argument to each attribute"""
        if args and len(args) != 0:
            try:
                if args[0] is None:
                    self.__init__(self.width, self.height, self.x, self.y)
                else:
                    self.id = args[0]
                    self.width = args[1]
                    self.height = args[2]
                    self.x = args[3]
                    self.y = args[4]
            except Exception:
                pass

        elif kwargs and len(kwargs) != 0:
            for k, v in kwargs.items():
                if k == 'id':
                    if v is None:
                        self.__init__(self.width, self.height, self.x, self.y)
                    else:
                        self.id = v
                if k == 'x':
                    self.x = v
                if k == 'y':
                    self.y = v
                if k == 'width':
                    self.width = v
                if k == 'height':
                    self.height = v
