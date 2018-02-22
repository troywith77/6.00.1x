class fraction(object):
    def __init__(self, numer, denom):
        # numerator - 分子，denominator - 分母
        self.numer = numer
        self.denom = denom
    def __str__(self):
        return str(self.numer) + ' / ' + str(self.denom)
    def getNumer(self):
        return self.numer
    def getDenom(self):
        return self.denom
    def __add__(self, other):
        numerNew = self.getNumer() * other.getDenom() + self.getDenom() * other.getNumer()
        denomNew = self.getDenom() * other.getDenom()
        return fraction(numerNew, denomNew)
    def convert(self):
        return self.getNumer() / self.getDenom()

onHalf = fraction(1, 2)
twoThirds = fraction(2, 3)
print(onHalf + twoThirds)
print(onHalf.convert())