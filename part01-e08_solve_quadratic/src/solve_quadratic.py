#!/usr/bin/env python3

import math
import numpy as np

def solve_quadratic(a, b, c):
    discriminant = b**2 - 4*a*c
    root1 = (-b + math.sqrt(discriminant)) / (2 * a)
    root2 = (-b - math.sqrt(discriminant)) / (2 * a)
    return (root1, root2)

def main():
    print(solve_quadratic(1, -3, 2)) 
    print(solve_quadratic(1, 2, 1)) 

if __name__ == "__main__":
    main()

