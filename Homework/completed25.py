def is_palindrome_array(arr):
    for num in arr:
        s = str(num)
        if s != s[::-1]:
            return False
    return True

arr1 = [111, 222, 333, 444, 555]
print(is_palindrome_array(arr1))

arr2 = [121, 131, 20]
print(is_palindrome_array(arr2))