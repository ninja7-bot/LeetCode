s = "A man, a plan, a canal: Panama"
def isPalindrome(s):
    txt = re.sub(r'[^a-zA-Z0-9]', '', s).lower()
    return txt == txt[::-1]
isPalindrome(s)
