# =============================================================================
# ENUNCIADO
# Crea una clase Persona con atributos nombre y edad.
# Añade un @classmethod llamado "desde_string" que reciba un string con el
# formato "Sergio:23", lo separe y devuelva una instancia de Persona creada
# con esos datos.
# Prueba crear una Persona de la forma normal y otra usando desde_string,
# e imprime ambas con __str__.
# =============================================================================

class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
        
    @classmethod
    def desde_string(cls, string):
        nombre, edad = string.split(":")
        return cls(nombre, int(edad))
    
    def __str__(self):
        return f"{self.nombre} tiene {self.edad} años"
    
persona = Persona("Sergio", 23)
persona2 = Persona.desde_string("Maria:21")
print(persona)
print(persona2)