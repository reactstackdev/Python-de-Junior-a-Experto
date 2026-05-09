# =============================================================================
# ENUNCIADO — Parte 2: Encapsulación
# Aplica la convención de encapsulación de Python: renombra el atributo
# completada a _completada en toda la clase Tarea (en __init__, completar()
# y __str__). El guion bajo indica que es de uso interno.
# Comprueba que el comportamiento externo no cambia.
# =============================================================================

class Tarea:

    def __init__(self, titulo, descripcion):
        self.titulo = titulo
        self.descripcion = descripcion
        self._completada = False

    def completar(self):
        self._completada = True
        return self._completada

    def __str__(self):
        return f"{self.titulo} {self.descripcion} y ¿está completada? la respuesta es: {self._completada}"


class TareaUrgente(Tarea):
    def __init__(self, titulo, descripcion, prioridad):
        super().__init__(titulo, descripcion)
        if prioridad > 0 and prioridad < 4:
            self.prioridad = prioridad
        else:
            raise ValueError("La prioridad debe de ser un numero entre el 1 y el 3 incluidos")

    def __str__(self):
        return f"{self.titulo} {self.descripcion} y ¿está completada? la respuesta es: {self._completada}, esto tiene una prioridad {self.prioridad}"


libro = TareaUrgente("Lazarillo", "De Tormes", 2)
print(libro)
