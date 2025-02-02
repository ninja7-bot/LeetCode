def maxSubArray(nums):
    m = len(nums) + 1
    
    if m == 1:
        return nums[0]

    SUM = []
    
    for i in range(m):
        for j in range(i, m):
            if len(nums[i:j]) == 0:
                continue
            print(nums[i:j], sum(nums[i:j]))
            SUM.append(sum(nums[i:j]))
    res = max(SUM)
    return res
print(maxSubArray(nums = [5,4,-1,7,8]))
