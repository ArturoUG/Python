def numMayor(arreglo):
    
    # Supongamos que el mayor es el primero solo para tener un valor para inicializar
    mayor =  arreglo[0]    
    # Recorrer y buscar
    for elemento in arreglo:
        if elemento > mayor:
            mayor = elemento
    return mayor

def numMenor(arreglo):
    menor = arreglo[0]
    for elemento in arreglo:
        if elemento < menor:
            menor = elemento
    return menor

arreglo = [1,2,3,5,4]
mayor = numMayor(arreglo)
menor = numMenor(arreglo)


print(f"El num mayor es: {mayor}") 
print(f"El num menor es: {menor}")