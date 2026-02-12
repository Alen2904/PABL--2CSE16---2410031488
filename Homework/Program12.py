from typing import List
def minimize_diff(heights: List[int], k: int) -> int:
    n = len(heights)
    if n <= 1:
        return 0

    heights.sort()
    ans = heights[-1] - heights[0]

    for i in range(1, n):
        
        if heights[i] - k < 0:
            
            continue
        curr_min = min(heights[0] + k, heights[i] - k)
        curr_max = max(heights[i-1] + k, heights[-1] - k)
        ans = min(ans, curr_max - curr_min)

    return ans

if __name__ == "__main__":
    tests = [
        (2, [1, 5, 8, 10], 5),
        (3, [3, 9, 12, 16, 20], 11),
    ]

    for k, arr, expected in tests:
        res = minimize_diff(arr.copy(), k)
        print(f"k = {k}, arr = {arr}")
        print(f"Output: {res}    (expected: {expected})\n")

    