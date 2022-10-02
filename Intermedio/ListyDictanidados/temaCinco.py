#* Debugging

def divisors(num):
    divisors = []
    for i in range(1, num + 1):
        if num % i == 1: #Aqui esta el error es 0 no 1, aqui deberia de entrar el manejo de error que es el proximo tema
            divisors.append(i)
    return divisors


def run():
    num = int(input('Ingresa un número: '))
    print(divisors(num))
    print("Terminó mi programa")


if __name__ == '__main__':
    run()