from typing import List
def min_jumps(arr: List[int]) -> int:
    
    n = len(arr)
    if n <= 1:
        return 0
    if arr[0] == 0:
        return -1  

    max_reach = arr[0]
    steps = arr[0]
    jumps = 1

    for i in range(1, n):
        
        if i == n - 1:
            return jumps

        max_reach = max(max_reach, i + arr[i])
        steps -= 1

        if steps == 0:
            jumps += 1
            
            if i >= max_reach:
                return -1
            
            steps = max_reach - i
    return -1  

if __name__ == "__main__":
    tests = [
        ([1, 3, 5, 8, 9, 2, 6, 7, 6, 8, 9], 3),
        ([1, 4, 3, 2, 6, 7], 2),
        ([0, 10, 20], -1),
    ]
    for arr, expected in tests:
        out = min_jumps(arr)
        print(f"Input: {arr}")
        print(f"Output: {out}   (expected: {expected})\n")
