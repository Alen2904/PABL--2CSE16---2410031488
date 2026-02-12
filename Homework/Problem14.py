from typing import List
def find_duplicate(nums: List[int]) -> int:
    
    tortoise = nums[0]
    hare = nums[0]
    while True:
        tortoise = nums[tortoise]
        hare = nums[nums[hare]]
        if tortoise == hare:
            break

    p1 = nums[0]
    p2 = tortoise
    while p1 != p2:
        p1 = nums[p1]
        p2 = nums[p2]

    return p1

if __name__ == "__main__":
    tests = [
        ([1, 3, 4, 2, 2], 2),
        ([3, 1, 3, 4, 2], 3),
        ([3, 3, 3, 3, 3], 3),
    ]

    for arr, expected in tests:
        out = find_duplicate(arr)
        print(f"Input: {arr}")
        print(f"Output: {out}   (expected: {expected})\n")
