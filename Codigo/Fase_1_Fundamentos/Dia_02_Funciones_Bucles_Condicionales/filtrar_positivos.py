# =============================================================================
# ENUNCIADO
# Escribe una función filtrar_positivos(lista) que reciba una lista de números
# y devuelva una nueva lista que contenga solo los positivos, ordenada de
# mayor a menor. El 0 no se considera positivo.
# Ejemplo: [-1, 5, 0, 3, -2, 8] → [8, 5, 3]
# =============================================================================

def filtrar_positivos(lista):
    numPos = []
    for num in lista:
        if num > 0:
            numPos.append(num)
    numPos.sort(reverse=True)
    return numPos

print(filtrar_positivos([100, -1, 50]))
