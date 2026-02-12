from typing import List
def common_in_three(a: List[int], b: List[int], c: List[int]) -> List[int]:
    i = j = k = 0
    res = []
    last = None

    while i < len(a) and j < len(b) and k < len(c):

        if a[i] == b[j] == c[k]:
            val = a[i]
            if last is None or last != val:
                res.append(val)
                last = val

            while i < len(a) and a[i] == val:
                i += 1
            while j < len(b) and b[j] == val:
                j += 1
            while k < len(c) and c[k] == val:
                k += 1

        else:
            mn = min(a[i], b[j], c[k])

            if a[i] == mn:
                mv = a[i]
                while i < len(a) and a[i] == mv:
                    i += 1
            elif b[j] == mn:
                mv = b[j]
                while j < len(b) and b[j] == mv:
                    j += 1
            else:
                mv = c[k]
                while k < len(c) and c[k] == mv:
                    k += 1

    return res if res else [-1]

if __name__ == "__main__":
    print(common_in_three(
        [1, 5, 10, 20, 40, 80],
        [6, 7, 20, 80, 100],
        [3, 4, 15, 20, 30, 70, 80, 120]
    ))

    print(common_in_three(
        [1, 2, 3, 4, 5],
        [6, 7],
        [8, 9, 10]
    ))

    print(common_in_three(
        [1, 1, 1, 2, 2, 2],
        [1, 1, 2, 2, 2],
        [1, 1, 1, 1, 2, 2, 2, 2]
    ))
