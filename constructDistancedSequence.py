
n = 3

def constructDistancedSequence(n):
    size = 2 * n - 1
    result = [0] * size
    used = set()

    def backtrack(index):
        if index == size:
            return True 
        
        if result[index] != 0:
            return backtrack(index + 1) 
        
        for num in range(n, 1, -1): 
            if num in used:
                continue
            if index + num < size and result[index] == 0 and result[index + num] == 0:
                result[index] = result[index + num] = num
                used.add(num)
                
                if backtrack(index + 1):
                    return True
                
                result[index] = result[index + num] = 0
                used.remove(num)
        
        if 1 not in used:
            result[index] = 1
            used.add(1)
            
            if backtrack(index + 1):
                return True
            
            result[index] = 0
            used.remove(1)
        
        return False

    backtrack(0)
    return result

print(constructDistancedSequence(n))
