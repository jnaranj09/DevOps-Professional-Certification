while True:
    print("Menú:")
    print("1. Opción 1")
    print("2. Opción 2")
    print("3. Opción 3")
    print("Escriba SALIR para salir del programa")

    opcion = input("Elija una opción: ")

    if opcion.upper() == "SALIR":
        print("Saliendo del programa...")
        break

    if opcion == "1":
        print("Ha elegido la opción 1")
    elif opcion == "2":
        print("Ha elegido la opción 2")
    elif opcion == "3":
        print("Ha elegido la opción 3")
    else:
        print("Opción inválida, por favor elija una opción válida")