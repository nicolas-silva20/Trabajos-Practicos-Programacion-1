#Se solicita el ingreso de un número de dos cifras
numero = int(input("Ingrese un número de dos cifras: "))

#Se separan las cifras del numero y se asignan a 2 variables distintas
cifra1 = numero // 10
cifra2 = numero % 10

#Se invierten las dos cifras y se forma el numero buscado
numero_invertido = cifra2 * 10 + cifra1

#Se imprime el número invertido
print(f"El número invertido es: {numero_invertido}")