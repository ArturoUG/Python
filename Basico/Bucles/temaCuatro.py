import random

num1 = random.randint(0, 100)
print(num1)
num2 = int(input("Adivina el numero: "))
while num2 != num1:
    if num2 > num1:
        print("Ingresa un numero menor")
    else:
        print("Ingresa un numero mayor")
    num2 = int(input("Te equivocaste. Adivina el numero: "))

else:
    print("Adivinaste el numero.")