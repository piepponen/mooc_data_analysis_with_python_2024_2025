#!/usr/bin/env python3

import re

def file_listing(filename="src/listing.txt"):
    with open(filename, "r", encoding="utf-8") as f:
        return [
            (int(size), month, int(day), int(hour), int(minute), filename)
            for size, month, day, hour, minute, filename in 
            re.findall(r'\S+\s+\d+\s+\S+\s+\S+\s+(\d+)\s+(\w+)\s+(\d+)\s+(\d+):(\d+)\s+(.+)', f.read())
        ]

def main():
    for entry in file_listing():
        print(entry)

if __name__ == "__main__":
    main()
