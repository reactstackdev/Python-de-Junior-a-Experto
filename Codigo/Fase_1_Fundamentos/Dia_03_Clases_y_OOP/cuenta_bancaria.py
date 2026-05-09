# =============================================================================
# ENUNCIADO
# Define una clase CuentaBancaria con un saldo inicial que se pasa al crearla.
# Implementa tres métodos:
#   - depositar(cantidad): suma al saldo y devuelve el nuevo saldo.
#   - retirar(cantidad): resta del saldo si hay fondos suficientes y devuelve
#     True. Si no hay saldo, devuelve False sin modificar nada.
#   - obtener_saldo(): devuelve el saldo actual.
# Prueba los tres métodos con distintos casos, incluyendo un intento de
# retirada fallida.
# =============================================================================

class CuentaBancaria:
    def __init__(self, saldo):
        self.saldo = saldo

    def depositar(self, cantidad):
        self.saldo = self.saldo + cantidad
        return self.saldo

    def retirar(self, cantidad):
        if self.saldo >= cantidad:
            self.saldo = self.saldo - cantidad
            return True
        else:
            return False

    def obtener_saldo(self):
        return self.saldo

dinero = CuentaBancaria(saldo=200)
print(f"El saldo es: {dinero.obtener_saldo()}")
dinero.retirar(100)
print(f"El saldo es: {dinero.obtener_saldo()}")
dinero.retirar(101)
print(f"El saldo es: {dinero.obtener_saldo()}")
dinero.depositar(201)
print(f"El saldo es: {dinero.obtener_saldo()}")
