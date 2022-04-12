

def calculoMonedas(tipoMoneda, valorDolar):
    pesos = int(input(f"Cuantos pesos {tipoMoneda} tienes: "))
    pesos = round(pesos / valorDolar, 2)
    print(f"{pesos} Dolares")

pesoMexicano = 1
PesoArgentino = 2
PesoColombiano = 3

opc = int(input(f'''Menu de conversor de monedas
{pesoMexicano}) Peso Mexicano a Dolar
{PesoArgentino}) Peso Argentino a Dolar
{PesoColombiano}) Peso Colombiano a Dolar
Ingresa tu opcion deseada: '''))

if(opc == 1):
    calculoMonedas("Mexicanos",20.14)
elif(opc == 2):
    calculoMonedas("Argentinos", 111.9)
elif(opc == 3):
    calculoMonedas("Colombianos", 3759.3)
else:
    print("Ingresa una opcion valida. Intenta de nuevo")
