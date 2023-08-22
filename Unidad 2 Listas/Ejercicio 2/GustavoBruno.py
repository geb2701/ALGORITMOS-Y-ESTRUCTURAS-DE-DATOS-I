import random

def ObtenerValoresLista (cantidad = 0):
    nuevaLista = []

    for i in range(cantidad):
        valorRandom = random.randint(1,100)
        nuevaLista.append(valorRandom)
    
    return nuevaLista

def VerificarRepetido(lista):
    posicionLista = 0
    encontreRepetido = False
    while posicionLista < len(lista) and encontreRepetido == False:
        valorLista = lista[posicionLista]
        
        posicionComparacion = posicionLista + 1
        while posicionComparacion < len(lista) and encontreRepetido == False:
            if valorLista == lista[posicionComparacion]:
                encontreRepetido = True
            posicionComparacion += 1
        posicionLista += 1
    return encontreRepetido

def EliminarRepetidosListaSencilla(lista):
    return list(set(lista))

def EliminarRepetidosLista(lista):
    nuevaLista = []

    for i in lista:
        if i not in nuevaLista:
            nuevaLista.append(i)

    return nuevaLista

listaInicial = ObtenerValoresLista(50)
print("Elementos de la lista => " + str(listaInicial))

valoresRepetidos = VerificarRepetido(listaInicial)

if (valoresRepetidos == True):
    print("Existen Valores Repetidos")
else:
    print("No Existen Valores Repetidos")

print("Elementos de la lista Cambiada => " + str(EliminarRepetidosLista(listaInicial)))