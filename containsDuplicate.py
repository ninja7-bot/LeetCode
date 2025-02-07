nums = [1,2,3,1]
from collections import Counter

def containsDuplicate(nums):
    C = Counter(nums)
    for count in C.values():
        print(count)
        if count>=2:
            return False
    return True
containsDuplicate(nums)
