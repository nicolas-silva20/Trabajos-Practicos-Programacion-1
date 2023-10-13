#Se inicializa el contador de números pares
even_numbers = 0

#Se inicia el bucle para ingresar números
while True:
    number = int(input("Ingrese un número entero positivo (-1 para salir): "))

    #Se verifica si el usuario ingresa el numero de salida
    if number == -1:
        break

    #Se verifica si el número ingresado es positivo
    if number < 0:
        print("Por favor, ingrese un número entero positivo.")
        continue

    #Se calcula la suma de los dígitos del número ingresado:
    digit_sum = 0 #Se inicia el valor en 0
    temp_number = number #Se almacena el valor del numero en una variable temporal
    while temp_number > 0: #Mientras el valor sea mayor a cero se ejecutan las lineas de calculo para la suma
        digit_sum += temp_number % 10 #Se obtiene el ultimo digito del numero y se lo suma a la variable de suma
        temp_number //= 10 #Se elimina al digito sumado para así seguir con el siguiente digito

    #Se imprime la suma de los dígitos
    print(f"La suma de los dígitos de {number} es {digit_sum}")

    #Se verifica si el número es par
    if number % 2 == 0:
        even_numbers += 1 #De ser así, se incrementa el contador de numeros pares en 1

#Se imprime la cantidad de números pares ingresados
print(f"Se ingresaron {even_numbers} números pares.")