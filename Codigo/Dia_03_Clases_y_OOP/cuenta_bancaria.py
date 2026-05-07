# Ejercicio 2 — Un paso más
# Define una clase CuentaBancaria con un atributo saldo inicial (se pasa al crear la cuenta) 
# y tres métodos: depositar(cantidad), retirar(cantidad) y obtener_saldo(). 
# El método retirar debe devolver False si no hay saldo suficiente, y True si la operación fue exitosa.

class CuentaBancaria():
    def __init__(self, saldo):
        self.saldo = saldo
    
    def depositar(self, cantidad):
        self.saldo = self.saldo + cantidad
        return self.saldo
    
    def retirar(self, cantidad):
        if self.saldo >= cantidad:
            self.saldo= self.saldo - cantidad
            return True
        else:
            return False
        
    def obtener_saldo(self):
        return self.saldo
    
dinero = CuentaBancaria(saldo = 200)
print(f"El saldo es: {dinero.obtener_saldo()}")
dinero.retirar(100)
print(f"El saldo es: {dinero.obtener_saldo()}")
dinero.retirar(101)
print(f"El saldo es: {dinero.obtener_saldo()}")
dinero.depositar(201)
print(f"El saldo es: {dinero.obtener_saldo()}")