from math import gcd, pow

class Rational:
    def __init__(self, numer, denom):
        if denom == 0:
            raise ValueError("Denominator cannot be zero")
        common = gcd(numer, denom)
        self.numer = numer // common
        self.denom = denom // common
        if self.denom < 0:
            self.numer = -self.numer
            self.denom = -self.denom

    def __eq__(self, other):
        return self.numer == other.numer and self.denom == other.denom

    def __repr__(self):
        return f'{self.numer}/{self.denom}'

    def __add__(self, other):
        new_numer = self.numer * other.denom + other.numer * self.denom
        new_denom = self.denom * other.denom
        return Rational(new_numer, new_denom)

    def __sub__(self, other):
        new_numer = self.numer * other.denom - other.numer * self.denom
        new_denom = self.denom * other.denom
        return Rational(new_numer, new_denom)

    def __mul__(self, other):
        new_numer = self.numer * other.numer
        new_denom = self.denom * other.denom
        return Rational(new_numer, new_denom)

    def __truediv__(self, other):
        if other.numer == 0:
            raise ValueError("Cannot divide by zero")
        new_numer = self.numer * other.denom
        new_denom = self.denom * other.numer
        return Rational(new_numer, new_denom)

    def __abs__(self):
        return Rational(abs(self.numer), abs(self.denom))

    def __pow__(self, power):
        if isinstance(power, int):
            if power >= 0:
                new_numer = self.numer ** power
                new_denom = self.denom ** power
            else:
                new_numer = self.denom ** abs(power)
                new_denom = self.numer ** abs(power)
            return Rational(new_numer, new_denom)
        elif isinstance(power, float):
            return pow(self.numer, power) / pow(self.denom, power)
        else:
            raise TypeError("Power must be an integer or float")

    def __rpow__(self, base):
        return pow(pow(base, self.numer), 1/self.denom)
