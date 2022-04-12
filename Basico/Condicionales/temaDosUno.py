
print("1.Conversion de Pesos mexicanos a Dolares")
print("2.Conversion de Dolares a Pesos mexicanos")
opc = int(input("Ingresa la opcion deseada: "))

if(opc == 1):
    peso = int(input("Ingresa la cantidad a convertir: "))
    total = round(peso / 20.14, 2)
    print (f"{total} dolares")
elif(opc == 2):
    dolar = int(input("Ingresa la cantidad a convertir: "))
    total = dolar * 20.14
    print (f"{total} pesos mexicanos")
else:
    print("Ingresa una opcion correcta")
     


