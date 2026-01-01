def binary_search(arr, x):
    low = 0
    high = len(arr) - 1
    mid = 0
    
    result = -1
    iter_n = 0
 
    while low <= high:
 
        mid = (high + low) // 2
 
        if arr[mid] < x:
            low = mid + 1
            iter_n += 1
 
        elif arr[mid] > x:
            high = mid - 1
            result = mid
            iter_n += 1
 
        else:
            return mid
 
    return iter_n, result
