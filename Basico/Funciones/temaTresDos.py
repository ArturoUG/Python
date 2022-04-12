def esPalindromo():
    palabra = input("Escribe una palabra: ")
    palabra = palabra.strip().lower()
    if(palabra == palabra[::-1]):
        print(f"La palabra {palabra} es un palindromo.")
    else:
        print(f"La palabraa {palabra} no es un paliindromo.")

esPalindromo()