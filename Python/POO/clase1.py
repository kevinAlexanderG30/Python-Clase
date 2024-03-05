class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def obtener_informacion(self):
        return f"Nombre: {self.nombre}, Edad: {self.edad} años"

# Uso de la clase Persona
persona1 = Persona("Juan", 25)
persona2 = Persona("María", 30)

print(persona1.obtener_informacion())
print(persona2.obtener_informacion())

# En este ejemplo, creamos una clase Persona con un constructor
# (__init__) que inicializa los atributos nombre y edad. También
# tenemos un método llamado obtener_informacion que devuelve una 
# cadena con la información de la persona. Luego, creamos dos instancias de la clase 
# Persona y mostramos su información.