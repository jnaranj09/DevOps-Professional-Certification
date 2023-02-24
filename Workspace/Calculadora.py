print("Hola")
nombre = input("Favor digite su nombre: ")
print("\nHola " + nombre + "\n")

"""
Este primer "While True" es un loop para ejecutar todo el programa de nuevo si no se cumple el ultimo "break"
"""

while True:

        """
        Este segundo "While True" evalua que la seleccion sea un numero entre 1 y 4. Si es invalido, entonces repite el bucle
        hasta que se digite un numero entre 1 y 4.
        """

        while True:
                menu = int(input("\nIngrese un numero segun el menu de opciones:\n 1) Suma\n 2) Resta\n 3) Multiplicacion\n 4) Division\n\n Opcion: " ))
                if menu < 1 or menu > 4:
                        print("\nOpcion Invalida!!\n")
                else:
                        break

        """
        El siguiente bloque de IFs, ejectua un bloque de codigo dependiendo de la seleccion entre 1 y 4 que hizo el usuario
        """

        if menu == 1:
                print("\nHa seleccionado Suma!\n")
                suma1 = int(input("Favor ingrese el primer numero: "))
                suma2 = int(input("Favor ingrese el segundo numero: "))
                sumaresult = suma1 + suma2
                print( "\n" + str(suma1) + " + " + str(suma2) + " = " + str(sumaresult) + "\n" )
        if menu == 2:
                print("\nHa seleccionado Resta!\n")
                resta1 = int(input("Favor ingrese el primer numero: "))
                resta2 = int(input("Favor ingrese el segundo numero: "))
                restaresult = resta1 - resta2
                print( "\n" + str(resta1) + " - " + str(resta2) + " = " + str(restaresult) + "\n")
        if menu == 3:
                print("\nHa seleccionado Multiplicacion!\n")
                multi1 = int(input("Favor ingrese el primer numero: "))
                multi2 = int(input("Favor ingrese el segundo numero: "))
                multiresult = multi1 * multi2
                print( "\n" + str(multi1) + " * " + str(multi2) + " = " + str(multiresult) + "\n" )
        if menu == 4:
                print("Ha seleccionado Division!\n")
                divi1 = int(input("Favor ingrese el primer numero: "))
                while True:
                        divi2 = int(input("Favor ingrese el segundo numero: "))
                        if divi2 == 0:
                                print("No es posible dividir entre 0, favor digite otro numero")
                        else:
                                break
                diviresult = divi1 / divi2
                print( "\n" + str(divi1) + " / " + str(divi2) + " = " + str(diviresult) + "\n" )

        """
        El siguiente "While True" evalua que la seleccion sea un numero entre 1 y 2. Si en invalido, entonces repite el bucle
        hasta que se digite un numero entre 1 y 2
        """

        while True:
                menuchoice = int(input("Digite:\n 1) Realizar otra operacion\n 2) Salir del programa\n Opcion: "))
                if menuchoice < 1 or menuchoice > 2:
                        print("\nOpcion Invalida!!\n")             
                else:
                        break
        
        """
        Los siguientes IFs, validan si se selecciona "volver al menu", entonces NO se ejecuta el Break,
        y el primer "While true" se vuelve a ejecutar.
        Si se selecciona "Salir del programa", entonces se ejecuta un "break" y el programa se cierra
        """

        if menuchoice == 1:
                print("\n Regresando al Menu.....\n")
        if menuchoice == 2:
                break