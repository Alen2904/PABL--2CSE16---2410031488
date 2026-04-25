def previous_smaller(arr):
    stack = []
    result = []
    
    for x in arr:
        while stack and stack[-1] >= x:
            stack.pop()
        
        if stack:
            result.append(stack[-1])
        else:
            result.append(-1)
        
        stack.append(x)
    
    return result


print(previous_smaller([1, 6, 2]))
print(previous_smaller([1, 5, 0, 3, 4, 5]))