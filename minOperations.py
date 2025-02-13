"""
nums = [2,11,10,1,3]
k = 10


def minOperations(nums, k):
    def check(nums):
        for num in nums:
            if num<k:
                return False
        return True
    count = 0
    while not(check(nums)):
        sm = min(nums)
        nums.remove(sm)
        s_sm = min(nums)
        nums.remove(s_sm)

        val = sm * 2 + s_sm
        count+=1
        nums.append(val)
        check(nums)
    return count

print(minOperations(nums, k))
"""    
import time
import random
import heapq
from typing import List

class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        heapq.heapify(nums)

        count = 0
        while nums[0] < k:
            sm = heapq.heappop(nums)
            s_sm = heapq.heappop(nums)

            val = sm * 2 + s_sm
            count += 1
            heapq.heappush(nums, val)
        return count

# Generate large test cases
def generate_test_case(size, min_val, max_val, k):
    """Generates a list of random numbers with given size and range."""
    return [random.randint(min_val, max_val) for _ in range(size)], k

# Test case sizes
test_cases = {
    "Small (1K)": generate_test_case(10**3, 1, 10**3, 500),
    "Medium (10K)": generate_test_case(10**4, 1, 10**4, 5000),
    "Large (100K)": generate_test_case(10**5, 1, 10**5, 50000),
    "Huge (1M)": generate_test_case(10**6, 1, 10**6, 500000),
}

# Benchmark function
def benchmark(func, nums, k):
    start_time = time.time()
    result = func(nums, k)
    end_time = time.time()
    return end_time - start_time, result

# Run benchmarks
solution = Solution()

print("\n===== Benchmarking minOperations() =====\n")
for test_name, (nums, k) in test_cases.items():
    print(f"\n🏆 Running benchmark for {test_name} 🏆")
    
    nums_copy = nums[:]  # Avoid modifying original test cases
    time_taken, result = benchmark(solution.minOperations, nums_copy, k)
    
    print(f"Execution Time: {time_taken:.5f} seconds | Operations: {result}")

