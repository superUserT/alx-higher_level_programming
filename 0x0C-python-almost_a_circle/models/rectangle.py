#!/usr/bin/python3
"""A base Class for the model Rectangle"""
from models.base import Base


class Rectangle(Base):
    """Represents the base model"""
    def __init__(self, width, height, x=0, y=0, id=None):
        """Initialize a new Base"""
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """get width"""
        return self.__width

    @width.setter
    def width(self, value):
        """Assignment - Type and value validation width"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """get height"""
        return self.__height

    @height.setter
    def height(self, value):
        """Assignment - Type and value validation for height"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value <= 0:
            raise ValueError("width must be > 0")
        self.__height = value

    @property
    def x(self):
        """Gets x"""
        return self.__x

    @x.setter
    def x(self, value):
        """Assignment - Type and value validation for x"""
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        elif value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """Gets y"""
        return self.__y

    @y.setter
    def y(self, value):
        """Assignment - Type and value validation for y"""
        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        elif value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """Returns area of a rectangle"""
        return self.__height * self.__width

    def display(self):
        """Print the rectangle using '#' characters with x and y offsets"""
        if self.__width <= 0 or self.__height <= 0:
            print()
            return

        for i in range(self.y):
            print()
        for i in range(self.height):
            print(' ' * self.x + '#' * self.width)

    def __str__(self):
        """Returns rectangle description"""
        name = str(self.__class__.__name__)
        id = str(self.id)
        w = str(self.__width)
        h = str(self.__height)
        x = str(self.__x)
        y = str(self.__y)

        return f"[{name}] ({id}) {x}/{y} - {w}/{h}"

    def to_dictionary(self):
        """Returns the dict representation of a rectangle"""
        return {
            "id": self.id,
            "width": self.__width,
            "height": self.__height,
            "x": self.__x,
            "y": self.__y
        }

    def update(self, *args, **kwargs):
        """Assigns an argument to each attribute"""
        attrs = ["id", "width", "height", "x", "y"]
        if len(args) != 0:
            for i in range(len(args)):
                setattr(self, attrs[i], args[i])
        elif len(kwargs) != 0:
            for key, value in kwargs.items():
                setattr(self, key, value)
