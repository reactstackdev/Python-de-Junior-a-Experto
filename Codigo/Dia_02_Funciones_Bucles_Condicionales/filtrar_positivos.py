# Escribe una función filtrar_positivos(numeros) que reciba una lista y devuelva una nueva lista solo con los números positivos, ordenada de mayor a menor.
# Ejemplo: [-1, 5, 0, 3, -2, 8] → [8, 5, 3]



def filtrar_positivos(lista):
    # lista = [-1 ,-2, 5, 0, 7, 3, 0, 0, 1, 1, 1]
    numPos = []
    for num in lista:
        if num > 0:
            numPos.append(num)
    
    numPos.sort(reverse = True)
        
    return numPos 

print(filtrar_positivos([100, -1, 50]))