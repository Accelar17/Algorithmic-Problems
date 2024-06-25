def nextGreaterElement(nums1, nums2):
    next_greater = {}
    stack = []
    
    for num in reversed(nums2):
        while stack and stack[-1] <= num:
            stack.pop()
        next_greater[num] = stack[-1] if stack else -1
        stack.append(num)
    
    return [next_greater[num] for num in nums1]


nums1 = [4, 1, 2]
nums2 = [1, 3, 4, 2]
print(nextGreaterElement(nums1, nums2)) 

nums1 = [2, 4]
nums2 = [1, 2, 3, 4]
print(nextGreaterElement(nums1, nums2)) 
