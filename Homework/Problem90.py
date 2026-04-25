def largest_after_k_deletions(s, k):
    stack = []
    
    for ch in s:
        while stack and k > 0 and stack[-1] < ch:
            stack.pop()
            k -= 1
        stack.append(ch)
    
    while k > 0:
        stack.pop()
        k -= 1
    
    return "".join(stack)


print(largest_after_k_deletions("ritz", 2))
print(largest_after_k_deletions("zebra", 3))