# Вывести квадраты чисел от 30 до 40 включительно
import math


a = 3
b = 4
c = 5


def solve_qad_qe(a, b, c):
    D = b**2 - 4*a*c
    if D < 0:
        return None, None
    elif D == 0:
        print("Только один корень")
        x = (-b) / 2 * a
        return x, None
    else:
        print("Два корня")
        x1 = ((-b) + math.sqrt(D)) / (2*a)
        x2 = ((-b) - math.sqrt(D)) / (2*a)
        return x1, x2


x1, x2 = solve_qad_qe(a, b, c)


print(x1, x2)


def f(x):
    if x >= -2 and x < 2:
        return x**2
    elif x >= 2:
        return x**2 + 4*x + 5
    #


def func(x):
    return True / False
