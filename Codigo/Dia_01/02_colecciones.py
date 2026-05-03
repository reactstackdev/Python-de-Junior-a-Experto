lenguajes = ["Java", "C", "Python", "PHP", "JavaScript"]
lenguajes.append("Nestjs")
print("Anyadimos: ", lenguajes)
lenguajes.pop(0)
print("Eliminamos: ", lenguajes)
print("Cantidad de elementos: ", len(lenguajes) )
print("Los 3 ultimos lenguajes son: ", lenguajes[-3:])