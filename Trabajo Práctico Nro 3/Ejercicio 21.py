#Se inicializa la variable para almacenar el mayor número
largest_number = 0

#Se inicia el bucle para ingresar números
while True:
    number = int(input("Ingrese un número entero positivo ( o '0' para salir): "))
    
    #Se verifica si el número es 0
    if number == 0:
        break #En tal caso, se sale del bucle
    
    #Caso contrario, se verifica si el número ingresado es mayor que el mayor número actual
    if number > largest_number:
        largest_number = number #De ser así, el valor es asignado como 'mayor'

#Se imprime el mayor número ingresado
print(f"El mayor número ingresado fue: {largest_number}")