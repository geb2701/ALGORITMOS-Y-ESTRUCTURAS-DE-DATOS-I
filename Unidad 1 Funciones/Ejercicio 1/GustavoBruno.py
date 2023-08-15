def EncontrarMayor(numero1, numero2, numero3):
    numeroMasAlto = numero1
    repetido = 0
    if (numeroMasAlto < numero2):
        numeroMasAlto = numero2
    elif (numeroMasAlto == numero2):
        repetido = 2
    
    if (numeroMasAlto < numero3):
        numeroMasAlto = numero3

        repetido = 0
    elif (numeroMasAlto == numero3):
        repetido += 1

    if (repetido > 0):
        numeroMasAlto = -1

    return numeroMasAlto

primerNumero = int(input("Ingrese el Primer Numero => "))
segundoNumero = int(input("Ingrese el Segundo Numero => "))
tercerNumero = int(input("Ingrese el Tercer Numero => "))

resultado = EncontrarMayor(primerNumero, segundoNumero, tercerNumero)

if resultado > 0:
    print("Numero mas alto = " + str(resultado))
else:
    print("No existe un numero mas alto")