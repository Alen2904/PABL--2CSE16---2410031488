import heapq

def min_operations(arr):
    max_heap = [-x for x in arr]
    heapq.heapify(max_heap)
    
    total_sum = sum(arr)
    target = total_sum / 2
    
    operations = 0
    
    while total_sum > target:
        largest = -heapq.heappop(max_heap)
        half = largest / 2
        total_sum -= half
        heapq.heappush(max_heap, -half)
        operations += 1
    
    return operations

print(min_operations([8, 6, 2]))
print(min_operations([9, 1, 2]))