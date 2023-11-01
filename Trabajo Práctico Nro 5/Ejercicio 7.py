import sys
sys.path.append("D:/Facultad/Programacion/TP y Ejercicios en Clase/Funciones")
import funciones

#Se inicializa la lista de numeros
numbers = []

while True:
    entrance = input("Ingrese un número (o 'fin' para terminar): ") #Se solicita el ingreso de numeros hasta que el usuario ingrese 'fin'
    if entrance.lower() == 'fin':
        break
    numbers.append(entrance)

maximum, minimum = funciones.find_max_min(numbers)

if maximum is not None and minimum is not None:
    print(f"Valor máximo: {maximum}")
    print(f"Valor mínimo: {minimum}")
else:
    print("No se ingresaron números válidos.")