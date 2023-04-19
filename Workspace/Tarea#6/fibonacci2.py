secuencia=[]
max=int(input("Favor digite el numero maximo de la secuencia fib: "))
for i in range(max+1):
    if i == 0:
        secuencia.append(0)
    elif i == 1:
        secuencia.append(1)
    else:
        secuencia.append(secuencia[i-2]+secuencia[i-1])
for j in range(max+1):
    print(f"El fibonacci de {j} es {secuencia[j]}")


##aqui es necesario el elif para que no evalue nada mas si se cumple el primer o segundo if