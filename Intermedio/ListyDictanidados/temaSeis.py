
#* Manejo de excepciones

def divisors2(num):
    divisors = []
    for i in range(1, num + 1):
        if num % i == 0:
            divisors.append(i)
    return divisors


def run2():
    try: 
        num = int(input('Ingresa un número: '))
        print(divisors2(num))
        print("Terminó mi programa")
    except ValueError: 
        print("Debes ingresar un número")

#challenge
def divisors(num):
    divisors = []
    for i in range(1, num + 1):
        if num% i == 0:
            divisors.append(i)
    return divisors


def run():
    while True:
        try:
            num = int(input('Ingresa un número: '))
            if num < 0:
                raise ValueError
            print(divisors(num))
            print("Terminó mi programa")
            break
        except ValueError:
            print("Debes ingresar un entero positivo")




if __name__ == '__main__':
    run2()