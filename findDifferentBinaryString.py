nums = ["111","011","001"]
def findDifferentBinaryString(nums):
    l = len(nums[0])
    nums_set = set(nums)
    
    for i in range(2**l):
        candidate = format(i, '0{}b'.format(l))
        if candidate not in nums_set:
            return candidate
print(findDifferentBinaryString(nums))
