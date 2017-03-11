# Euclid's algorithm to get greatest common divisor, or GCD
# GCD of m and n is n if n divides m evenly. If not, then it is the GCD of n and
# the remainder of m divided by n. Iterative!!!
def gcd(m, n):
    while m%n != 0:
        oldm = m
        oldn = n
        m = oldn
        n = oldm%oldn
    return n

class Fraction:

# The first method is the constructor __init__
# Two arguments top, which is the numerator (num) and bottom, which is the denominator (den)
# num and den are two internal data object
    def __init__(self, top, bottom):
        self.num = top
        self.den = bottom

# Method 'show' to allow 'Fraction' object to print itself as a string
    def show(self):
        print(str(self.num) + '/' + str(self.den))

# __str__ is called anytime a Fraction object is asked to convert itself to a string
    def __str__(self):
        return str(self.num) + '/' + str(self.den)

# add function
    def __add__(self, other):
        newnum = self.num * other.den + self.den * other.num
        newden = self.den * other.den
        common = gcd(newnum, newden)
        return Fraction(newnum // common, newden // common)

# minus function
    def __sub__(self, other):
        newnum = self.num * other.den - self.den * other.num
        newden = self.den * other.den
        common = gcd(newnum, newden)
        return Fraction(newnum // common, newden // common)

# mulitply function
    def __mul__(self, other):
        newnum = self.num * other.num
        newden = self.den * other.den
        common = gcd(newnum, newden)
        return Fraction(newnum // common, newden // common)

# divison function
    def __div__(self, other):
        newnum = self.num * other.den
        newden = self.den * other.num
        common = gcd(newnum, newden)
        return Fraction(newnum // common, newden // common)

# equality function, deep equality
    def __eq__(self, other):
        firstnumber = self.num * other.den
        secondnumber = other.num * self.den
        return firstnumber == secondnumber

# < function, deep equality
    def __lt__(self, other):
        firstnumber = self.num * other.den
        secondnumber = other.num * self.den
        return firstnumber < secondnumber

# > function, deep equality
    def __gt__(self, other):
        firstnumber = self.num * other.den
        secondnumber = other.num * self.den
        return firstnumber > secondnumber
# Create an instance of the Fraction class
myfraction = Fraction(3, 5)
# If no __str__, Output: <__main__.Fraction instance at 0x10bb66bd8>, can't convert itself to a string
# Three different ways to print Fraction object, all involke __str__
print(myfraction)
print(str(myfraction))
print(myfraction.__str__())
myfraction.show()
f1 = Fraction(1, 4)
f2 = Fraction(1, 2)
f3 = f1 + f2
print(f3)
x = Fraction(1,2)
y = Fraction(2,3)
print(x+y)
print(x-y)
print(x*y)
print(x.__div__(y)) # x/y, x//y do not work
print(x == y)
print(x < y)
print(x > y)
