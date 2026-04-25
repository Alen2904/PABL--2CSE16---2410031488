def get_min(matrix, r1, c1, r2, c2):
    # If invalid section
    if r1 > r2 or c1 > c2:
        return None
    
    mn = float('inf')
    for i in range(r1, r2 + 1):
        for j in range(c1, c2 + 1):
            mn = min(mn, matrix[i][j])
    
    return mn


def footpath_cost(matrix, queries):
    n = len(matrix)
    m = len(matrix[0])
    
    results = []
    
    for R, C in queries:
        # Convert to 0-based
        R -= 1
        C -= 1
        
        total = 0
        
        # Top-left
        mn = get_min(matrix, 0, 0, R-1, C-1)
        if mn is not None:
            total += mn
        
        # Top-right
        mn = get_min(matrix, 0, C+1, R-1, m-1)
        if mn is not None:
            total += mn
        
        # Bottom-left
        mn = get_min(matrix, R+1, 0, n-1, C-1)
        if mn is not None:
            total += mn
        
        # Bottom-right
        mn = get_min(matrix, R+1, C+1, n-1, m-1)
        if mn is not None:
            total += mn
        
        results.append(total)
    
    return results


# Example 1
matrix1 = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]
queries1 = [[2,2]]

print(footpath_cost(matrix1, queries1))  # Output: [20]


# Example 2
matrix2 = [
    [1,2,3,4],
    [5,6,7,8],
    [1,2,3,4]
]
queries2 = [[3,4]]

print(footpath_cost(matrix2, queries2))  # Output: [1]