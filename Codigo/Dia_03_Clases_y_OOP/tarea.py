# Ejercicio 3 — Directo al proyecto
# Define una clase Tarea que tendrás que usar luego en tu CLI. Que tenga: titulo, descripcion, 
# y completada (empieza en False). Un método completar() que cambie el estado a True, 
# y un método mostrar() que devuelva un string con la info de la tarea formateada (usa f-strings).

class Tarea():
    
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
print(libro.completada)   # Antes de completar
print(f"La obra es el: {libro.mostrar()}")
libro.completar()
print(libro.completada)   # Después de completar — ¿cambió algo?
print(f"La obra es el: {libro.mostrar()}")