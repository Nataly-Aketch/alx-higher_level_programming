#!/usr/bin/python3
"""defines a class Square that inherits from rectangle"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """inherits all attributes of class Rectangle"""
    def __init__(self, size, x=0, y=0, id=None):
        """initializes square"""
        super().__init__(size, size, x, y, id=None)

    @property
    def size(self):
        return super().width

    @size.setter
    def size(self, value):
        Rectangle.width.fset(self, value)
        Rectangle.height.fset(self, value)

    def update(self, *args, **kwargs):
        """updates the class"""
        if args and len(args) != 0:
            for i, arg in enumerate(args):
                if i == 0:
                    if arg is None:
                        self.__init__(self.size, self.x, self.y)
                    else:
                        self.id = arg
                if i == 1:
                    self.size = arg
                if i == 2:
                    self.x = arg
                if i == 3:
                    self.y = arg

        if kwargs and len(kwargs) != 0:
            for k, v in kwargs.items():
                if k == "id":
                    if v is None:
                        self.__init__(self.size, self.x, self.y)
                    else:
                        self.id = v
                if k == "size":
                    self.size = v
                if k == "x":
                    self.x = v
                if k == "y":
                    self.y = v

    def to_dictionary(self):
        """returns dictionary representation of the class"""
        return {'id': self.id, 'width': self.width,
                'height': self.height, 'x': self.x, 'y': self.y}

    def __str__(self):
        """returns string representation of the class"""
        return "[Square] ({}) {}/{} - {}".format(self.id, self.x,
                                                 self.y, self.width)
