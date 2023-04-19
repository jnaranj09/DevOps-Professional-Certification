from openpyxl import Workbook, load_workbook
filesheet = "Workspace\banco\DB.xlsx"
wb = load_workbook(filesheet)
ws = wb.active

while True:
    print("Eliga una opcion: ")
    print("1. Realizar un deposito")
    print("2. Retirar dinero")
    print("3. Consultar saldo")
    print("4. Salir")
    print("")
    try:
        menuchoice=int(input())
        if menuchoice == 1:
            
            deposito = int(input("Digite la cantidad que desea depositar: "))
 

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