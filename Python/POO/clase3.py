class Carro:
    def __init__(self, marca, modelo, color, combustible="Gasolina"):
        self.marca = marca
        self.modelo = modelo
        self.color = color
        self.combustible = combustible
        self.encendido = False  # Atributo para representar el estado del carro

    def obtener_informacion(self):
        estado_encendido = "encendido" if self.encendido else "apagado"
        return f"Carro {self.marca} {self.modelo} ({self.color}) - Combustible: {self.combustible}, Estado: {estado_encendido}"

    def encender(self):
        if not self.encendido:
            self.encendido = True
            print("El carro ha sido encendido.")
        else:
            print("El carro ya está encendido.")

    def apagar(self):
        if self.encendido:
            self.encendido = False
            print("El carro ha sido apagado.")
        else:
            print("El carro ya está apagado.")

# Uso de la clase Carro
carro1 = Carro("Toyota", "Camry", "Azul")
carro2 = Carro("Honda", "Civic", "Rojo", "Híbrido")

print(carro1.obtener_informacion())
carro1.encender()
print(carro1.obtener_informacion())
carro1.apagar()
print(carro1.obtener_informacion())

print(carro2.obtener_informacion())
carro2.encender()
print(carro2.obtener_informacion())
