#!/usr/bin/env python3
# usemodule.py

try:
    from src import triangle
except ModuleNotFoundError:
    import triangle

def main():
    a, b = 3, 4
    
    print(f"Hypotenuse of a triangle with sides {a} and {b}: {triangle.hypotenuse(a, b)}")
    print(f"Area of a triangle with sides {a} and {b}: {triangle.area(a, b)}")

if __name__ == "__main__":
    main()
