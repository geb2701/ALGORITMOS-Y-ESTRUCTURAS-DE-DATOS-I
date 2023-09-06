def MatrizA(n):
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

def MatrizB(n):
    nuevaMatriz = []

    poner = n -1
    for i in range (n):
        nuevaMatriz.append([])
        for j in range (n):
            if (j == poner):
                valor = 3 ** (poner)
                poner -= 1
            else: 
                valor = 0
            nuevaMatriz[i].append(valor)
    
    return nuevaMatriz

def MatrizC(n):
    nuevaMatriz = []

    cantidad = 1
    for i in range (n):
        nuevaMatriz.append([])
        cantidadActual = 0
        for j in range (n):
            if (cantidadActual < cantidad):
                valor = n - i
            else: 
                valor = 0
            cantidadActual += 1
            nuevaMatriz[i].append(valor)
        cantidad +=1
    
    return nuevaMatriz

def MatrizD(n):
    nuevaMatriz = []

    for i in range (n):
        nuevaMatriz.append([])
        for j in range (n):
            nuevaMatriz[i].append(2 ** (n - i - 1))

    return nuevaMatriz

def MatrizE(n):
    nuevaMatriz = []
    poner = False
    valor = 0
    for i in range (n):
        nuevaMatriz.append([])
        for j in range (n):
            if poner:
                valor += 1
                nuevaMatriz[i].append(valor)
                poner = False
            else:
                nuevaMatriz[i].append(0)
                poner = True
        if poner:
            poner = False
        else:
            poner = True
    return nuevaMatriz

def MatrizF(n):
    nuevaMatriz = []
    
    valor = 0
    for i in range (n):
        nuevaMatriz.append([])
        for j in range (n):
            nuevaMatriz[i].append(0)
        
        cantidad = i + 1
        cantidadActual = 0
        for j in range (n -1, -1, -1):
            if cantidad > cantidadActual:
                valor += 1
                nuevaMatriz[i][j] = valor
                cantidadActual += 1
            else:
                break

    return nuevaMatriz

def MatrizG(n):
    nuevaMatriz = []
    for i in range (n):
        nuevaMatriz.append([])
        for j in range (n):
            nuevaMatriz[i].append(0)

    maximoX = n
    maximoY = n
    minimoY = 0
    minimoX = -1
    valor = 1

    actualX = 0
    actualY = 0

    MovemosDerecha = True
    MovemosIzquierda = False
    MovemosArriba = False
    MovemosAbajo = False

    while valor <= n*n:
        if MovemosDerecha:
            if actualX == maximoX:
                maximoX -= 1
                actualX -= 1
                actualY += 1
                MovemosDerecha = False
                MovemosAbajo = True
            else:
                nuevaMatriz[actualY][actualX] = valor
                valor += 1
                actualX += 1
        elif MovemosAbajo:
            if actualY == maximoY:
                maximoY -= 1
                actualY -= 1
                actualX -= 1
                MovemosAbajo = False
                MovemosIzquierda = True
            else:
                nuevaMatriz[actualY][actualX] = valor
                valor += 1
                actualY += 1
        elif MovemosIzquierda:
            if actualX == minimoX:
                minimoX += 1
                actualX += 1
                actualY -= 1
                MovemosIzquierda = False
                MovemosArriba = True
            else:
                nuevaMatriz[actualY][actualX] = valor
                valor += 1
                actualX -= 1
        elif MovemosArriba:
            if actualY == minimoY:
                minimoY += 1
                actualY += 1
                actualX += 1
                MovemosArriba = False
                MovemosDerecha = True
            else:
                nuevaMatriz[actualY][actualX] = valor
                valor += 1
                actualY -= 1
    return nuevaMatriz

def MatrizH(n):
    nuevaMatriz = []
    for i in range (n):
        nuevaMatriz.append([])
        for j in range (n):
            nuevaMatriz[i].append(0)

    x = 0
    actualX = 0
    y = 0
    actualY = 0
    valor = 0
    encontramosDiagonal = False
    cantidadDiagonal = 0
    while valor < n*n:
        if actualX >= 0 and actualX < n and actualY >= 0 and actualY < n:
            valor += 1
            nuevaMatriz[actualY][actualX] = valor
            cantidadDiagonal += 1
            actualX -= 1
            actualY += 1
        else:
            
            if cantidadDiagonal == n:
                encontramosDiagonal = True
            cantidadDiagonal = 0
            
            if encontramosDiagonal:
                y += 1
                actualY = y
                actualX = n -1
            else:
                x += 1
                actualX = x
                actualY = y

    return nuevaMatriz

n = int(input("Ingrese el tamaño de la matriz => "))

listaOpciones = [
    ["A", MatrizA],
    ["B", MatrizB],
    ["C", MatrizC],
    ["D", MatrizD],
    ["E", MatrizE],
    ["F", MatrizF],
    ["G", MatrizG],
    ["H", MatrizH]
]

print("Opciones:")
for i in range(len(listaOpciones)):
    print(f"{i + 1}) {listaOpciones[i][0]}")

opcion = int(input("Ingrese el matriz a obtener => "))
if opcion > 0 and opcion <= len(listaOpciones) + 1:
    nuevaMatriz = listaOpciones[opcion - 1][1](n)
    print("Nueva Matriz")
    for linea in nuevaMatriz:
        print(linea)

print("Fin")



