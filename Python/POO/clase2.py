class Rectangulo:
    def __init__(self, longitud, ancho):
        self.longitud = longitud
        self.ancho = ancho

    def calcular_area(self):
        return self.longitud * self.ancho

    def calcular_perimetro(self):
        return 2 * (self.longitud + self.ancho)


rectangulo1 = Rectangulo(5, 8)
rectangulo2 = Rectangulo(10, 3)

print(f"Área del rectángulo 1: {rectangulo1.calcular_area()}")
print(f"Perímetro del rectángulo 1: {rectangulo1.calcular_perimetro()}")

print(f"Área del rectángulo 2: {rectangulo2.calcular_area()}")
print(f"Perímetro del rectángulo 2: {rectangulo2.calcular_perimetro()}")
