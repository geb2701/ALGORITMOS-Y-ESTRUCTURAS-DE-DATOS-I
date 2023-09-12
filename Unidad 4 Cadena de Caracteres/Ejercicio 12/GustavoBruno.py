mazo = []
palos = ["Basto","Espada","Copa","Oro"]

for palo in palos:
    for i in range(1,13):
        mazo.append(f"{str(i)} {palo}")

for carta in mazo:
    print(carta)