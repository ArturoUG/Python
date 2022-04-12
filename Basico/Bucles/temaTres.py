def esPrimo():
    num = int(input("Ingresa un numero: "))
    for i in range(2,num):
        if i % 2 == 0:
            print(f"{i} es primo")
        else:
            print(f"{i} no es primo")

esPrimo()