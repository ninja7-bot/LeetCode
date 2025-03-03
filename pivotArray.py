nums = [9,12,5,10,14,3,10]
pivot = 10

def pivotArray(nums, pivot):
    left = []   
    middle = [] 
    right = []  

    for num in nums:
        if num < pivot:
            left.append(num)
        elif num > pivot:
            right.append(num)
        else:
            middle.append(num)
    
    return left + middle + right
pivotArray(nums, pivot)
