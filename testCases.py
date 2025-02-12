import time
import random
from collections import defaultdict

# Generate large test cases
def generate_test_case(size, num_digits):
    """Generates a list of random numbers with given size and digit length."""
    lower_bound = 10**(num_digits - 1)  # Smallest number with num_digits
    upper_bound = 10**num_digits - 1    # Largest number with num_digits
    return [random.randint(lower_bound, upper_bound) for _ in range(size)]

# Large test cases
small_test = generate_test_case(10**3, 6)   # 1,000 numbers
medium_test = generate_test_case(10**4, 6)  # 10,000 numbers
large_test = generate_test_case(10**5, 6)   # 100,000 numbers
huge_test = generate_test_case(10**6, 6)    # 1,000,000 numbers

# 1️⃣ List Comprehension Approach
def maxSum_list_comprehension(nums):
    hashMap = defaultdict(list)
    res = -1

    for num in nums:
        digit_sum = sum([int(i) for i in str(num)])  # List comprehension (slow)
        hashMap[digit_sum].append(num)

    for values in hashMap.values():
        if len(values) > 1:
            values.sort(reverse=True)
            res = max(res, values[0] + values[1])

    return res

# 2️⃣ Generator Expression Approach
def maxSum_generator_expression(nums):
    hashMap = defaultdict(list)
    res = -1

    for num in nums:
        digit_sum = sum(int(i) for i in str(num))  # Generator expression (faster)
        hashMap[digit_sum].append(num)

    for values in hashMap.values():
        if len(values) > 1:
            values.sort(reverse=True)
            res = max(res, values[0] + values[1])

    return res

# 3️⃣ Function Approach with Generator Expression
def digit_sum(n):
    return sum(int(i) for i in str(n))

def maxSum_function(nums):
    hashMap = defaultdict(list)
    res = -1

    for num in nums:
        digit_sum_value = digit_sum(num)  # Function call (optimized)
        hashMap[digit_sum_value].append(num)

    for values in hashMap.values():
        if len(values) > 1:
            values.sort(reverse=True)
            res = max(res, values[0] + values[1])

    return res

# 4️⃣ Function Approach with map()
def digit_sum_map(n):
    return sum(map(int, str(n)))

def maxSum_function_map(nums):
    hashMap = defaultdict(list)
    res = -1

    for num in nums:
        digit_sum_value = digit_sum_map(num)  # Function with map() (alternative optimization)
        hashMap[digit_sum_value].append(num)

    for values in hashMap.values():
        if len(values) > 1:
            values.sort(reverse=True)
            res = max(res, values[0] + values[1])

    return res

# Benchmark function
def benchmark(func, nums):
    start_time = time.time()
    result = func(nums)
    end_time = time.time()
    print(f"{func.__name__}: {end_time - start_time:.5f} seconds | Result: {result}")

# Run benchmarks
print("\n===== Benchmarking Different Digit Sum Approaches =====\n")

test_cases = [
    ("Small Test (1K numbers)", small_test),
    ("Medium Test (10K numbers)", medium_test),
    ("Large Test (100K numbers)", large_test),
    ("Huge Test (1M numbers)", huge_test),
]

for test_name, test_case in test_cases:
    print(f"\n🏆 Running benchmarks for {test_name} 🏆\n")
    benchmark(maxSum_list_comprehension, test_case)
    benchmark(maxSum_generator_expression, test_case)
    benchmark(maxSum_function, test_case)
    benchmark(maxSum_function_map, test_case)
