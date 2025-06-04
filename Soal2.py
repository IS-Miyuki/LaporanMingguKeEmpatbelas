def palindrome(n:str):
    n = n.lower()
    if len(n) == 0:
        return True
    elif n[0] == n[-1]:
        return palindrome(n[1:-1])
    else:
        return False

print(palindrome("radar"))