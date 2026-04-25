def max_visible(arr):
    n = len(arr)
    
    left = [0] * n
    right = [0] * n
    
    stack = []
    
    for i in range(n):
        count = 0
        while stack and arr[stack[-1]] < arr[i]:
            count += left[stack[-1]] + 1
            stack.pop()
        
        left[i] = count
        stack.append(i)
    
    stack = []
    
    for i in range(n - 1, -1, -1):
        count = 0
        while stack and arr[stack[-1]] < arr[i]:
            count += right[stack[-1]] + 1
            stack.pop()
        
        right[i] = count
        stack.append(i)
    
    ans = 0
    for i in range(n):
        ans = max(ans, left[i] + right[i] + 1)
    
    return ans


print(max_visible([6, 2, 5, 4, 5, 1, 6]))