def canJump(nums):
    max_reach = 0
    
    for i, num in enumerate(nums):
        if i > max_reach:
            return False
        max_reach = max(max_reach, i + num)
    
    return max_reach >= len(nums) - 1


print(canJump([2, 3, 1, 1, 4])) 
print(canJump([3, 2, 1, 0, 4])) 
