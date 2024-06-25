def mySqrt(x):
    if x < 2:
        return x

    left, right = 0, x
    result = 0

    while left <= right:
        mid = (left + right) // 2
        if mid * mid <= x:
            result = mid
            left = mid + 1
        else:
            right = mid - 1
    
    return result


print(mySqrt(4))  
print(mySqrt(8))  
print(mySqrt(0))  
print(mySqrt(1))  
print(mySqrt(9))  
print(mySqrt(15))
