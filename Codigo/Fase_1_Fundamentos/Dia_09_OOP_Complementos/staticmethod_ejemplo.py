# =============================================================================
# ENUNCIADO
# Crea una clase Calculadora sin atributos de instancia.
# Añade tres @staticmethod: sumar(a, b), restar(a, b) y multiplicar(a, b).
# Cada una recibe dos números y devuelve el resultado.
# Prueba llamarlas sin instanciar la clase: Calculadora.sumar(3, 5).
# =============================================================================


class Calculadora:
    @staticmethod
    def sumar(a, b):
        return a + b
    @staticmethod
    def restar(a, b):
        return a - b
    @staticmethod
    def multiplicar(a, b):
        return a * b
    
print(Calculadora.sumar(3, 5))
print(Calculadora.restar(10, 4))
print(Calculadora.multiplicar(6, 7))