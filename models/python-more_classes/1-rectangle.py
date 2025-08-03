#!/usr/bin/python3
"""Defines a Rectangle class with width and height attributes."""


class Rectangle:
    """Represents a rectangle with validated width and height."""

    def __init__(self, width=0, height=0):
        """Initialize a new Rectangle with width and height."""
        self.__width = 0  # Ensure __width exists before setter call
        self.__height = 0  # Ensure __height exists before setter call
        self.height = height
        self.width = width

    @property
    def width(self):
        """Retrieve the width of the rectangle."""
        return self.__width

    @width.setter
    def width(self, value):
        """Set the width with validation."""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Retrieve the height of the rectangle."""
        return self.__height

    @height.setter
    def height(self, value):
        """Set the height with validation."""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
