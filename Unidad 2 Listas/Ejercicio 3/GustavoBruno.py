lista = []
cantidadElementos = int(input("Ingrese la Cantidad de Numeros => "))

for i in range(1, cantidadElementos):
    lista.append(i*i)

# esto puede fallar si es menor a 10
# for i in range(len(lista)-1,len(lista)-11,-1):
#     print(lista[i])

if (len(lista)>= 10):
    for i in range(len(lista)-1,len(lista)-11,-1):
        print(lista[i])
else:
    for i in range(len(lista)-1,-1,-1):
        print(lista[i])