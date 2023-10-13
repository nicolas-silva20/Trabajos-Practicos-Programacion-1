#Se inicializa la variable para la sumatoria
summation = 0

#Se inicializa el bucle para ingresar números
while True:
    number = int(input("Ingrese un número entero ( o '0' para salir): "))
    
    #Se verifica si el número es 0
    if number == 0:
        break #En tal caso, se sale del bucle
    
    #Caso contrario, el bucle continua y se añade el número a la sumatoria
    summation += number

#Se imprime la sumatoria de los números ingresados
print(f"La sumatoria de los números ingresados es: {summation}")