import math
import numpy as np


def math_function(x):
    y = (2 * math.pow(x, 2)) + 3
    return y


def range2(inf, sup):
    num = (sup - inf) * 100
    interval = np.linspace(inf, sup, num)
    return interval


value = 0
print("Solo acepta valores enteros xd")
lim_inf = input("Limite inferior: ")
lim_sup = input("Limite superior: ")
lim_inf = int(lim_inf)
lim_sup = int(lim_sup)

intervalo = range2(lim_inf, lim_sup)
for n in range(intervalo.size - 1):
    i = intervalo[n]
    j = intervalo[n + 1]
    alt_i = math_function(i)
    alt_j = math_function(j)
    alt_prom = (alt_i + alt_j) / 2
    area = (j - i) * alt_prom

    value = value + area

print("La integral es: ", value)
