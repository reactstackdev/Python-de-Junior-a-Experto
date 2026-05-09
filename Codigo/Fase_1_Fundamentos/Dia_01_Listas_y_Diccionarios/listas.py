# =============================================================================
# ENUNCIADO
# Crea una lista de al menos 5 lenguajes de programación. Después:
#   1. Añade un elemento al final con append().
#   2. Elimina el primer elemento con pop().
#   3. Imprime la cantidad total de elementos con len().
#   4. Imprime los 3 últimos elementos usando slicing negativo.
# =============================================================================

lenguajes = ["Java", "C", "Python", "PHP", "JavaScript"]
lenguajes.append("Nestjs")
print("Añadimos: ", lenguajes)
lenguajes.pop(0)
print("Eliminamos: ", lenguajes)
print("Cantidad de elementos: ", len(lenguajes))
print("Los 3 últimos lenguajes son: ", lenguajes[-3:])
