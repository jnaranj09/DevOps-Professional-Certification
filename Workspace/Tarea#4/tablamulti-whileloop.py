while True:
    num = int(input("Ingrese un número para calcular su tabla de multiplicar (o ingrese 0 para salir): "))
    if num == 0:
        break
    for i in range(1, 11):
        print(num, "x", i, "=", num*i)