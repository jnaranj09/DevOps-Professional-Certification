array = [4,3,2,1,63,4,2,8]
n = len(array)
print(f"tamaño del array es: {n}")
for i in range(n-1):
     for j in range (n-i-1):
         if array[j] > array[j+1]:
             array[j], array[j+1] = array[j+1], array[j]
print(array)


#Nota: cuando se coloca solo un numero dentro del parentesis en range, el for va a iterar desde 0 por default, hasta el numero dado
#Basicamente no es necesario hacer (0,4) con poner solo el 4, ya basta.

# como funciona
# array = 8 , 4 , 3 , 1 
# 	     {0} {1} {2} {3}

# n = len(array)  (longitud del array es 4)

# ---------------
# for i in range(n-1) (de 0 hasta 3) (osea 0,1,2)

# vuelta i(0)
# ---------------

# for j in range de 0 hasta (n(4)-i(0)-1) = 3 (osea 0,1,2)
# vuelta j 0
# si
# index0 > index1
# intercambio los datos

#  4 , 8 , 3 , 1 
# {0} {1} {2} {3}

# vuelta j 1
# si
# index1 > index2
# intercambio los datos

#  4 , 3 , 8 , 1 
# {0} {1} {2} {3}

# vuelta j 2
# si 
# index2 > index3
# intercambio los datos

#  4 , 3 , 1 , 8 
# {0} {1} {2} {3}

# -----------------

# for i 
# vuelta i(1)
# -----------------

# for j in range de 0 hasta (n(4)-i(1)-1)=2 (osea 0,1)
# vuelta j 0
# si
# index0 > index1
# intercambio los datos

#  3 , 4 , 1 , 8 
# {0} {1} {2} {3}

# vuelta j 1
# si
# index1 > index2
# intercambio los datos

#  3 , 1 , 4 , 8 
# {0} {1} {2} {3}


# Aqui solo hago dos vueltas, porque no deberia tener que cambiar 4 por el 8

# -----------------

# for i 
# vuelta i(2)

# -----------------

# for j in range de 0 hasta (n(4)-i(2)-1)=1 (osea 0) (solo una vuelta)
# vuelta j 0
# si
# index0 > index1
# intercambio los datos


#  1 , 3 , 4 , 8 
# {0} {1} {2} {3}

# ------------------