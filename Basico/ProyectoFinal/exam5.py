def agenda():    
    print("= Agenda de Contactos =")
    nombre = input("Ingresa nombre: ")
    tel = int(input("Telefono: "))
    email = input("Email: ")

    agenda = (nombre, tel, email)
    print(agenda)


def facturacion():
    print("= Servicio de facturacion = ")
    nombre = input("Cliente: ")
    id = int(input("ID: "))
    telefono = int(input("Telefono: "))
    direccion = input("Direccion: ")
    producto = input("Nombre del producto: ")
    cantidad = int(input("Cantidad: "))
    valor = int(input("Valor de la unidad: "))
    valorxUnidad = cantidad * valor
    total = (f"En total es {valorxUnidad}")

    facturacion = {"nombre":nombre, "id":id, "telefono":telefono, "direccion":direccion,
    "producto":producto, "cantidad":cantidad, "valor": valor, "Valor por Unidad":valorxUnidad,
    "total":total}
    for k,v in facturacion.items():
        print(f"{k} - {v}")


def controlVehicular():
    multa = int(input("Ingresa tu monto de tu multa: "))
    if multa == 2500:
        print("Puede circular")
    else:
        print("No ingreso correctamente el total de su multa.")
    






controlVehicular()