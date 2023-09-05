def matrizA(n):
    nuevaMatriz = []

    for i in range (n):
        nuevaMatriz.append([])
        for j in range (n):
            if (i == j):
                valor = (i*2) + 1
            else: 
                valor = 0
            nuevaMatriz[i].append(valor)
    
    return nuevaMatriz
    
n = int(input("Ingrese el tamaño de la matriz => "))
nuevaMatriz = matrizA(n)
for linea in nuevaMatriz:
    print(linea)



