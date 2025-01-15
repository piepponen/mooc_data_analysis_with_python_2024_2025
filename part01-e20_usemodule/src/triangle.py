"""
This module provides functions to calculate properties of a right-angled triangle.
It includes functions for computing the hypotenuse and area of a right triangle.
"""

__version__ = "1.0"
__author__ = "Sofiia Piepponen"

import math

def hypotenuse(a, b):
    """Returns the hypotenuse given two perpendicular sides."""
    return math.sqrt(a**2 + b**2)

def area(a, b):
    """Returns the area of a right-angled triangle given two perpendicular sides."""
    return 0.5 * a * b

