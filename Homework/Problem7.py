def max_subarray_sum(arr):
    if not arr:
        raise ValueError("arr must contain at least one element")
    max_ending = arr[0]   
    max_so_far = arr[0]   
    
    for x in arr[1:]:
        
        if max_ending + x < x:
            max_ending = x
        else:
            max_ending = max_ending + x

        if max_ending > max_so_far:
            max_so_far = max_ending

    return max_so_far


# example
if __name__ == "__main__":
    a = [2, 3, -8, 7, -1, 2, 3]
    print("input: ", a)
    print("max subarray sum:", max_subarray_sum(a))  