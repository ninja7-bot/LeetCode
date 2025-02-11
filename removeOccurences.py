s = "daabcbaabcbc"
part = "abc"


def removeOccurrences(s, part):
    flag = True
    l = len(part)
    while flag:
        if part not in s:
            return s
            flag = False
        i = s.find(part)
        j = i + l
        s = s[:i] + s[j:]
        flag = True

        
removeOccurrences(s, part)
