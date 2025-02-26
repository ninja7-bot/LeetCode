nums = [2,-5,1,-4,3,-2]

def maxAbsoluteSum(nums):
    max_sum = min_sum = 0
    current_max = current_min = 0

    for num in nums:
        current_max = max(num, current_max + num)
        max_sum = max(max_sum, current_max)

        current_min = min(num, current_min + num)
        min_sum = min(min_sum, current_min)

    return max(max_sum, -min_sum)
"""    
    mxx = 0
    n = len(nums)

    for i in range(n):
        for j in range(i + 1, n + 1):
            s = abs(sum(nums[i:j]))
            mxx = max(s, mxx)
    return mxx
"""
        
print(maxAbsoluteSum(nums))
