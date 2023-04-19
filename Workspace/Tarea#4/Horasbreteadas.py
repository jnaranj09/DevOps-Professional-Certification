h_t = int(input("Favor ingrese las horas trabajadas este mes: "))
s_b = int(input("Favor ingrese su salario base mensual: "))
s_h = s_b / 160
if h_t > 160 and h_t <=180:
    dif_h = h_t - 160
    salario = (h_t * s_h) + (dif_h * s_h)
    print("Su salario es de: " + str(salario))
elif h_t > 180:
    dif_h1 = h_t - 160
    dif_h2 = h_t - 180
    salario = (h_t * s_h) + (h_t * dif_h1) + (h_t * dif_h2)
    print("Su salario es de: " + str(salario))
else:
    salario = s_h * h_t
    print("Su salario es de: " + str(salario))