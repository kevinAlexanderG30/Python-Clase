contador = 1
while contador <= 5:
    print(contador)
    contador += 1


numeros = [2, 4, 6, 8, 10]
buscar_numero = 6
indice = 0
while numeros[indice] != buscar_numero:
    indice += 1
print(f"El número {buscar_numero} se encuentra en el índice {indice}")


numero_usuario = int(input("Ingrese un número mayor que 5: "))
while numero_usuario <= 5:
    print("El número ingresado no es mayor que 5.")
    numero_usuario = int(input("Ingrese un número mayor que 5: "))
print(f"¡Gracias! Has ingresado el número {numero_usuario}.")
