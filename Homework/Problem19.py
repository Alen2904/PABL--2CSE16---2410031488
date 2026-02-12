from collections import Counter
from typing import List
def is_subset(a: List[int], b: List[int]) -> bool:
    count_a = Counter(a)
    count_b = Counter(b)

    for num in count_b:
        if count_a[num] < count_b[num]:
            return False
    return True

if __name__ == "__main__":
    print(is_subset(
        [11, 7, 1, 13, 21, 3, 7, 3],
        [11, 3, 7, 1, 7]
    ))

    print(is_subset(
        [1, 2, 3, 4, 4, 5, 6],
        [1, 2, 4]
    ))

    print(is_subset(
        [10, 5, 2, 23, 19],
        [19, 5, 3]
    ))
