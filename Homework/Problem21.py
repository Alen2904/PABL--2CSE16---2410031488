def min_chocolate_diff(arr, m):
    n = len(arr)
    if m == 0 or n == 0:
        return 0
    if m > n:
        return -1
    arr.sort()
    min_diff = float('inf')
    for i in range(n - m + 1):
        diff = arr[i + m - 1] - arr[i]
        if diff < min_diff:
            min_diff = diff
    return min_diff

arr1 = [3, 4, 1, 9, 56, 7, 9, 12]
m1 = 5
print(min_chocolate_diff(arr1, m1))

arr2 = [7, 3, 2, 4, 9, 12, 56]
m2 = 3
print(min_chocolate_diff(arr2, m2))

arr3 = [3, 4, 1, 9, 56]
m3 = 5
print(min_chocolate_diff(arr3, m3))