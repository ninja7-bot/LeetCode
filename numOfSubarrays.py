#   Input:
arr = [1,2,3,4,5,6,7]
# Output: 16
def numOfSubarrays(arr):
    n = len(arr)
    count = 0

    prefix = [0] * (n + 1)
    for i in range(n):
        prefix[i+1] = prefix[i] + arr[i]
    
    for i in range(n):
        for j in range(i+1, n+1):
            sub_sum = prefix[j] - prefix[i]
            if sub_sum % 2 != 0:
                count += 1
    return count
            


print(numOfSubarrays(arr))
