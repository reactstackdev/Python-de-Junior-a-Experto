# =============================================================================
# ENUNCIADO — Parte 1: __str__ y herencia
# Parte 1: Renombra el método mostrar() de la clase Tarea a __str__ para que
# Python lo llame automáticamente al hacer print(objeto).
#
# Parte 2: Crea una clase TareaUrgente que herede de Tarea y añada el atributo
# prioridad (entero entre 1 y 3). Usa super().__init__() para no repetir código.
# Valida que la prioridad esté en rango con raise ValueError si no lo está.
# Sobreescribe __str__ para que también muestre la prioridad.
# =============================================================================

class Tarea:

    def __init__(self, titulo, descripcion):
        self.titulo = titulo
        self.descripcion = descripcion
        self.completada = False

    def completar(self):
        self.completada = True
        return self.completada

    def __str__(self):
        return f"{self.titulo} {self.descripcion} y ¿está completada? la respuesta es: {self.completada}"


class TareaUrgente(Tarea):
    def __init__(self, titulo, descripcion, prioridad):
        super().__init__(titulo, descripcion)
        if prioridad > 0 and prioridad < 4:
            self.prioridad = prioridad
        else:
            raise ValueError("La prioridad debe de ser un numero entre el 1 y el 3 incluidos")

    def __str__(self):
        return f"{self.titulo} {self.descripcion} y ¿está completada? la respuesta es: {self.completada}, esto tiene una prioridad {self.prioridad}"


libro = TareaUrgente("Lazarillo", "De Tormes", 2)
print(libro)
