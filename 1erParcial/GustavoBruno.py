def Ejercicio1():
    def OrdenarPorInsercion(lista): 
        n=len(lista)
        for i in range(1,n):
            desordenadoCuenta=lista[i]
            c=i
            while (c >0 and lista[c-1][0] > desordenadoCuenta[0]):
                lista[c]=lista[c-1]
                c-=1
            lista[c]=desordenadoCuenta

    def ObtenerCuentas():
        print("Ingreso de Cuentas")
        cuentas=[]
        cuentaActual = 0
        while cuentaActual != -1:
            cuentaActual = int(input("Por favor, Ingrese el numero de cuenta, ponga -1 para finalizar => "))
            if cuentaActual <= 0 and cuentaActual != -1:
                print("El numero de cuenta no puede 0 o menor")
            elif cuentaActual != -1:
                yaCargada = False
                for cuenta in cuentas:
                    if yaCargada == False and cuenta[0] == cuentaActual:
                        yaCargada = True
                    
                if yaCargada:
                    print("Esta cuenta ya fue cargada")
                else:
                    saldo = int(input("Por favor, Ingrese el saldo de la cuenta => "))
                    while saldo < 0:
                        print("El Saldo no puede ser menor a 0")
                        saldo = int(input("Por favor, Ingrese el saldo de la cuenta => "))

                    gastos = []
                    ultimoGasto = 0
                    while ultimoGasto != -1:
                        print(f"Saldo actual de la cuenta es ${saldo}")
                        ultimoGasto = int(input("Por favor, Ingrese el gasto de la cuenta, ponga -1 para finalizar la carga de gastos => "))
                        if ultimoGasto <= 0 and ultimoGasto != -1:
                            print("Los gastos no pueden 0 o menores")
                        else:
                            if ultimoGasto> saldo:
                                print("Los gastos no pueden mayores al saldo")
                            else:
                                gastos.append(ultimoGasto)
                                saldo -= ultimoGasto

                    registroCuenta = [cuentaActual, saldo]
                    cuentas.append(registroCuenta)
        return cuentas

    def CuentaConMenorValor(lista):
        cuentasMinimas = []
        minimoActual = -1
        for cuenta in lista:
            if minimoActual == -1 or cuenta[1] < minimoActual:
                cuentasMinimas = [cuenta]
                minimoActual = cuenta[1]
            elif cuenta[1] == minimoActual:
                cuentasMinimas.append(cuenta)
        print("Cuentas Minimas")
        for cuentas in cuentasMinimas:
            print(f"Nro. Cuenta: {cuentas[0]}, Saldo: {cuentas[1]}")

    def PromedioSaldos(lista):
        saldoTotal = 0
        for cuenta in lista:
            saldoTotal += cuenta[1]
        promedio = saldoTotal/len(lista)

        print(f"El promedio de las cuentas es ${promedio}")

    def PorcentajeMinimo(lista):
        cantidadCuentas = 0
        for cuenta in lista:
            if cuenta[1]>= 59000:
                cantidadCuentas += 1
        porcentaje = 100 * cantidadCuentas / len(lista)
        print(f"El porcentaje de saldos menores o iguales a 59000 es de {porcentaje}%")

    def SaldoMaximo(lista):
        saldoMaximo = 0
        for cuenta in lista:
            if cuenta[1] > saldoMaximo:
                saldoMaximo = cuenta[1]

        print(f"El saldo mas alto es de ${saldoMaximo}")

    def ListadoCuentas(lista):
        print("Listado de Cuentas")
        for cuenta in lista:
            print(f"Nro. Cuenta: {cuenta[0]}, Saldo: {cuenta[1]}")
    print("Sistema de Cuentas")
    cuentas = ObtenerCuentas()
    OrdenarPorInsercion(cuentas)

    listaOpciones = [
        ["Cuentas Con Saldo Menor Saldo", CuentaConMenorValor],
        ["Promedio Saldos", PromedioSaldos],
        ["Porcentaje de saldos menores o iguales a 59000", PorcentajeMinimo],
        ["Saldo Maximo", SaldoMaximo],
        ["Listado Cuentas", ListadoCuentas]
    ]

    opcion = 0
    while opcion != -1:
        print("Opciones:")
        for i in range(len(listaOpciones)):
            print(f"{i + 1}) {listaOpciones[i][0]}")
        print(f"-1) Finalizar programa")

        opcion = int(input("Seleccione la opcion a trabajar => "))
        if opcion > 0 and opcion <= len(listaOpciones) + 1:
            listaOpciones[opcion - 1][1](cuentas)
            input("Ingrese para continuar => ")
        elif opcion != -1:
            print("Opcion Invalida")

def Ejercicio2():
    def FiltrarPalabrasA(cadena, n):
        #ciclos normales
        lista = cadena.split()

        nuevaCadena =[]
        for palabra in lista:
            if len(palabra)>=n:
                nuevaCadena.append(palabra)

        return nuevaCadena

    def FiltrarPalabrasB(cadena, n):
        #ciclos por compresion
        lista = cadena.split()

        nuevaCadena = []
        palabrasCorrectas = [len(palabra)>=n for palabra in lista]

        for i in range(len(lista)):
            if palabrasCorrectas[i]:
                nuevaCadena.append(lista[i])

        return nuevaCadena

    def FiltrarPalabrasC(cadena, n):
        #filter
        lista = cadena.split()

        nuevaCadena = list(filter(lambda x: len(x)>=n, lista))

        return nuevaCadena

    def VerificarError (lista, n):
        error = False
        for palabra in lista:
            if len(palabra)<n:
                error = True
        return error

    cadena = str(input("Ingrese la cadena de texto => "))
    minimoPalabra = int(input("Ingrese el minimo tamaño de la palabra => "))

    listaOpciones = [
        ["Ciclo Normal", FiltrarPalabrasA],
        ["Listas de Compresión", FiltrarPalabrasB],
        ["Funcion Filter", FiltrarPalabrasC]
    ]

    opcion = 0
    while opcion != -1:
        print("Opciones:")
        for i in range(len(listaOpciones)):
            print(f"{i + 1}) {listaOpciones[i][0]}")
        print(f"-1) Finalizar programa")

        opcion = int(input("Seleccione la opcion a trabajar => "))
        if opcion > 0 and opcion <= len(listaOpciones) + 1:
            resultado = listaOpciones[opcion - 1][1](cadena, minimoPalabra)
            if VerificarError(resultado, minimoPalabra):
                print("Se ha detectado un error")
            else:
                if len(resultado) == 0:
                    print("No hay palabras que cumplan las condiciones dadas")
                else:
                    for palabra in resultado:
                        print(palabra, end=" ")
            input("\nIngrese para continuar => ")
        elif opcion != -1:
            print("Opcion Invalida")

ejercicio = int(input("ingrese el numero de ejercicio => "))

if ejercicio == 1:
    Ejercicio1()
elif ejercicio == 2:
    Ejercicio2()

print("Fin")