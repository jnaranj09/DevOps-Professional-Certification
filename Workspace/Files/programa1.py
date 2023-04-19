#Hacer un programa que con un menu solicite al usuario que se desea hacer:
#1. Leer un archivo
#2. Escribir un archivo
#3. Salir
#Si la opcion es 1, solicita el nombre del archivo y lo manda a imprimir
#Si la opcion es 2 solicita el nombre del archivo y el texto que se desea ingresar
#Si es 3, sale del programa.


while True:
    print("Eliga una opcion: ")
    print("1. Leer un archivo")
    print("2. Crear/Sobrescribir un archivo")
    print("3. Agregar informacion a un archivo")
    print("4. Salir")
    print("")
    try:
        menuchoice=int(input())
        if menuchoice == 1:
            try:
                    file = input("Favor digite el nombre del archivo que desea leer: ")
                    f = open (file, "r")
                    content = f.read()
                    print("--------------------------------")
                    print("El contenido del archivo es: ")
                    print("--------------------------------")
                    print("")
                    print(content)
                    print("\n--------------------------------")
                    f.close()
                    print("\nse cerro el archivo \n")
            except FileNotFoundError:
                    print("\nEl archivo no existe!\n")

        elif menuchoice == 2:

            file = input("\nFavor digite el nombre del archivo que desea Crear/Sobre escribir: ")
            f = open (file, "w")
            mod = input("\nFavor digite los datos que desea ingresar al archivo: \n")
            f.write(mod)
            print(f"\nSe escribio en el archivo lo siguiente: '{mod}'\n")
            f.close()
            print("\nse cerro el archivo \n")

        elif menuchoice == 3:
             
            file = input("\nFavor digite el nombre del archivo al que desea agregarle informacion : ")
            f = open (file, "a")
            mod = input("\nFavor digite los datos que desea ingresar al archivo: \n")
            f.write(f"\n{mod}")
            print(f"\nSe agrego en el archivo lo siguiente: '{mod}'\n")
            f.close()
            print("\nse cerro el archivo \n")
        
        elif menuchoice == 4:
             
             break

        else:

            print("\nopcion invalida!!\n")

    except ValueError:
        print("\nEl dato ingresado es invalido!!\n")