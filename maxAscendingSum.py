NUMS = [
    [5,5,6,6,6,9,1,2]],
    [10,20,30,40,50],
    [12,17,15,13,10,11,12],
    [6],
    [6,10,6],
    [100,10,1],
    [6,7,7,5],
    [7,9,1,1,1,3],
    [5,5,6,6,6,9,1,2],
    [3,6,10,1,8,9,9,8,9],
    [47,28,59,19,47,2,25,52,29,19,36,6,98,47,76,60,17,91,1,45,100,6,41,48,74,59,84,57,82,25,88,97,91,58,18,22,51,93,93,39,99,36,1,72,27,55,36,91,29,62,77,31,21,49,87,47,9,84,9,65,72,85,31,19,71,37,95,7,41,98,69,76,86,68,64,78,11,31,14,29,92,33,11,64]
]

def maxAscendingSum(nums):
    l = len(nums)
    max_sum = 0
    SUM = nums[0]
    for i in range(1, l):
        if nums[i] > nums[i-1]:
            SUM += nums[i]
        else:
            max_sum = max(SUM, max_sum)
            SUM = nums[i]
    max_sum = max(SUM, max_sum)
    return max_sum
            
        
for num in NUMS:
    print(maxAscendingSum(num))
