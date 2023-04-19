# Matriz = [
#         ["4312","Cris",90],
#         ["5432","Ale",96],
#         ["4542","Esteban"]
#         ]

#Add a value at the end of the Matrix
# for i in range(len(Matriz)):
#      if i == len(Matriz)-1:
#          Matriz[i].append(80)
# print(Matriz)

#How to travel every value in the matrix
# for each_list in range(len(Matriz)):
#     for each_value in range(len(Matriz[each_list])):
#         print(f"Position {each_list},{each_value}: {Matriz[each_list][each_value]}")

#Fix a student name
# print(Matriz)
# for each_list in range(len(Matriz)):
#      if Matriz[each_list][1].upper() == "ALE":
#           Matriz[each_list][1]="Fernanfloo"
# print(Matriz)

#Remove a complete list referring to a stundent
# print(Matriz)
# for each_list in range(len(Matriz)):
#       if Matriz[each_list][1].upper() == "ALE":
#            Matriz.remove(Matriz[each_list])
#            break
# print(Matriz)








##############################################

Matriz = [
         [2,5,90],
         [6,62,96],
         [45,52,23]
         ]


#1. Sumar todos los elementos de una matriz completa

# Total = 0
# for each_list in range(len(Matriz)):
#      for each_value in range(len(Matriz[each_list])):
#           Total = Total + Matriz[each_list][each_value]
# print(Total)

#2. Sumar todos los elementos de una Columna especifica

Total=0
item=0
for each_value in range(len(Matriz[0])):
    for each_list in range(len(Matriz)):
        Total= Total+Matriz[each_list][each_value]
    print(f"Total de la columna {each_value} es: {Total}")
    Total=0


#3. Sumar todos los elementos de una fila especifica

# for each_list in range(len(Matriz)):
#      Total = 0
#      for each_value in range(len(Matriz[each_list])):
#          Total = Total + Matriz[each_list][each_value]
#      print(f"La lista {each_list} suma: {Total}")


