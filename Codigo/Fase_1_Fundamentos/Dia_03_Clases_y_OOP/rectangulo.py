# =============================================================================
# ENUNCIADO
# Define una clase Rectangulo con dos atributos (ancho y alto) y dos métodos:
# area() y perimetro(). Los métodos deben retornar el valor calculado, nunca
# imprimirlo dentro. Instancia al menos un rectángulo y prueba ambos métodos.
# =============================================================================

class Rectangulo:
    def __init__(self, ancho, alto):
        self.ancho = ancho
        self.alto = alto

    def area(self):
        area_total = self.ancho * self.alto
        return area_total

    def perimetro(self):
        perimetroTotal = 2 * (self.ancho + self.alto)
        return perimetroTotal

figura = Rectangulo(ancho=20, alto=40)
print(f"El area de la figura es: {figura.area()}")
print(f"El perimetro de la figura es: {figura.perimetro()}")
