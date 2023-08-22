import random

def ObtenerValoresLista (cantidad = 0):
    nuevaLista = []

    for i in range(cantidad):
        valorRandom = random.randint(10,99)
        nuevaLista.append(valorRandom)
    
    return nuevaLista

def SumarLista (lista):
    valorSuma = 0

    for i in lista:
        valorSuma += i
    
    return valorSuma

def EliminarValor(lista, valorEliminar):
    if valorEliminar in lista:
        lista.remove(valorEliminar)
        print(f"Se eliminó {valorEliminar} de la lista.")
    return lista

def VerificarCapicua(lista):
    esCapicua = False
    if (len(lista) >= 2):
        if lista[0] == lista[(len(lista) - 1)]:
            esCapicua = True
    if (esCapicua == True):
        print("Esta Lista es Capicua")
    else:
        print("Esta Lista no es Capicua")
            


listaInicial = ObtenerValoresLista(4)
print("Elementos de la lista => " + str(listaInicial))

print("La Suma de estos numeros da " + str(SumarLista(listaInicial)))

inputEliminar = int(input("Que numero desea Eliminar => "))

listaInicial = EliminarValor(listaInicial, inputEliminar)
print("Elementos de la lista Cambiada => " + str(listaInicial))

VerificarCapicua(listaInicial)
