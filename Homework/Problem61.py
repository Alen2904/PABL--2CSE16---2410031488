def can_place(arr, k, dist):
    count = 1
    last = arr[0]
    
    for i in range(1, len(arr)):
        if arr[i] - last >= dist:
            count += 1
            last = arr[i]
            if count >= k:
                return True
    
    return False


def max_min_diff(arr, k):
    arr.sort()
    
    left = 0
    right = arr[-1] - arr[0]
    ans = 0
    
    while left <= right:
        mid = (left + right) // 2
        
        if can_place(arr, k, mid):
            ans = mid
            left = mid + 1
        else:
            right = mid - 1
    
    return ans


print(max_min_diff([2, 6, 2, 5], 3))
print(max_min_diff([1, 4, 9, 0, 2, 13, 3], 4))