
num = [1, 2, 3]


class Solution:
    def PlusOne(digits: list) -> list:
        num.append(num[-1] + 1)
        num.remove(num[-2])
        return num
print(Solution.PlusOne(num))

