def pasarNumeroAPalabra(numero):
    textoSalida = "SON:"
    

    #billon
    auxiliar = 0
    while numero >= 1000000000000:
        numero -= 1000000000000
        auxiliar += 1
    if auxiliar > 0:
        textoSalida += f" {pasarLetraHastaTresDigitos(auxiliar)}"
        if auxiliar == 1:
            textoSalida += " BILLONES"
        else:
            textoSalida += " BILLON"


    #mil millones
    auxiliar = 0
    adeudaMillon = 0
    while numero >= 1000000000:
        numero -= 1000000000
        auxiliar += 1
    if auxiliar > 0:
        textoSalida += f" {pasarLetraHastaTresDigitos(auxiliar)} MIL"
        adeudaMillon = True

    #millones
    auxiliar = 0
    unSoloMillon = False
    while numero >= 1000000:
        numero -= 1000000
        auxiliar += 1
    if auxiliar > 0:
        textoSalida += f" {pasarLetraHastaTresDigitos(auxiliar)}"
        if adeudaMillon == False and auxiliar == 1:
            unSoloMillon = True

        adeudaMillon = True
    if unSoloMillon:
        textoSalida += f" MILLON"
    elif adeudaMillon:
        textoSalida += f" MILLONES"

    #miles
    auxiliar = 0
    while numero >= 1000:
        numero -= 1000
        auxiliar += 1
    if auxiliar > 0:
        textoSalida += f" {pasarLetraHastaTresDigitos(auxiliar)} MIL"

    #cientos o inferior
    textoSalida += f" {pasarLetraHastaTresDigitos(numero,False)}"

    return textoSalida


def pasarLetraHastaTresDigitos(numero, vieneHeredado = True):
    if (numero == 0):
        retorno = ""
    elif (numero == 1 and vieneHeredado):
        retorno = "UN"
    else:
        mayorDiez = False
        if numero > 10:
            mayorDiez = True
        hasta10 = ["UNO","DOS","TRES","CUATRO","CINCO","SEIS","SIETE","OCHO","NUEVE"]
        hasta100 = ["DIEZ","VIENTE","TREINTA","CUARENTA","CIENCUENTA","SESENTA","SETENTA","OCHENTA","NOVENTA"]
        hasta1000 = ["CIENTO","DOCIENTOS","TRESCIENTOS","CUATROCIENTOS","QUINIENTOS","SIECIENTOS","SIETECIENTOS","OCHOCIENTOS","NUEVECIENTOS"]

        especiales = [[11,"ONCE"], [12,"DOCE"], [13,"TRECE"], [14,"CATORCE"], [15,"QUINCE"]]
        retorno = ""

        auxiliar = 0
        while numero >= 100:
            numero -= 100
            auxiliar += 1
        if (auxiliar != 0):
            retorno += hasta1000[auxiliar-1]
        
        esEspecial = None
        for elemento in especiales:
            if numero == elemento[0]:
                esEspecial = elemento[1]

        if esEspecial != None:
            retorno += " " + esEspecial
        else:
            auxiliar = 0
            while numero >= 10:
                numero -= 10
                auxiliar += 1
            if (auxiliar != 0):
                retorno += " " + hasta100[auxiliar-1]
            if numero != 0:
                if mayorDiez:
                    retorno += " Y "
                retorno += hasta10[numero-1]
    
    return retorno

print(pasarNumeroAPalabra(int(input("Ingrese el Número a Convertir => "))))