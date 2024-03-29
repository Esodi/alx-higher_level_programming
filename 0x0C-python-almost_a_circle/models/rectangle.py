#!/usr/bin/python3
"""a module with a  class Rectangle"""
from models.base import Base


class Rectangle(Base):
    '''class Rectangle that inherits from Base'''

    def __init__(self, width, height, x=0, y=0, id=None):
        super().__init__(id)
        if isinstance(width, int):
            if (width > 0):
                self.__width = width
            else:
                raise ValueError("width must be > 0")
        else:
            raise TypeError("width must be an integer")
        if isinstance(height, int):
            if height > 0:
                self.__height = height
            else:
                raise ValueError("height must be > 0")
        else:
            raise TypeError("height must be an integer")
        if isinstance(x, int):
            if x >= 0:
                self.__x = x
            else:
                raise ValueError("x must be >= 0")
        else:
            raise TypeError("x must be an integer")
        if isinstance(y, int):
            if y >= 0:
                self.__y = y
            else:
                raise ValueError("y must be >= 0")
        else:
            raise TypeError("y must be an integer")

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if isinstance(value, int):
            if value > 0:
                self.__width = value
            else:
                raise ValueError("width must be > 0")
        else:
            raise TypeError("width must be an integer")

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if isinstance(value, int):
            if value > 0:
                self.__height = value
            else:
                raise ValueError("height must be > 0")
        else:
            raise TypeError("height must be an integer")

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, value):
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, value):
        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        '''Method that return the area of the rectangle'''
        return self.__width * self.__height

    def display(self):
        '''method that print rectangle using #'''
        print("\n"*self.__y, end='')
        for i in range(self.__height):
            print(" "*self.__x + "#"*self.__width)

    def __str__(self):
        '''__str__ method'''
        return f"[Rectangle] ({self.id}) {self.__x}/{self.__y} - \
{self.__width}/{self.__height}"

    def update(self, *args):
            list(args)
            lst = [self.id, self.__width, self.__height, self.__x, self.__y]
            j = 0
            for i in args:
                lst[j] = i
                j += 1;
