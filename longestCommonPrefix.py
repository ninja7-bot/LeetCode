strs = ["flower","flow","flight"]
def longestCommonPrefix(strs):
    string = ""
    for i in range(0, len(strs)-1):
        string = ''.join(sorted(set(string) &
         set(strs[i]), key = strs[i+1].index))
    return string
print(longestCommonPrefix(strs))
