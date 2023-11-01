import sys
sys.path.append("D:/Facultad/Programacion/TP y Ejercicios en Clase/Funciones")
import funciones


first_number = int(input("Ingrese el primer número entero: "))
second_number = int(input("Ingrese el segundo número entero: "))

if funciones.is_multiple(first_number, second_number) or funciones.is_multiple(second_number, first_number):
    print(f"¡Uno de los números es múltiplo del otro!")
else:
    print("Ninguno de los números es múltiplo del otro.")