#Se solciita el ingreso de un número entero mayor que cero
number = int(input("Ingrese un número entero mayor que cero: "))

#Se valida si el número es mayor que cero
if number <= 0:
    print("El número debe ser mayor que cero.")
else:
    print(f"Divisores de {number}:")

    #Se itera desde 1 hasta el número (inclusive)
    for i in range(1, number + 1):
        if number % i == 0: #En caso de que el numero sea divisible por 'i' se imprime éste último
            print(i)