def sumar2Anteriores(n, n2, cantidad, lista = None):
    if (lista == None):
        lista = [n, n2]

    if (cantidad >= 0):
        numeroActual = n + n2
        cantidad -= 1
        lista.append(numeroActual)
        sumar2Anteriores(n2, numeroActual, cantidad, lista)
    return lista

print(sumar2Anteriores(0,1,10))
