def calcularVuelto (t,d, tipoBilletes):
    vuelto=d-t
    vueltos = []
    if (vuelto > 0):
        

        for i in range(len(tipoBilletes)):
            vueltos.append(vuelto // tipoBilletes[i])
            vuelto = vuelto % tipoBilletes[i]

        for i in range(len(tipoBilletes)):
            if vueltos[i]>0:
                print("Billetes de " + str(tipoBilletes[i]) + ": " + str(vueltos[i]))
    elif(vuelto == 0):
        print("No hay que dar Vuelto")
    else:
        print("Aun le faltan $" + str(vuelto * - 1))

   
total=int(input("Ingresar el valor total de la compra: "))
dinero=int(input("Ingresar el valor de la compra:"))
tipoBilletes = [2000,1000,500,100,50,20,10,5,1]

if (total <= dinero):
    vueltos = calcularVuelto (total,dinero, tipoBilletes)
else:
    print(" El dinero suministrado es menor que el valor de la compra")