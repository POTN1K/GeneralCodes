import math


def math_function(x):
    y = (2 * math.pow(x, 3))+5
    return y


def pendiente(x_menor, x_mayor):
    y1 = math_function(x_menor)
    y2 = math_function(x_mayor)
    y_fin = y2-y1
    x_fin = x_mayor-x_menor
    m = y_fin/x_fin
    return m


x1 = input("En que punto quieres saber la pendiente? ")
x1 = float(x1)
x2 = x1 + 0.00000000001
res = pendiente(x1, x2)
res = int(res)
print("La pendiente en ", x1, " es ", res)


