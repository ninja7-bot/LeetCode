nums = [-1,0,3,5,9,12]
target = 9
def binarySearch(nums, target):
    low = 0
    high = len(nums)-1
    
    while low <= high:
        mid = low + (high - low)//2

        if target == nums[mid]:
            return mid

        elif target > nums[mid]:
            low = mid + 1

        else:
            high = mid - 1
    return -1
print(binarySearch(nums, target))
    
