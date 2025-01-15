#!/usr/bin/env python3

def find_matching(L, pattern):
    return [index for index, element in enumerate(L) if pattern in element]

def main():
    result = find_matching(["sensitive", "engine", "rubbish", "comment"], "en")
    print(result)

if __name__ == "__main__":
    main()
