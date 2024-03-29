#!/usr/bin/python3
"""Module for class Rectangle"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """class Square which inherits from Rectangle"""
    def __init__(self, size):
        """new instance of Rectangle

        Args:
            size: size of square
        """
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def area(self):
        return self.__size ** 2
