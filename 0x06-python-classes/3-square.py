#!/usr/bin/python3
"""Defines a class square"""


class Square:
    """This is a square class"""

    def __init__(self, size=0):
        """Constructor of the square class"""
        if type(size) != int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    def area(self):
        """Function that returns the area"""
        return self.__size ** 2
