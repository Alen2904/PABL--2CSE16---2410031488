from collections import defaultdict

def count_pairs_optimized(arr):
    count = 0
    m = len(arr[0])
    
    for i in range(m):
        freq = defaultdict(int)
        
        for s in arr:
            pattern = s[:i] + '*' + s[i+1:]
            count += freq[pattern]
            freq[pattern] += 1
    
    return count


print(count_pairs_optimized(["abc", "abd", "bbd"]))
print(count_pairs_optimized(["bcde", "bced", "bdce"]))
print(count_pairs_optimized(["def", "deg", "dmf", "xef", "dxg"]))