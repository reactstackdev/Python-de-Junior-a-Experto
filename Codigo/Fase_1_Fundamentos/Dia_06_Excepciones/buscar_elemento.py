# =============================================================================
# ENUNCIADO
# Escribe una función buscar_elemento(lista, indice) que devuelva el elemento
# de la lista en la posición indicada.
# Gestiona dos errores:
#   - IndexError: cuando el índice no existe en la lista.
#   - TypeError: cuando el índice no es un entero.
# Pruébala con tres casos: uno válido, uno con índice fuera de rango,
# y uno pasando un string como índice.
# =============================================================================

def buscar_elemento(lista, indice):
    return lista[indice]

lista = [1, 2, 3, 4, 5]
try:
    lista1 = buscar_elemento(lista, 3)
    print(f"El elemento en la posición indicada es: {lista1}")
    lista2 = buscar_elemento(lista,73)
    print(f"El elemento en la posición indicada es: {lista2}")
    lista3 = buscar_elemento(lista, "3")
    print(f"El elemento en la posición indicada es: {lista3}")
except IndexError:
    print("El índice no existe en la lista, introduce otro número")
except TypeError:
    print("El índice debe ser un número entero, introduce otro número")
    
finally:
    print("Operación finalizada")