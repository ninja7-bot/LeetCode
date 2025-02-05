s1 = "bank"
s2 = "kanb"
def areAlmostEqual(s1, s2):
    if sorted(s1) != sorted(s2):
        return False
    COUNT = 0


    for i in range(len(s1)):
        if s1[i] == s2[i]:
            continue
        elif s1[i] != s2[i]:
            COUNT+=1          
    if COUNT > 2:
        return False
    return True
    


areAlmostEqual(s1, s2)
        
