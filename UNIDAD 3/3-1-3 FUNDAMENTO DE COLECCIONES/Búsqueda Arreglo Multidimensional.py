# Búsqueda Arreglo Multidimensional
# Creación de una matriz de 3x3

matriz = [
    [2, 3, 25],
    [58, 30, 1],
    [23, 10, 9]
]

def buscar_valor(matriz,valor):

# Recorrer y Buscar el valor
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            if matriz[i][j] == valor:
             return i, j # Retorna la posición
    return None

# Solcitar el valor a buscar
numero_buscar = 9

# Llamo a la función
resultado = buscar_valor(matriz,numero_buscar)

if resultado:
    print(f"el resultado del número {numero_buscar} se encuentra en la posición {resultado[0]} {resultado[1]}")
else:
    print(f"el numero no se encuentra en la matriz")