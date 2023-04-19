import math
radio=int(input("Favor ingrese el radio: "))
altura=int(input("Favor ingrese la altura: "))
volumen = math.pi * radio ** 2 * altura
area = (2 * math.pi * radio * altura) + (2 * math.pi * radio ** 2)
print("Volumen: " + str(volumen) + " area: " + str(area))
