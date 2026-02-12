from typing import List
def merge_in_place(a: List[int], b: List[int]) -> None:
    n, m = len(a), len(b)
    total = n + m
    gap = (total + 1) // 2

    while gap > 0:
        i = 0
        j = gap
        while j < total:
            if i < n:
                val_i = a[i]
            else:
                val_i = b[i - n]

            if j < n:
                val_j = a[j]
            else:
                val_j = b[j - n]

            if val_i > val_j:
                if i < n and j < n:
                    a[i], a[j] = a[j], a[i]
                elif i < n and j >= n:
                    a[i], b[j - n] = b[j - n], a[i]
                else:
                    b[i - n], b[j - n] = b[j - n], b[i - n]

            i += 1
            j += 1

        if gap == 1:
            gap = 0
        else:
            gap = (gap + 1) // 2
            
if __name__ == "__main__":
    tests = [
        ([2, 4, 7, 10], [2, 3]),
        ([1, 5, 9, 10, 15, 20], [2, 3, 8, 13]),
        ([0, 1], [2, 3]),
    ]

    for a, b in tests:
        print("Before:")
        print(" a =", a)
        print(" b =", b)
        merge_in_place(a, b)
        print("After:")
        print(" a =", a)
        print(" b =", b)
        print("-" * 40)
