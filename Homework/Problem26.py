def median(arr):
    
    if not arr:
        raise ValueError("Cannot compute median of an empty list.")
    a = sorted(arr)
    n = len(a)
    mid = n // 2
    if n % 2:
        med = a[mid]
    else:
        med = (a[mid - 1] + a[mid]) / 2
    if isinstance(med, float) and med.is_integer():
        return int(med)
    return med

print(median([90, 100, 78, 89, 67]))   
print(median([56, 67, 30, 79]))        
print(median([1, 2]))                  