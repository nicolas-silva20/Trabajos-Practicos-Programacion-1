#Se solciita el ingreso de dos numeros
number1 = int(input("Ingresa el primer número entero: "))
number2 = int(input("Ingresa el segundo número entero: "))

#Se determina el número más pequeño y más grande mediante las funciones min() y max()
initial_number = min(number1, number2)
final_number = max(number1, number2)

#Se recorren los números entre el número inicial y final
print("Números pares entre", initial_number, "y", final_number, ":")
for number in range(initial_number, final_number + 1):
    if number % 2 == 0: #Si el numero es par se imprime y se coloca un espacio para colocar el siguiente en la misma linea
        print(number, end=" ")

print("\nNúmeros impares entre", initial_number, "y", final_number, ":")
for number in range(initial_number, final_number + 1):
    if number % 2 != 0: #Si el numero es impar se imprime y se coloca un espacio para colocar el siguiente en la misma linea
        print(number, end=" ")