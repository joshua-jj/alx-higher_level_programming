#!/usr/bin/python3
"""Defines a class square"""


class Square:
    """This is a square class"""

    def __init__(self, size=0):
        """Constructor of the square class"""
        self._size = size

    @property
    def size(self):
        """Getter function of the class"""
        return self._size

    @size.setter
    def size(self, value):
        """Setter function of the class"""
        if type(value) != int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self._size = value

    def area(self):
        """Function that returns the area"""
        return self._size ** 2

    def my_print(self):
        """This funtion prints square"""
        if self._size == 0:
            print()
        else:
            for i in range(self._size):
                print('#' * self._size)
