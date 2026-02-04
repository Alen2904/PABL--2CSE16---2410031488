def rotate_by_one(arr):
    n = len(arr)
    if n <= 1:
        return arr  

    last = arr[-1]           
    for i in range(n - 1, 0, -1):
        arr[i] = arr[i - 1]  
    arr[0] = last            

    return arr  

# example
if __name__ == "__main__":
    a = [1, 2, 3, 4, 5]
    print("before:", a)
    rotate_by_one(a)
    print("after: ", a)  # [5, 1, 2, 3, 4]