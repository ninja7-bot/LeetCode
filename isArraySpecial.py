nums = [2,1,4]

def isArraySpecial(nums):
    l = len(nums) - 1 
    for i in range(l):
        print(nums[i], nums[i+1])
        if (nums[i]%2 == 0 and nums[i + 1]%2 != 0) or (nums[i]%2 != 0 and nums[i + 1]%2 == 0):
                continue
        else:
            return False
    return True
print(isArraySpecial(nums))
    
