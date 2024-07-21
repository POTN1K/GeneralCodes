"""import math

x = input("Dame el radio ")
x = float(x)

areaE = 4 * (x ** 2) * math.pi

volume = 4 * (x ** 3) * math.pi / 3

print("El area de la esfera es ", areaE, ", y el volumen es ", volume)
print("-------------------------------------------")

sides = []
s = 0

for side in range(0, 3):
    side = input("Dame un lado: ")
    side = float(side)
    sides.append(side)
    s = s + side

s = s / 2
areaT = math.sqrt(s * (s - sides[0]) * (s - sides[1]) * (s - sides[2]))

print("El area es: ", areaT)"""
print("-------------------------------------------")
lados = [0, 0, 0]
for x in range(0, 3):
    while lados[x] <= 0:
        lados[x] = int(input("Dame un lado"))

if (lados[0] + lados[1] > lados[2]) & (lados[1] + lados[2] > lados[0]) & (lados[2] + lados[0] > lados[1]):
    if lados[0] == lados[1] & lados[0] == lados[2]:
        print("Equilatero")
    elif (lados[0] == lados[1]) | (lados[0] == lados[2]) | (lados[1] == lados[2]):
        print("Isósceles")
    else:
        print("Escaleno")
else:
    print("No es un triangulo")
