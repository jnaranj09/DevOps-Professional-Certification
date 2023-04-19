class Cuenta():
    def __init__(self, numcuenta, titular):
        self.numcuenta = numcuenta
        self.titular = titular

class TipoCuenta(Cuenta):
    def __init__(self, numcuenta, titular, edad, tipo=""):
        Cuenta.__init__(self, numcuenta, titular)
        self.edad = edad
        self.tipo = tipo
    def tipocuenta(self):
        if self.edad < 18:
            self.tipo = "Cuenta Joven"
        else:
            self.tipo = "Cuenta Normal"
        return self.tipo
    def __str__(self):
        return "La cuenta: " + self.numcuenta + ", a nombre de: " + self.titular + ", es de tipo: " + TipoCuenta.tipocuenta(self)


numcuenta = input("Introduce el número de cuenta: ")
titular = input("Introduce el nombre del titular: ")
edad = int(input("Introduce la edad del titular: "))

Cuenta1 = TipoCuenta(numcuenta, titular, edad)
print(Cuenta1)