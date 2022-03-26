def palindrome(string):
    n = str(string)
    if n == n[::-1]:
        return True
    else:
        return False


o = palindrome(121)
print(o)

