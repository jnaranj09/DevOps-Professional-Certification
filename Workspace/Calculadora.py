print("Hola")
nombre = input("Favor digite su nombre: ")
print("Hola " + nombre)
menu = int(input("Ingrese un numero segun el menu de opciones\n 1) Suma\n 2) Resta\n 3) Multiplicacion\n 4) Division\n" ))
while menu < 1 or menu > 4:
    print("Numero invalido!!\n")
    menu = int(input("Ingrese un numero segun el menu de opciones\n 1) Suma\n 2) Resta\n 3) Multiplicacion\n 4) Division\n" ))
else:
    if menu == 1:
        suma1 = int(input("Favor ingrese el primer numero: "))
        suma2 = int(input("Favor ingrese el segundo numero: "))
        sumaresult = suma1 + suma2
        print( str(suma1) + " + " + str(suma2) + " = " + str(sumaresult) )
    if menu == 2:
        print("resta")


    