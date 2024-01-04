from math import sqrt


def myfunc(x):
    return (180 / x) * 60 + (x / 2) * 0.04


def golden(f, a, b,  tolerance=1e-6):
    phi = (sqrt(5) - 1) / 2 # расчет константы золотого сечения
    c = a + (1 - phi) * (b - a)
    d = a + b - c
    while abs(b - a) > tolerance:
        if f(c) <= f(d):
            b = d
            d = c
            c = a + (1 - phi) * (b - a)
        else:
            a = c
            c = d
            d = a + b - c
    return [a, b], (a + b) / 2

a = 700
b = 800
tolerance = 3.5
print(golden(f=myfunc, a=a, b=b, tolerance=tolerance))