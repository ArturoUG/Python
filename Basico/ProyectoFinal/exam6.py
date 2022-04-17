def ciudades():
    mexicoCity = 1
    guadalajara = 2
    acapulco = 3
    cancun = 4
    cabos = 5 
    monto = 0

    ciudades = int(input(f'''ciudades
    {mexicoCity}.- Ciudad de México = 200
    {guadalajara}.- Guadalajara = 100
    {acapulco}.- Acapulco = 200
    {cancun}.- Cancun = 400
    {cabos}.- Cabos = 500 
    Ingrese el numero de la ciudad a viajar: '''))

    if ciudades == 1:
        return 200
    elif ciudades == 2:
        return 100
    elif ciudades == 3:
        return 200
    elif ciudades == 4:
        return 400
    elif ciudades == 5:
        return 500
    else:
        print("Ingrese una opcion correcta.")

def fechas():
    total = ciudades()
    uno = 1 
    tres = 2
    seis = 3
    dosw = 4

    dias = int(input(f'''Con cuantos dias de anticipacion esta realizando su compra
    NOTA: Cuanto menos tiempo mas se multiplicara el total.
    {uno}.- un dia
    {tres}.- tres dias o mas
    {seis}.- Seis dias o mas
    {dosw}.- Dos semanas o mas
    Ingrese la opcion deseada: '''))

    if dias == 1:
        total = total * 5
    elif dias == 2:
        total = total * 4
    elif dias == 3:
        total = total * 2
    elif dias == 4:
        total = total * 1
    else:
        print("Ingrese una opcion correcta.")
    print(f"El total es: {total}")

def maxmin():
    cont = 0
    while cont != 3:
        opc = input("Desea comprar un boleto Si=S / No=N: ")
        if opc == "S":
            cont += 1
            fechas()
            print(f"Su asiento es el numero: {cont}")
        else:
            print("Gracias")
            break
        print(f"Numero de pasajeros al momento: {cont}")

if __name__ == '__main__':
    maxmin()