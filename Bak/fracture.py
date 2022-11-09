import math


class fracture:
    def __init__(self, numerator, denominator):
        self.numerator = numerator
        self.denominator = denominator

    def extend(self, k):
        extendnum = self.numerator * k
        extendden = self.denominator * k
        print(extendnum)
        print(extendden)

    def shorten(self, k):
        shortennum = self.numerator // k
        shortenden = self.denominator // k
        print(shortennum)
        print(shortenden)

    def low(self):
        lowdcomden = math.gcd(self.numerator, self.denominator)  # greatest common divisor
        lownum = self.numerator // lowdcomden
        lowden = self.denominator // lowdcomden
        print(lownum)
        print(lowden)

    def info(self):
        print(self.numerator)
        print(self.denominator)


fracture1 = fracture(4, 6)

fracture1.extend(3)
fracture1.shorten(2)
fracture1.low()
