# =============================================================================
# ENUNCIADO
# Define una clase Tarea con tres atributos: titulo, descripcion y completada
# (que empieza en False). Implementa dos métodos:
#   - completar(): cambia completada a True y devuelve su valor.
#   - mostrar(): devuelve un string formateado con la información de la tarea.
# Instancia una tarea, imprímela antes y después de completarla.
# =============================================================================

class Tarea:

    def __init__(self, titulo, descripcion):
        self.titulo = titulo
        self.descripcion = descripcion
        self.completada = False

    def completar(self):
        self.completada = True
        return self.completada

    def mostrar(self):
        return f"{self.titulo} {self.descripcion} y ¿está completada? la respuesta es: {self.completada}"

libro = Tarea(titulo="Quijote", descripcion="Y sancho panza")
print(libro.completada)
print(f"La obra es el: {libro.mostrar()}")
libro.completar()
print(libro.completada)
print(f"La obra es el: {libro.mostrar()}")
