peso = float(input("Favor ingrese su peso en kilogramos: "))
altura = float(input("Favor ingrese su altura en metros: "))
imc = (peso/(altura**2))
if imc < 18.5:
    print("peso insuficiente")
    print("imc: " + str(imc))
elif imc < 24.9:
    print("peso normal")
    print("imc: " + str(imc))
elif imc < 29.9:
    print("sobrepeso")
    print("imc: " + str(imc))
elif imc <34.9:
    print("obesidad")
    print("imc: " + str(imc))
else:
    print("dato invalido")