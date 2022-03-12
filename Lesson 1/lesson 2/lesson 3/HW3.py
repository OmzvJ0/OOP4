def scf(a, b):
    if a == 0:
        return b
    else:
        return scf(b % a, a)

class Fraction:

    def __init__(self, num, denum):
        skf1 = scf(num, denum)
        self.num = num // skf1
        self.denum = denum // skf1

    def __str__(self):
        if self.denum == 1:
            return str(self.num)

        elif self.num > self.denum:
            return str(self.num // self.denum) + " " +\
                   str(Fraction(self.num % self.denum, self.denum))
        else:
            return str(self.num) + "/" + str(self.denum)

    def __add__(self, other):
        new_num = self.num * other.denum + other.num * self.denum
        new_denum = self.denum * other.denum
        return Fraction(new_num, new_denum)

    def __sub__(self, other):
        new_num = self.num * other.denum - other.num * self.denum
        new_denum = self.denum * other.denum
        return Fraction(new_num, new_denum)

    def __mul__(self, other):
        new_num = self.num * other.num
        new_denum = self.denum * other.denum
        return Fraction(new_num, new_denum)

    def __floordiv__(self, other):
        new_num = self.num // other.num
        new_denum = self.denum // other.denum
        return Fraction(new_num, new_denum)

a = Fraction(5, 9)
b = Fraction(2, 4)

print(a + b)
print(a - b)
print(a * b)
print(a // b)