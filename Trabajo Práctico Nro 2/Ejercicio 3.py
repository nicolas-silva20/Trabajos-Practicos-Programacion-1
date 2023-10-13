# Se solicita el ingreso del primer nombre
nombre1 = input("Ingrese el primer nombre: ")

#Se solicita el ingreso del segundo nombre
nombre2 = input("Ingrese el segundo nombre: ")

#Se obitiene la primer letra de cada nombre
primera_letra1 = nombre1[0].lower()  #Se convierten a minúsculas para hacer la comparación sin distinción de mayúsculas/minúsculas
primera_letra2 = nombre2[0].lower()

#Se comparan las primeras letras y se imprime el resultado
if primera_letra1 == primera_letra2:
    print("Coincidencia")
else:
    print("No hay coincidencia")