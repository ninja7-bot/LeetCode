nums = [1,2,4,5,10]
def tupleSameProduct(nums):
    L = len(nums)
    D = {}
    for i in range(L):
        for j in range(i+1, L):
            val = nums[i] * nums[j]
            D[val] = D.get(val, 0) + 1
    print(D)
    result = 0
    for count in D.values():
        if count >= 2:
            result += (count * (count - 1) // 2) * 8

    return result

            

        
    


tupleSameProduct(nums)
