print ("Escriba que desea hacer")
print ("Escribar leer un archivo -> r ")
print ("Escribar escribir un archivo -> w ")
print ("Salir -> S ")

opcion = input().lower()

if opcion == 'r':
    f = open ('archivo1.txt','r')
    print("Se abre el archivo en MODO LECTURA")
    contenido = f.read()
    print("Se lee el archivo")
    print(contenido)
    f.close()

elif opcion == 'w':
    f = open ('archivo1.txt','w')
    print("Se abre el archivo en MODO ESCRITURA")
    f.write('Este es un archivo de prueba creado a las 19:22')
    print("Se escribe el archivo")
    f.close()
    print("Se cierra el archivo")

elif opcion == 's':
    print("Saliendo del programa...")

else:
    print("Opción inválida")