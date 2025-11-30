def es_primo(numero):
    """
    Verifica si un número es primo.
    Un número primo es un número mayor que 1 que solo es divisible por 1 y por sí mismo.
    """
    if numero < 2:
        return False
    
    # Comprobar divisibilidad desde 2 hasta la raíz cuadrada del número
    for i in range(2, int(numero ** 0.5) + 1):
        if numero % i == 0:
            return False
    
    return True


def obtener_primos(inicio, fin):
    """
    Obtiene todos los números primos en un rango específico.
    """
    primos = []
    for numero in range(inicio, fin + 1):
        if es_primo(numero):
            primos.append(numero)
    
    return primos


# Obtener los números primos entre 1 y 250
primos_1_250 = obtener_primos(1, 250)

# Guardar los resultados en un archivo
with open('resultados.txt', 'w') as archivo:
    archivo.write("Números primos entre 1 y 250\n")
    archivo.write("=" * 40 + "\n\n")
    archivo.write(f"Total: {len(primos_1_250)} números primos\n\n")
    archivo.write("Lista de números primos:\n")
    archivo.write(str(primos_1_250))

# Mostrar los resultados también en consola
print(f"Números primos entre 1 y 250:")
print(f"Total: {len(primos_1_250)} números primos")
print()
print(primos_1_250)
print("\n✓ Resultados guardados en 'resultados.txt'")
