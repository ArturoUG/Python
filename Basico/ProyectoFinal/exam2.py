

def menu():

    suma = 1
    resta = 2
    multiplicacion = 3
    division = 4
    exit = 0

    print(f''' Opciones
    {suma}) Suma
    {resta}) Resta
    {multiplicacion}) Multiplicacion
    {division}) Division
    {exit}) Salir''')

def suma():
    print("= SUMA =")
    num1 = int(input("Numero 1: "))
    num2 = int(input("Numero 2: "))
    total = num1 + num2
    print (total)

def resta():
    print("= RESTA =")
    num1 = float(input("Numero 1: "))
    num2 = float(input("Numero 2: "))
    total = num1 - num2
    print (total)

def multiplicacion():
    print("= MULTIPLICACION =")
    num1 = float(input("Numero 1: "))
    num2 = float(input("Numero 2: "))
    total = num1 * num2
    print (total)

def division():
    print("= DIVISION =")
    num1 = float(input("Numero 1: "))
    num2 = float(input("Numero 2: "))
    total = num1 / num2
    print (total)

def calculadora():

    menu()
    opc = int(input("Ingresa la opcion deseada: "))

    while(opc != 0):
        if opc == 1:
            suma()
        elif opc == 2:
            resta()
        elif opc == 3:
            multiplicacion()
        elif opc == 4:
            division()
        elif opc == 0:
            print("Gracias. Nos vemos")
        else:
            print("Ingresa una opcion correcta.")

        menu()
        opc = int(input("Ingresa la opcion deseada: "))
    
if __name__ == "__main__":
    calculadora()
