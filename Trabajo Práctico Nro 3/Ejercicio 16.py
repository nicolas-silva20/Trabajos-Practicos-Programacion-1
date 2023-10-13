#Se solicita el ingreso de la cantidad de números a introducir
number_of_numbers = int(input("¿Cuántos números desea introducir? "))

#Se incializa el contador de números negativos
negative_numbers = 0

#Se itera según la cantidad de números especificada
for i in range(number_of_numbers):
    number = float(input("Introduzca un número: ")) #Se solicita el ingreso de un numero
    if number < 0: #Se verifica si es menor que 0
        negative_numbers += 1 #En tal caso, se incrementa el contador de numeros negativos en 1

#Se imprime la cantidad de números negativos
print(f"Ha introducido {negative_numbers} números negativos.")