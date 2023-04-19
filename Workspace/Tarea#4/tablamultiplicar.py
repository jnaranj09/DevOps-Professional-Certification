numero = int(input("Ingrese un número para ver su tabla de multiplicar: "))

for i in range(1, 11):
    result = numero * i
    print(numero, "x", i, "=", result)