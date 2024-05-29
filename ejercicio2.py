#Crear una matriz de 10x10. A continuación, pedir un enntero y una posición de la matriz y sustituir el entero situado en la posicion nueva introducida. vizualizar la matriz resultante.

import random
sust = [[random.randint(1, 100) for _ in range(10)] for _ in range(10)]

for i in range(10):
    for j in range(10):
        sust[i][j] = random.randint(1, 100)
        
print("La matriz es: ")

for i in range(10):
    print(sust[i])

nuevo = int(input("Digite un número nuevo: "))
fila = int(input("Digite la posicion de la fila: "))
columna = int(input("Digite la posicion de la columna: "))

sust[fila][columna] = nuevo

print("La matriz resultante es: ")

for i in range(10): 
    print(sust[i])