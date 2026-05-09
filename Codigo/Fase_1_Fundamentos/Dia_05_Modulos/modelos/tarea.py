# =============================================================================
# ENUNCIADO — Módulo: modelos/tarea.py
# Este fichero es un módulo dentro del paquete modelos. Contiene las clases
# Tarea y TareaUrgente sin código de prueba. Se importa desde main.py con:
#   from modelos.tarea import Tarea
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
