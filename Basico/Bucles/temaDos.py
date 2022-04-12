contador = 0

for contador in range(1001):
    print(contador)

for i in range(10):
    print(11 * i)

nombre = input("Escri be tu nombre: ")

for letra in nombre:
    print(letra)

frase = input("Ingresa una frase: ")

for letra in frase:
    if letra == "o":
        break
    print(letra)