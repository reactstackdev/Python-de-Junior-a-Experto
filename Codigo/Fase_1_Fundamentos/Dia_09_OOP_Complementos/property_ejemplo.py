# =============================================================================
# ENUNCIADO
# Crea una clase Circulo con un atributo privado _radio.
# Añade una property "radio" que devuelva el radio.
# Añade un setter para "radio" que valide que el valor sea positivo —
# si no lo es, lanza ValueError.
# Añade una property "area" que calcule y devuelva el area (pi * r^2)
# sin que sea un atributo almacenado.
# Prueba crear un circulo, leer su area, cambiar el radio y volver a leer.
# =============================================================================

import math

class Circulo:


    def __init__(self, radio):
        self.radio = radio
        
    @property
    def radio(self):
        return self._radio
    
    @radio.setter
    def radio(self, num):
        if num > 0:
            self._radio = num
        else:
            raise ValueError("El radio debe ser un numero positivo")
        
    @property
    def area(self):
        return math.pi * self._radio ** 2
    
    
circulo = Circulo(5)
print(circulo.area)
circulo.radio = 10
print(circulo.area)