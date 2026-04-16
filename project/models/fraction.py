class Fraction:
    def __init__(self, numerator, denominator):
        self.num = numerator
        self.den = denominator

    def __add__(self, other):
        return Fraction(self.num * other.den + other.num * self.den,
                        self.den * other.den)

    def __sub__(self, other):
        return Fraction(self.num * other.den - other.num * self.den,
                        self.den * other.den)

    def __mul__(self, other):
        return Fraction(self.num * other.num,
                        self.den * other.den)

    def __truediv__(self, other):
        return Fraction(self.num * other.den,
                        self.den * other.num)

    def __str__(self):
        return f"{self.num}/{self.den}"