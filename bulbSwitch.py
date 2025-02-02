def bulbSwitch(n):
    LEN = n + 1
    bulbs = [0] * n
    # 0 is OFF.
    # 1 is ON.
    if n == 0:
        return 0
    for i in range(1, LEN):
        if i == 1:
            bulbs = [1 for x in range(n)]
        elif i == 2:
            x = 1
            bulbs[x*2-1] = 0
            x+=1
        elif i == 3:
            x = 1
            bulbs[x*3-1] = 0 if 1 else 1
            x+=1
        elif i == LEN-1:
            print(i, LEN-1, bulbs[i-1])
            bulbs[n-1] = 0 if 1 else 1
        bulbs[i-1] = 0 if 1 else 1
    x = bulbs.count(1)
    return x
print(bulbSwitch(4))

"""
[1, 1, 1, 1]: R1
[1, 0, 1, 1]: R2
[1, 0, 0, 1]: R3
[1, 0, 0, 0]: R4

"""
