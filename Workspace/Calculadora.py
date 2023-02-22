print("Hola")
nombre = input("Favor digite su nombre: ")
print("\nHola " + nombre + "\n")
while True:
    menu = int(input("Ingrese un numero segun el menu de opciones:\n 1) Suma\n 2) Resta\n 3) Multiplicacion\n 4) Division\n\n Opcion: " ))
    if menu < 1 or menu > 4:
        print("\nOpcion Invalida!!\n")
    else:
        break
if menu == 1:
        print("Ha seleccionado Suma!\n")
        suma1 = int(input("Favor ingrese el primer numero: "))
        suma2 = int(input("Favor ingrese el segundo numero: "))
        sumaresult = suma1 + suma2
        print( str(suma1) + " + " + str(suma2) + " = " + str(sumaresult) )
if menu == 2:
        print("Ha seleccionado Resta!\n")
        resta1 = int(input("Favor ingrese el primer numero: "))
        resta2 = int(input("Favor ingrese el segundo numero: "))
        restaresult = resta1 - resta2
        print( str(resta1) + " - " + str(resta2) + " = " + str(restaresult) )
if menu == 3:
        print("Ha seleccionado Multiplicacion!\n")
        multi1 = int(input("Favor ingrese el primer numero: "))
        multi2 = int(input("Favor ingrese el segundo numero: "))
        multiresult = multi1 * multi2
        print( str(multi1) + " * " + str(multi2) + " = " + str(multiresult) )
if menu == 4:
        print("Ha seleccionado Division!\n")
        divi1 = int(input("Favor ingrese el primer numero: "))
        divi2 = int(input("Favor ingrese el segundo numero: "))
        diviresult = divi1 / divi2
        print( str(divi1) + " / " + str(divi2) + " = " + str(diviresult) )


    