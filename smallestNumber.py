def smallestNumber(pattern):
    l = len(pattern)
    res = [0] * (l + 1)
    num = 1  

    def add(idx):
        nonlocal num
        if idx > l:
            return
        
        start = idx
        while start < l and pattern[start] == 'I':
            res[start] = num
            num += 1
            start += 1
        
        end = start
        while end < l and pattern[end] == 'D':
            end += 1
        
        for i in range(end, start - 1, -1):
            res[i] = num
            num += 1
        
        add(end + 1)
    
    add(0)
    return ''.join(map(str, res))

def smallestNumber(self, pattern: str) -> str:
        n = len(pattern)
        stack = []
        result = []
        
        for i in range(n + 1):
            stack.append(str(i + 1))
            if i == n or pattern[i] == 'I':  
                while stack:
                    result.append(stack.pop())
        
        return ''.join(result)

pattern = "IIIDIDDD"
print(smallestNumber(pattern))  # Output: "123549876"
