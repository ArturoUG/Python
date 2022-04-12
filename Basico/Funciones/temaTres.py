def imprimirMensaje():
    print("Estas son las funciones")
    print("Y ahorita vamos con las funciones con parametros")

imprimirMensaje()
imprimirMensaje()
imprimirMensaje()

def funcionesParametros(n1):
    n1 = int(n1)
    if n1 == 1:
        print("Escogiste el numero 1")
    elif n1 == 2:
        print("Escogiste el numero 2")
    elif n1 == 3:
        print("Escogiste el numero 3")
    else:
        print("Opcion invalida")

funcionesParametros(2)