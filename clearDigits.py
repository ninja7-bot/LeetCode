s = "cb34"
def clearDigits(s):
        res = []
        for char in s:
            if char.isdigit():
                if res:
                    res.pop()
            else:
                res.append(char)
        return "".join(res)
     
print(clearDigits(s))
