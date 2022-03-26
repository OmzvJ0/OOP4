def palindrome(string):
    n = str(string)
    if n == n[::-1]:
        return True
    else:
        return False

x = input("Введите число")
o = palindrome(x)
print(o)

