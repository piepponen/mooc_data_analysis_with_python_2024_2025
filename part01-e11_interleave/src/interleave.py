#!/usr/bin/env python3
def interleave(*lists):
    result = []
    for items in zip(*lists):
        result.extend(items)
    return result

def main():
    result = interleave([1, 2, 3], [20, 30, 40], ['a', 'b', 'c'])
    print(result)

if __name__ == "__main__":
    main()
