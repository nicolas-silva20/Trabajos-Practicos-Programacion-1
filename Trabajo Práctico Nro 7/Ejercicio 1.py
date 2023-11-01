import sys
sys.path.append("D:/Facultad/Programacion/TP y Ejercicios en Clase/Funciones")
import funciones

numbers = []

while True:
    entrance = input("Ingrese un número ('fin' para terminar): ")
    if entrance.lower() == 'fin':
        break
    numero = int(entrance)
    numbers.append(numero)

if numbers:
    print("Lista de números original:", numbers)
    funciones.numbers_in_order_bubble(numbers)
    print("Lista ordenada:", numbers)
else:
    print("No se ingresaron números.")