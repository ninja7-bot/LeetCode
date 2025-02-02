from collections import Counter
s= "loveleetcode"
def firstUniqChar(s):
    freq = Counter(s)
    for key, val in freq.items():
        if val == 1:
            res = s.index(key)
            return res
    return -1
        

    
print(firstUniqChar(s))
