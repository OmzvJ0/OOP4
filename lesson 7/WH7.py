def palindrome(string):
    n = str(string)
    if n == n[::-1]:
        return True
    else:
        return False
while 1:
    x = input("Введите число ")
    print(palindrome(x))

