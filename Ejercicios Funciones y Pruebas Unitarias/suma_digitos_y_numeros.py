import sys
sys.path.append("D:/Facultad/Programacion/TP y Ejercicios en Clase/Funciones")
import funciones


digits_total_add = 0
numbers_total_add = 0

while True:
    number = int((input("Ingrese el numero a procesar ('0' para terminar):")))
    
    if number == 0:
        break

    digit_add_number = funciones.add_digits(number)
    digits_total_add += digit_add_number
    numbers_total_add += number
    
    print(f"La suma de los digitos de {number} es {digit_add_number}")
    print(f"La suma total de los digitos de todos los numeros ingresados es {digits_total_add}")
    print(f"La suma de los numeros ingresados hasta el momento es {numbers_total_add}")