#Rellenar una matriz de 3x3. imprimirla en su orden y obtner e imprimir la suma y el promedio por cada fila de la matriz

matriz3 = []
a = int(input("Digite el número de filas: "))
b = int(input("Digite el número de columnas: "))

if a == 3 and b == 3:
    for i in range(a):
        matriz3.append([])
        for j in range(b):
            matriz3[i].append(None)
            
    for j in range(0, a):
        for i in range(0, b):
            matriz3[j][i] = int(input("Digite un número: "))
            
    print(matriz3)
    
    for j in range(0, a):
        suma = 0
        for i in range(0, b):
            suma += matriz3[j][i]
        print("La suma de la fila es: ", suma)
        print("El promedio de la fila es: ", suma/b)    
        
else:
    print("La matriz debe ser de 3x3")