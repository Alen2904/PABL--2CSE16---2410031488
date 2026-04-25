def find_pivot(arr):
    left, right = 0, len(arr) - 1
    
    while left < right:
        mid = (left + right) // 2
        if arr[mid] > arr[right]:
            left = mid + 1
        else:
            right = mid
    
    return left


def count_leq(arr, left, right, x):
    ans = left - 1
    
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] <= x:
            ans = mid
            left = mid + 1
        else:
            right = mid - 1
    
    return ans + 1


def count_elements(arr, x):
    n = len(arr)
    pivot = find_pivot(arr)
    
    count = 0
    
    count += count_leq(arr, 0, pivot - 1, x)
    count += count_leq(arr, pivot, n - 1, x)
    
    return count


print(count_elements([4, 5, 8, 1, 3], 6))
print(count_elements([6, 10, 12, 15, 2, 4, 5], 14))