nums = [4,6,10,6]
from collections import defaultdict

def maximumSum(nums):
    
    def digitSum(num: int)->int:
        digit_sum = 0
        while num:
            digit_sum += num % 10
            num //= 10
        return digit_sum
    
    hashMap = defaultdict(list)
    pairs = []
    
    for num in nums:
        digit_sum = digitSum(num)
        hashMap[digit_sum].append(num)

    res = -1

    for values in hashMap.values():
        if len(values) > 1:
            values.sort(reverse=True)
            res = max(res, values[0] + values[1])

    return res        


print(maximumSum(nums))
