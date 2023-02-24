import time  #1. Este modulo le permite al programa ejecutar el comando "time.sleep() el cual duerme o pausa el programa por el tiempo especificado en segundos"
try:                            #2. Este try > While True loop intenta ejecutar todo el programa excepto si se detecta un CTRL+C (Keyboard interrupt al final del codigo)
        while True:             #   si se detecta la interrupcion, el programa termina.
                print("-----------------------------------")
                print("Bienvenido a tu calcu de confianza")
                print("-----------------------------------")
                print("\nNota: Presiona CTRL+C para salir del programa en cualquier momento\n")
                print("-----------------------------------")
                time.sleep(2)

                #3. Este primer "While True" es un loop para ejecutar todo el programa de nuevo si no se cumple el ultimo "quit(). Basicamente es volver al menu"

                while True:

                        """
                        4. 
                        Este segundo "While True" evalua que la seleccion sea un numero entre 1 y 4. Si es invalido, entonces repite el bucle
                        hasta que se digite un numero entre 1 y 4.

                        Este While contiene una validacion de tipo de dato (while > try > except). Si se genera un error de valor (ejem: se ingresa texto cuando el programa solicita un numero entero)
                        entonces el programa imprime que el tipo de dato es invalido, y reinicia el bucle While.
                        """

                        while True:
                                try:
                                        menu = int(input("\nIngrese un numero segun el menu de opciones:\n\n 1) Suma\n 2) Resta\n 3) Multiplicacion\n 4) Division\n\n Opcion: " ))
                                        if menu < 1 or menu > 4:
                                                print("\n-----------------------------------")
                                                print("Opcion Invalida!!")
                                                print("-----------------------------------")
                                        else:
                                                break
                                except ValueError:
                                        print("\n-----------------------------------")
                                        print("El tipo de dato ingresado es invalido, debe ser un numero entero entre 1 y 4.")
                                        print("-----------------------------------")
                        """
                        #5. 
                        El siguiente bloque de IFs, ejectua codigo dependiendo de la seleccion entre 1 y 4 que hizo el usuario
                        Tambien contienen la misma validacion de tipo de dato (while > try > except).
                        """
                        if menu == 1:
                                while True:
                                        try:
                                                print("\nHa seleccionado Suma!\n")
                                                suma1 = int(input("Favor ingrese el primer numero: "))
                                                suma2 = int(input("Favor ingrese el segundo numero: "))
                                                sumaresult = suma1 + suma2
                                                print( "\n" + str(suma1) + " + " + str(suma2) + " = " + str(sumaresult) + "\n" )
                                                break
                                        except ValueError:
                                                print("\n-----------------------------------")
                                                print("El tipo de dato ingresado es invalido, debe ser un numero entero")
                                                print("-----------------------------------")
                        if menu == 2:
                                while True:
                                        try:
                                                print("\nHa seleccionado Resta!\n")
                                                resta1 = int(input("Favor ingrese el primer numero: "))
                                                resta2 = int(input("Favor ingrese el segundo numero: "))
                                                restaresult = resta1 - resta2
                                                print( "\n" + str(resta1) + " - " + str(resta2) + " = " + str(restaresult) + "\n")
                                                break
                                        except ValueError:
                                                print("\n-----------------------------------")
                                                print("El tipo de dato ingresado es invalido, debe ser un numero entero")
                                                print("-----------------------------------")
                        if menu == 3:
                                while True:
                                        try:
                                                print("\nHa seleccionado Multiplicacion!\n")
                                                multi1 = int(input("Favor ingrese el primer numero: "))
                                                multi2 = int(input("Favor ingrese el segundo numero: "))
                                                multiresult = multi1 * multi2
                                                print( "\n" + str(multi1) + " * " + str(multi2) + " = " + str(multiresult) + "\n" )
                                                break
                                        except ValueError:
                                                print("\n-----------------------------------")
                                                print("El tipo de dato ingresado es invalido, debe ser un numero entero")
                                                print("-----------------------------------")
                        if menu == 4:
                                while True:
                                        try:
                                                print("\nHa seleccionado Division!\n")
                                                divi1 = int(input("Favor ingrese el primer numero: "))
                                                
                                                """
                                                #6.
                                                El siguiente While loop valida que mientras divi2 sea igual a 0, volvera a solicitar el dato
                                                ya que ningun numero es divisible entre 0
                                                """
                                                
                                                while True:
                                                        divi2 = int(input("Favor ingrese el segundo numero: "))
                                                        if divi2 == 0:
                                                                print("\n-----------------------------------")
                                                                print("No es posible dividir entre 0, favor digite otro numero")
                                                                print("-----------------------------------\n")
                                                        else:
                                                                break
                                                diviresult = divi1 / divi2
                                                print( "\n" + str(divi1) + " / " + str(divi2) + " = " + str(diviresult) + "\n" )
                                                break
                                        except ValueError:
                                                print("\n-----------------------------------")
                                                print("El tipo de dato ingresado es invalido, debe ser un numero entero")
                                                print("-----------------------------------")


                        """
                        #7. 
                        El siguiente "While True" evalua que la seleccion sea un numero entre 1 y 2. Si es invalido, entonces repite el bucle
                        hasta que se digite un numero entre 1 y 2
                        """

                        while True:
                                try:
                                        menuchoice = int(input("Ingrese un numero segun el menu de opciones:\n\n 1) Realizar otra operacion\n 2) Salir del programa\n\n Opcion: "))
                                        if menuchoice < 1 or menuchoice > 2:
                                                print("\nOpcion Invalida!!\n")             
                                        else:
                                                break
                                except ValueError:
                                        print("\n-----------------------------------")
                                        print("\nEl tipo de dato ingresado es invalido, debe ser un numero entero entre 1 y 2.\n")
                                        print("-----------------------------------")
                        
                        """
                        #8. 
                        Los siguientes IFs, validan si se selecciona "volver al menu", entonces NO se ejecuta el quit(),
                        y el primer "While true" (El menu) se vuelve a ejecutar.
                        Si se selecciona "Salir del programa", entonces se ejecuta un "quit()" y el programa se cierra
                        """

                        if menuchoice == 1:
                                print("\n-----------------------------------")
                                print("Regresando al Menu.....")
                                print("-----------------------------------")
                        if menuchoice == 2:
                                print("Nos vemos luego..............")
                                time.sleep(0.7)
                                print("...............")
                                time.sleep(0.5)
                                print(".......")
                                time.sleep(0.2)
                                print("..")
                                quit()


except KeyboardInterrupt:       #2.1 Este try > While True loop intenta ejecutar todo el programa excepto si se detecta un CTRL+C (Keyboard interrupt al final del codigo)
                                #    si se detecta la interrupcion, el programa termina.
        print("\n-----------------------------------")
        print("El programa fue interrumpido por el usuario")
        time.sleep(1)
        print("Nos vemos luego..............")
        time.sleep(0.7)
        print("...............")
        time.sleep(0.5)
        print(".......")
        time.sleep(0.2)
        print("..")