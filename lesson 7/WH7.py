def palindrome(string):
    n = str(string)
    if n == n[::-1].startswith(n):
        return True
    else:
        return False


o = palindrome(123)
print(o)

