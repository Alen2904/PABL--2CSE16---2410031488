def min_jumps(arr):
    n = len(arr)
    if n == 0:
        return -1
    if n == 1:
        return 0

    jumps = 0         
    curr_end = 0      
    furthest = 0      

    for i in range(n - 1):
        
        furthest = max(furthest, i + arr[i])

        if i == curr_end:
        
            if furthest <= i:
                return -1
            jumps += 1
            curr_end = furthest
            
            if curr_end >= n - 1:
                break

    return jumps if curr_end >= n - 1 else -1


# examples / quick checks
if __name__ == "__main__":
    a = [1, 3, 5, 8, 9, 2, 6, 7, 6, 8, 9]
    print("input:", a)
    print("min jumps:", min_jumps(a)) 
    print(min_jumps([2, 1, 0, 3]))     
    print(min_jumps([0]))              
    print(min_jumps([]))