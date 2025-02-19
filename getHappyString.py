n = 3
k = 9

def getHappyString(n, k):
        total = 2 ** (n - 1) 
        if k > 3 * total:
            return "" 
        
        chars = ['a', 'b', 'c']
        result = []
        index = (k - 1) // total 
        result.append(chars[index])
        k = (k - 1) % total + 1

        for i in range(1, n):
            total //= 2
            for ch in chars:
                if ch != result[-1]:
                    if k > total:
                        k -= total
                    else:
                        result.append(ch)
                        break

        return "".join(result)
        
getHappyString(n, k)
