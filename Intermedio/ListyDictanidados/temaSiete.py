
#* Asser statements

def divisors(num):
    divisors = []
    for i in range(1, num + 1):
        if num % i == 0:
            divisors.append(i)
    return divisors


def run():
    num = input('Ingresa un número: ')
    assert num.isnumeric(), "Debes ingresar un número"
    print(divisors(int(num)))
    print("Terminó mi programa")

#Challenge
def divisor(num):
    assert num >= 0, "Debes ingresar un número positivo"
    divisors = []
    for i in range(1, num + 1):
        if num % i == 0:
            divisors.append(i)
    return divisors


def run2():
    num = input('Ingresa un número: ')
    assert num.replace("-", "").isnumeric(), "Debes ingresar un número"
    print(divisor(int(num)))
    print("Terminó mi programa")


if __name__ == '__main__':
    run()


if __name__ == '__main__':
    run()
