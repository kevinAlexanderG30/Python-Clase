def obtener_numero():

    while True:
        try:
            numero = int(input("Ingresa un número: "))   
            return numero
        except ValueError:
            print("Error: Debes ingresar un número válido. Intenta nuevamente.")

numero_ingresado = obtener_numero()
print(f"Has ingresado el número: {numero_ingresado}")
