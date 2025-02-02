NUMS = [6,10,6]
# A[i] == B[(i+x) % A.length]

def checkSort(nums):
    LENGTH = len(nums)
    SORTED = sorted(nums)
    ROTATION = 0
    for i in range(LENGTH):
        for j in range(LENGTH):
            A = SORTED[j]
            B = nums[(j + ROTATION) % LENGTH]
            if A != B:
                ROTATION += 1
                
    for i in range(LENGTH):
        A = SORTED[i]
        B = nums[(i + ROTATION) % LENGTH]
        if A != B:
            return False
    return True

# A: sorted_nums
# B: nums
"""
1. Array ko sort karo.
2. Sorted array ke 1st element ko compare karo OG Array se.
3. Find the index of the 1st Element in OG Array.
4. Set ROTATION to that index.
5. Check if OGARRAY[:ROTATION] is SORTED AND OGARRAY[ROTATION:]
    is SORTED.
"""


def check(nums):
    LENGTH = len(nums)
    SORTED = sorted(nums)
    ROTATION = 0

    for i in range(-1, 0):
        if nums[i] == SORTED[0]:
            ROTATION = nums.index(nums[i])
            continue
    print(ROTATION)
    res = True
    for i in range(LENGTH):
        A = SORTED[i]
        B = nums[(i + ROTATION) % LENGTH]
        if A != B:
            res = False
            continue
    return res

print(checkSort(NUMS))
