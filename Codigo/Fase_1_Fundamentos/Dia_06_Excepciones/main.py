# =============================================================================
# ENUNCIADO
# Escribe una función dividir(a, b) que divida a entre b.
# Gestiona los siguientes errores sin que el programa pete:
#   - ZeroDivisionError: cuando b es cero.
#   - TypeError: cuando alguno de los argumentos no es numérico.
# Usa un bloque try/except con un except por cada tipo de error.
# Añade un bloque finally que imprima "Operación finalizada" siempre,
# tanto si hubo error como si la división fue exitosa.
# =============================================================================

def dividir(a, b):
    return a / b

try:
    retultado = dividir(10, 2)
    print(f"El resultado de la división es: {retultado}")
    retultado2 = dividir(10, 0)
    print(f"El resultado de la división es: {retultado2}")
except ZeroDivisionError:
    print("No se puede dividir por cero, introduce otro número")
except TypeError:
    print("No se puede dividir por un valor que no sea numérico, introduce otro número")
finally:
    print("Operación finalizada")
