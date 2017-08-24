class Polynomial:
    def __init__(self, *coeffs):
        self.coeffs = coeffs

    def __str__(self):
        return "{} x^2+{} x+ {} =0".format(*self.coeffs)

    def __add__(self, other):
        return Polynomial(*[x + y for x in self.coeffs for y in other.coeffs])


# , self.coeffs[1], self.coeffs[2]
p1 = Polynomial(1, 2, 3)
print(p1)
p2 = Polynomial(3, 4, 5)
# p1.coeffs = 1, 2, 3  # x^2+2x+3=0
# p2.coeffs = 3, 4, 3  # 3x^2+4x+3=0
print(p1)
print(*[1, 2, 3])
p3 = p1 + p2
print(p3)
