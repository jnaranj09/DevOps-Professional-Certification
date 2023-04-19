inicial = int(input("Introduce el número inicial: "))
final = int(input("Introduce el número final: "))

def recur(n):
    if n == final:
        print(n)
    else:
        print(n)
        recur(n-1)

recur(inicial)