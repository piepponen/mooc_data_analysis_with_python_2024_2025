#!/usr/bin/env python3

import re

def integers_in_brackets(s):
    return [int(m.group(1)) for m in re.finditer(r'\[\s*([+-]?\d+)\s*\]', s)]

def main():
    test_cases = [
        (" afd [asd] [12 ] [a34] [ -43 ]tt [+12]xxx", [12, -43, 12]),
        ("[100] [-200] [ 300 ]", [100, -200, 300]),
        ("[abc] [ 42] [ -7 ] [0]", [42, -7, 0]),
        ("[+5] [ -6] [7 ] [ 8] [-9]", [5, -6, 7, 8, -9]),
        ("no brackets here", [])
    ]
    
    for s, expected in test_cases:
        assert integers_in_brackets(s) == expected
    
    print("All tests passed.")

if __name__ == "__main__":
    main()

