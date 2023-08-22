listaInicial = ["Hola", "Como", "Estas","Todo", "Bien"]

listaBorrar = ["Estas", "Todo"]

def ObtenerNuevaLista(lista, borrar):
    #copiando
    # nuevaLista = lista.copy()
    # for i in borrar:
    #     nuevaLista.remove(i)
    # return nuevaLista

    nuevaLista = []
    for i in lista:
        if i not in borrar:
            nuevaLista.append(i)
    return nuevaLista

listaFinal = ObtenerNuevaLista(listaInicial, listaBorrar)

print("Elementos de la lista Incial => " + str(listaInicial))

print("Elementos de la lista Borrar => " + str(listaBorrar))

print("Elementos de la lista Final => " + str(listaFinal))