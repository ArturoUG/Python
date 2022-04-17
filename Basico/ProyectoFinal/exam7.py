
def tiendaOnline():
    playera = 1
    blusa = 2 
    cazadora = 3
    pantalon = 4
    gorra = 5
    exit = 0
    cliente = input("Nombre: ")

    opc = int(input(f''' 
    {playera}.- Playera = $100
    {blusa}.- Blusa = $200
    {cazadora}.- Cazadora = $300
    {pantalon}.- Pantalon = $300
    {gorra}.- Gorra = $50
    {exit}.- Salir
    Ingresa la opcion/es a comprar: '''))

    while opc != 0:
        total = 0
        if opc == 1:
            many = int(input("Numero de prendas: "))
            total1 = 100 * many
            print(f"Su total por unidad: ${total1} ")
            total += total1 
        elif opc == 2:
            many = int(input("Numero de prendas: "))
            total2 = 200 * many
            print(f"Su total por unidad: ${total2} ")
            total += total2
        elif opc == 3:
            many = int(input("Numero de prendas: "))
            total3 = 300 * many
            print(f"Su total por unidad: ${total3} ")
            total += total3
        elif opc == 4:
            many = int(input("Numero de prendas: "))
            total4 = 300 * many
            print(f"Su total por unidad: ${total4} ")
            total += total4
        elif opc == 5:
            many = int(input("Numero de prendas: "))
            total5 = 50 * many
            print(f"Su total por unidad: ${total5} ")
            total += total5 
        elif opc == 0:
            print("Gracias.")
            

        opc = int(input(f''' 
        {playera}.- Playera = $100
        {blusa}.- Blusa = $200
        {cazadora}.- Cazadora = $300
        {pantalon}.- Pantalon = $300
        {gorra}.- Gorra = $50
        {exit}.- Salir
        Desea Seguir comprando: '''))

    print(f"{cliente}, su total es {total + total2 + total3 + total4 + total5} ")
        
    
            
    
if __name__ == '__main__':
    tiendaOnline()