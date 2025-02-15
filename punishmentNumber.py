n = 10

"""
1. Iterate from 1 to 10.
2. For int i, visit digitPartition(i).
3. If digitPartition -> True, add i^2 to res.
4. If False, continue.

"""
from itertools import product

def punishmentNumber(n):
    def digitPartition(n):
    s = str(n * n)
    length = len(s)
    for mask in product([0, 1], repeat=length - 1):
        parts, num = [], s[0]
        for i in range(length - 1):
            if mask[i]:
                parts.append(int(num))
                num = s[i + 1]
            else:
                num += s[i + 1]
        parts.append(int(num))
        if sum(parts) == n:
            return True
    return False
    res = 0
    for i in range(1, n+1):
        if digitPartition(i):
            res+=i**2
    return res

print(punishmentNumber(10))
