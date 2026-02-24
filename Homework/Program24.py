def min_swaps(arr, k):
    n = len(arr)
    count = 0
    for num in arr:
        if num <= k:
            count += 1
    bad = 0
    for i in range(count):
        if arr[i] > k:
            bad += 1
    ans = bad
    i = 0
    j = count
    while j < n:
        if arr[i] > k:
            bad -= 1
        if arr[j] > k:
            bad += 1
        if bad < ans:
            ans = bad
        i += 1
        j += 1
    return ans

arr1 = [2, 1, 5, 6, 3]
k1 = 3
print(min_swaps(arr1, k1))

arr2 = [2, 7, 9, 5, 8, 7, 4]
k2 = 6
print(min_swaps(arr2, k2))

arr3 = [2, 4, 5, 3, 6, 1, 8]
k3 = 6
print(min_swaps(arr3, k3))