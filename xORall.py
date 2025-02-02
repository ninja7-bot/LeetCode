def xOR(nums1, nums2):
    xor1, xor2 = 0, 0
    for num in nums1:
        xor1 ^= num
    for num in nums2:
        xor2 ^= num
    return (xor1 * (len(nums2) % 2)) ^ (xor2 * (len(nums1) % 2))     

print(xOR([2,1,3], [10,2,5,0]))
