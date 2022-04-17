import random

def generador_pass():
    MAYUS = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'Ñ', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'X', 'Y', 'Z']
    MINUS = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'ñ', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'x', 'y', 'z']
    NUMS = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
    CHARS = ['*', '+', '-', '/', '@', '_', '?', '!', '.', '>', '<', '~', '^', '&', '$', '#']

    password = MAYUS + MINUS + NUMS + CHARS
    psw = []
    for i in range(10):
        cr = random.choice(password)
        psw.append(cr)

    psw = "".join(psw)
    return f"Tu nueva contrasña es {psw}"

print(generador_pass())