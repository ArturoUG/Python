
pesoMexicano = 1
PesoArgentino = 2
PesoColombiano = 3

opc = int(input(f'''Menu de conversor de monedas
{pesoMexicano}) Peso Mexicano a Dolar
{PesoArgentino}) Peso Argentino a Dolar
{PesoColombiano}) Peso Colombiano a Dolar
Ingresa tu opcion deseada: '''))

if(opc == 1):
    pM = int(input("Ingresa la cantidad a convertir: "))
    pM = round(pM / 20.14, 2)
    print(f"{pM} Dolares")
elif(opc == 2):
    pA = int(input("Ingresa la cantidad a convertir: "))
    pA = round(pA / 111.9, 2)
    print(f"{pA} Dolares")
elif(opc == 3):
    pC = int(input("Ingresa la cantidad a convertir: "))
    pC = round(pC / 3759.3, 2)
    print(f"{pC} Dolares")
else:
    print("Ingresa una opcion valida. Intenta de nuevo")
