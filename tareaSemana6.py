class CuentaBancaria:
    def __init__(self, saldo_inicial):
        self.__saldo = saldo_inicial  # Atributo privado

    def depositar(self, cantidad):
        if cantidad > 0:
            self.__saldo += cantidad
            print(f"Depositado: {cantidad}. Nuevo saldo: {self.__saldo}")
        else:
            print("Cantidad a depositar debe ser positiva.")

    def retirar(self, cantidad):
        if cantidad <= self.__saldo:
            self.__saldo -= cantidad
            print(f"Retirado: {cantidad}. Nuevo saldo: {self.__saldo}")
        else:
            print("Fondos insuficientes para el retiro.")

    def obtener_saldo(self):  # Método 'getter' para el saldo
        return self.__saldo

# Creando un objeto de la clase CuentaBancaria
mi_cuenta = CuentaBancaria(30000)

# Utilizando los métodos de la clase
print(f"Saldo inicial: {mi_cuenta.obtener_saldo()}")
mi_cuenta.depositar(15000)
mi_cuenta.retirar(15000)
print(f"Saldo final: {mi_cuenta.obtener_saldo()}")