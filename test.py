import math


class Figures:

    def __init__(self, **params):
        self.params = params


class Triangle(Figures):
    name = 'triangle'

    def __init__(self, a, b, c,):

        self.a = a
        self.b = b
        self.c = c

    def S_tr(self):
        if self.a + self.b > self.c and self.b + self.c > self.a and self.a + self.c > self.b:
            p = (self.a + self.b + self.c) / 2
            return (p * (p - self.a) * (p - self.b) * (p - self.c)) ** 0.5
        else:
            print("не треугольник")


class Rectangle(Figures):
    def __init__(self, A, B):
        self.A = A
        self.B = B

    def get_name(self):
        return 'rectangle'

    def S_rec(self):
        return self.A * self.B


class Circle(Figures):
    def __init__(self, R):
        self.R = R

    def S_cir(self):
        return math.pi * self.R ** 2