def min_subarray_len(x, arr):
    n = len(arr)
    start = 0
    curr = 0
    best = n + 1
    for end in range(n):
        curr += arr[end]
        while curr > x:
            length = end - start + 1
            if length < best:
                best = length
            curr -= arr[start]
            start += 1
    return 0 if best == n + 1 else best

x1 = 51
arr1 = [1, 4, 45, 6, 0, 19]
print(min_subarray_len(x1, arr1))

x2 = 100
arr2 = [1, 10, 5, 2, 7]
print(min_subarray_len(x2, arr2))