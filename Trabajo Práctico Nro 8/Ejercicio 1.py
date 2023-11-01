import sys
sys.path.append("D:/Facultad/Programacion/TP y Ejercicios en Clase/Funciones")
import funciones

number = int(input("Ingrese un número positivo: ")) #Se solicita el ingreso de un numero entero
number_of_digits = funciones.count_digits(number) #Se invoca a la función
print(f"El número {number} tiene {number_of_digits} dígitos.") #Se imprime el resultado