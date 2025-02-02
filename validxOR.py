def validxOR(d):
    n = len(d)
    og = [0] * n
    ogg = [0] * n
    for i in range(n):
        if i == n-1:
            if d[i] == 0:
                if og[i] == 0 and og[0] == 0:
                    continue
                elif og[i] == 1 and og[0] == 1:
                    continue
            else:
                if og[i] == 0 and og[0] == 1:
                    continue
                elif og[i] == 1 and og[0] == 0:
                    continue
        if d[i] == 0 and i < n-1:
            if og[i] == 0:
                og[i+1] = 0
            elif og[i] == 1:
                og[i+1] = 1
        elif d[i] == 1 and i < n-1:
            if og[i] == 0:
                og[i+1] = 1
            elif og[i] == 1:
                og[i+1] = 0
            else:
                og[i+1]
    for i in range(n):
        if i == n-1:
            if d[i] == og[i] ^ og[0]:
                return True
            else:
                return False
        if d[i] == og[i] ^ og[i+1]:
            continue
        else:
            return False
    return True
            
print(validxOR([1,0,1]))

