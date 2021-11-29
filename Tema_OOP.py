import math

class Fraction:

    def __init__(self, numarator, numitor):
        self.numarator = numarator
        if numitor != 0:
            self.numitor = numitor
        else:
            print("Error calculation!")

    def __str__(self):
        return f"Fraction: {self.numarator} / {self.numitor}"

    def __add__(self, other):
        numarator = self.numarator * other.numitor + self.numitor * other.numarator
        numitor   = self.numitor * other.numitor
        cmmdc = math.gcd(numarator, numitor)
        print(f"Cmmdc gathering fraction: {cmmdc}")
        if cmmdc > 1:
            numarator = numarator // cmmdc
            numitor = numitor // cmmdc

        return f"Gathering {Fraction(numarator, numitor)}"
    def __sub__(self, other):
        numarator = self.numarator * other.numitor - self.numitor * other.numarator
        numitor   = self.numitor * other.numitor
        cmmdc = math.gcd(numarator, numitor)
        print(f"Cmmdc decrease fraction: {cmmdc}")
        if cmmdc > 1:
            numarator = numarator // cmmdc
            numitor = numitor // cmmdc

        return f"Decrease {Fraction(numarator, numitor)}"

    def inverse(self):
        if self.numitor and self.numarator != 0:
            (self.numitor, self.numarator) = (self.numarator, self.numitor)
        return f"Inverse Fraction: {self.numarator} / {self.numitor}"

my_fraction = Fraction(8,4)
print(my_fraction.__str__())
print(my_fraction.__add__(other = Fraction(2,4)))
print(my_fraction.__sub__(other = Fraction(5,3)))
print(my_fraction.inverse())