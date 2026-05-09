# =============================================================================
# ENUNCIADO
# Escribe una función resumir_lista(lista) que reciba una lista de números y
# devuelva un diccionario con el conteo de positivos, negativos y ceros:
# {"Positivos": 5, "Negativos": 3, "Ceros": 2}
# Llámala con una lista de ejemplo e imprime el resultado.
# =============================================================================

lista = [-1, -2, 5, 0, 7, 3, 0, 0, 1, 1, 1]
numeros = {}

def resumir_lista(num):
    countPos, countNeg, countCer = 0, 0, 0
    for num in lista:
        if num > 0:
            countPos += 1
        elif num < 0:
            countNeg += 1
        else:
            countCer += 1
    numeros["Positivos"] = countPos
    numeros["Negativos"] = countNeg
    numeros["Ceros"] = countCer
    return numeros

print(f"{resumir_lista(lista)}")
