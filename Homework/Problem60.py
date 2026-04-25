def tug_of_war(arr):
    n = len(arr)
    total = sum(arr)
    k = n // 2
    
    best_diff = float('inf')
    best_subset = []
    
    def backtrack(index, count, curr_sum, subset):
        nonlocal best_diff, best_subset
        
        if count == k:
            diff = abs((total - curr_sum) - curr_sum)
            if diff < best_diff:
                best_diff = diff
                best_subset = subset[:]
            return
        
        if index >= n:
            return
        
        subset.append(arr[index])
        backtrack(index + 1, count + 1, curr_sum + arr[index], subset)
        subset.pop()
        
        backtrack(index + 1, count, curr_sum, subset)
    
    backtrack(0, 0, 0, [])
    
    subset1 = best_subset
    subset2 = arr[:]
    
    for x in subset1:
        subset2.remove(x)
    
    return [subset1, subset2]


print(tug_of_war([1, 2, 3, 4]))
print(tug_of_war([5, 10, 15]))