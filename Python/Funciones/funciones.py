import math

def calcular_area_circulo(radio):
    area = math.pi * radio**2
    return area


radio_del_circulo = 5.0
area_del_circulo = calcular_area_circulo(radio_del_circulo)

print(f"El área del círculo con radio {radio_del_circulo} es: {area_del_circulo}")
