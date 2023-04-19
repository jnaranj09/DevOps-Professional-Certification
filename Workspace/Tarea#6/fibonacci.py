max=int(input("Favor ingrese el numero maximo de la secuencia fibonacci: "))
def fib(i):
    if i == 1:
        return 1
    elif i == 0:
        return 0
    else:
        return (fib(i-1))+(fib(i-2))
for i in range (max+1): 
    print(f"El fibonacci de {i} es {fib(i)}")
