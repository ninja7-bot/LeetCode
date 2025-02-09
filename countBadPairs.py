nums = [1,2,3,4,5]
from collections import defaultdict


def countBadPairs(nums):
    count_good_pairs = 0
    freq_map = defaultdict(int)

    for j in range(len(nums)):
        diff = nums[j] - j
        count_good_pairs += freq_map[diff]
        freq_map[diff] += 1

    n = len(nums)
    total_pairs = n * (n - 1) // 2
    count_bad_pairs = total_pairs - count_good_pairs

    return count_bad_pairs

countBadPairs(nums)    
