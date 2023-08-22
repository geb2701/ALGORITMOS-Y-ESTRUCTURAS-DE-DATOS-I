def VerificarListaAcendente(lista):
    valido = True
    for i in range(len(lista) - 1):
        if lista[i] >=  lista[i +1]:
            valido = False
    return valido 

lista = [1,2]
estaOrdenada = VerificarListaAcendente(lista)

if len(lista) != 0:
    if estaOrdenada == True:
        print("Lista Ordenada")
    else:
        print("Lista Desordenada")
else:
    print("Lista Invalida")