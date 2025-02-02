def twoSum(l1, l2):
    s = []
    index = 1
    carry = 0

    LEN = max(len(l1), len(l2))

    for index in range(LEN, 0, -1):
        val_1 = 0 if not index else l1[index]
        val_2 = 0 if not index else l2[index]
        s = val_1 + val_2
    print(s)
    return s
twoSum([9,9,9,9,9,9,9], [9,9,9,9])    
