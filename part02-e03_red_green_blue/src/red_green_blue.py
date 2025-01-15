#!/usr/bin/env python3

import re

def red_green_blue(filename="src/rgb.txt"):
    with open(filename, "r", encoding="utf-8") as f:
        lines = f.readlines()[1:]  # Пропускаем заголовок

    result = []
    for line in lines:
        match = re.findall(r'(\d+)\s+(\d+)\s+(\d+)\s+(.+)', line.strip())
        if match:
            r, g, b, name = match[0]
            result.append(f"{r}\t{g}\t{b}\t{name}")

    return result

def main():
    for entry in red_green_blue():
        print(entry)

if __name__ == "__main__":
    main()

