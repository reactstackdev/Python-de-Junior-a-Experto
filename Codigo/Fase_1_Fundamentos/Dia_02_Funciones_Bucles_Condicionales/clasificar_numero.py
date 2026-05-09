# =============================================================================
# ENUNCIADO
# Escribe una función clasificar_numero(num) que reciba un entero y devuelva
# el string "positivo", "negativo" o "cero" según corresponda.
# Crea una lista con al menos 5 números (positivos, negativos y el cero),
# recórrela con un bucle y llama a la función con cada elemento imprimiendo:
# "El numero: 3 es positivo".
# =============================================================================

def clasificar_numero(num):
    if num > 0:
        return "positivo"
    elif num < 0:
        return "negativo"
    else:
        return "cero"

lista = [0, 2, -3, 4, -5, 6, -7, -8, 9, 10]

for num in lista:
    print(f"El numero: {num} es {clasificar_numero(num)}")
