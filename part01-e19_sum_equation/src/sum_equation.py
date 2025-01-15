#!/usr/bin/env python3

def sum_equation(L):
    if len(L) == 0:
        return "0 = 0"
    equation = " + ".join(map(str, L)) + " = " + str(sum(L))
    return equation

def main():
    print(sum_equation([1, 5, 7]))
    print(sum_equation([]))

if __name__ == "__main__":
    main()
