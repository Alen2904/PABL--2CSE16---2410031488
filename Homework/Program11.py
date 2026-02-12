import random
from typing import List
def kth_smallest(arr: List[int], k: int) -> int:
    n = len(arr)
    if not 1 <= k <= n:
        raise ValueError("k must be between 1 and len(arr)")

    left, right = 0, n - 1
    k_rel = k  
    while left <= right:
        p = random.randint(left, right)
        arr[p], arr[right] = arr[right], arr[p]
        pivot = arr[right]
        store = left
        
        for j in range(left, right):
            if arr[j] < pivot:
                arr[store], arr[j] = arr[j], arr[store]
                store += 1

        arr[store], arr[right] = arr[right], arr[store]
        rank = store - left + 1

        if k_rel == rank:
            return arr[store]
        if k_rel < rank:
            
            right = store - 1
        else:
            
            k_rel -= rank
            left = store + 1

    raise RuntimeError("Quickselect failed")

if __name__ == "__main__":
    tests = [
        ([10, 5, 4, 3, 48, 6, 2, 33, 53, 10], 4),  
        ([7, 10, 4, 3, 20, 15], 3),                 
    ]

    for arr, k in tests:
        a = arr.copy()
        print(f"Input: arr = {arr}, k = {k}")
        print("Output:", kth_smallest(a, k))
        print()

    
