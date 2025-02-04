nums = [1,4,3,3,2]

def longestMonotonicSubarray(nums):
    if not nums:
        return 0

    L = len(nums)
    max_length = 1
    inc = dec = 1

    for i in range(1, L):
        if nums[i] > nums[i - 1]:
            inc += 1
            dec = 1
        elif nums[i] < nums[i - 1]:
            dec += 1
            inc = 1
        else:  # nums[i] == nums[i - 1]
            inc = dec = 1

        max_length = max(max_length, inc, dec)

    return max_length

print(longestMonotonicSubarray(nums))
