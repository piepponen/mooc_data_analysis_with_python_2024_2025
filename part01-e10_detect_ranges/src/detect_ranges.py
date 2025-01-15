#!/usr/bin/env python3

def detect_ranges(L):
    L_sorted = sorted(L)
    result = []
    
    i = 0
    while i < len(L_sorted):
        start = L_sorted[i]
        end = start
        
        while i + 1 < len(L_sorted) and L_sorted[i + 1] == end + 1:
            end = L_sorted[i + 1]
            i += 1
        
        if end > start:
            result.append((start, end + 1))
        else:
            result.append(start)
        
        i += 1
    
    return result


def main():
    L = [2, 5, 4, 8, 12, 6, 7, 10, 13]
    result = detect_ranges(L)
    print("Input:", L)
    print("Detected ranges:", result)

if __name__ == "__main__":
    main()
