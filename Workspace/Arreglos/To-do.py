todo=[]
hora=1
while True:
    todo.append(input("Ingrese una tarea a realizar para la hora " + str(hora) + " o escriba 'SALIR' para terminar: ").upper())
    hora +=1
    if todo[-1] == "SALIR":
        todo.pop(-1)
        break
    if len(todo) == 8:
        break
print("")
index = 1
print ("Tareas a realizar:")
for i in (todo):
    print("Hora " + str(index) + ":" , i)
    index += 1
#Confirma si desea cambiar algo
while True:
    confirma=input("Desea cambiar alguna tarea? (si/no): ").upper()
    if confirma == "SI":
        tarea_c=int(input("Digite el numero de la tarea que desea cambiar: "))
        cambio=input("Digite la nueva tarea: ").upper()
        tarea_c-=1
        todo[tarea_c]=cambio
        index = 1
        print ("Tareas a realizar:")
        for i in (todo):
            print("Hora " + str(index) + ":" , i)
            index += 1
    if confirma == "NO":
        quit()
        
