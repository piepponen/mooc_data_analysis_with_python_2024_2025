#!/usr/bin/env python3

def merge(L1, L2):
    """Объединяет два отсортированных списка L1 и L2 в один отсортированный список."""
    i, j = 0, 0  # Индексы для L1 и L2
    merged_list = []

    while i < len(L1) and j < len(L2):
        if L1[i] < L2[j]:
            merged_list.append(L1[i])
            i += 1
        else:
            merged_list.append(L2[j])
            j += 1
    while i < len(L1):
        merged_list.append(L1[i])
        i += 1
    while j < len(L2):
        merged_list.append(L2[j])
        j += 1
    return merged_list


def main():
    L1 = [1, 3, 5, 7]
    L2 = [2, 4, 6, 8]
    print("Merged list:", merge(L1, L2))

    L3 = [10, 20, 30]
    L4 = [5, 15, 25, 35]
    print("Merged list:", merge(L3, L4))

    L5 = []
    L6 = [1, 2, 3]
    print("Merged list:", merge(L5, L6))

    L7 = [1, 2, 3]
    L8 = []
    print("Merged list:", merge(L7, L8))


if __name__ == "__main__":
    main()