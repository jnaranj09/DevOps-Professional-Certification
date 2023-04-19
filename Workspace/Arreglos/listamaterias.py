materias=[]
while True:
    materias.append(input("Ingrese una materia o escriba 'SALIR' para terminar: ").upper())
    if materias[-1] == "SALIR":
        break
materias.pop(-1)
print("")
index = 1
print ("Materias a llevar:")
for i in (materias):
    print(str(index)+".",i)
    index += 1