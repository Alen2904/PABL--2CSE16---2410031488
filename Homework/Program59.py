def combination_sum_k(n, k):
    result = []
    
    def backtrack(start, k, target, path):
        if k == 0 and target == 0:
            result.append(path[:])
            return
        
        if k == 0 or target < 0:
            return
        
        for i in range(start, 10):
            path.append(i)
            backtrack(i + 1, k - 1, target - i, path)
            path.pop()
    
    backtrack(1, k, n, [])
    return result


print(combination_sum_k(9, 3))
print(combination_sum_k(3, 3))