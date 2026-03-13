```python
# Module docstring
"""
This module provides a simple calculator with basic arithmetic operations.
"""

import math

def calculate_area(length, width):
    """
    Calculates the area of a rectangle.

    Args:
        length (float): The length of the rectangle.
        width (float): The width of the rectangle.

    Returns:
        float: The area of the rectangle.
    """
    return length * width

def calculate_perimeter(length, width):
    """
    Calculates the perimeter of a rectangle.

    Args:
        length (float): The length of the rectangle.
        width (float): The width of the rectangle.

    Returns:
        float: The perimeter of the rectangle.
    """
    return 2 * (length + width)

def calculate_distance(x1, y1, x2, y2):
    """
    Calculates the Euclidean distance between two points.

    Args:
        x1 (float): The x-coordinate of the first point.
        y1 (float): The y-coordinate of the first point.
        x2 (float): The x-coordinate of the second point.
        y2 (float): The y-coordinate of the second point.

    Returns:
        float: The Euclidean distance between the two points.
    """
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

def calculate_circle_area(radius):
    """
    Calculates the area of a circle.

    Args:
        radius (float): The radius of the circle.

    Returns:
        float: The area of the circle.
    """
    return math.pi * radius ** 2

def calculate_circle_circumference(radius):
    """
    Calculates the circumference of a circle.

    Args:
        radius (float): The radius of the circle.

    Returns:
        float: The circumference of the circle.
    """
    return 2 * math.pi * radius

class Calculator:
    """
    A simple calculator class with basic arithmetic operations.
    """

    def __init__(self):
        """
        Initializes the calculator.
        """
        pass

    def add(self, num1, num2):
        """
        Adds two numbers.

        Args:
            num1 (float): The first number.
            num2 (float): The second number.

        Returns:
            float: The sum of the two numbers.
        """
        return num1 + num2

    def subtract(self, num1, num2):
        """
        Subtracts the second number from the first.

        Args:
            num1 (float): The first number.
            num2 (float): The second number.

        Returns:
            float: The difference between the two numbers.
        """
        return num1 - num2

    def multiply(self, num1, num2):
        """
        Multiplies two numbers.

        Args:
            num1 (float): The first number.
            num2 (float): The second number.

        Returns:
            float: The product of the two numbers.
        """
        return num1 * num2

    def divide(self, num1, num2):
        """
        Divides the first number by the second.

        Args:
            num1 (float): The dividend.
            num2 (float): The divisor.

        Returns:
            float: The quotient of the two numbers.

        Raises:
            ZeroDivisionError: If the divisor is zero.
        """
        if num2 == 0:
            raise ZeroDivisionError("Cannot divide by zero.")
        return num1 / num2

# Example usage:
calculator = Calculator()
print("Area of rectangle:", calculate_area(5, 3))
print("Perimeter of rectangle:", calculate_perimeter(5, 3))
print("Distance between points:", calculate_distance(1, 2, 4, 6))
print("Area of circle:", calculate_circle_area(5))
print("Circumference of circle:", calculate_circle_circumference(5))
print("Sum:", calculator.add(2, 3))
print("Difference:", calculator.subtract(5, 2))
print("Product:", calculator.multiply(4, 5))
print("Quotient:", calculator.divide(10, 2))
```