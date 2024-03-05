def mi_decorador(funcion_original):
    def nueva_funcion():
        print("Ejecutando código antes de la función original.")
        funcion_original()
        print("Ejecutando código después de la función original.")
    return nueva_funcion

@mi_decorador
def funcion_a_decorar():
    print("Esta es la función original.")


funcion_a_decorar()
