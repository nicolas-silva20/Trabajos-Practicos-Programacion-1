import sys
sys.path.append("D:/Facultad/Programacion/TP y Ejercicios en Clase")
import funciones

while True:
    dni_number = input("Ingrese un número de DNI (entre 7 y 8 dígitos): ")

    if funciones.validate_dni(dni_number): #Se invoca a la funcion y se verifica que se haya ingresado un numero de DNI válido
        print(f"El número de DNI {dni_number} es válido.")
    else:
        print(f"El número de DNI {dni_number} no es válido.")
    
    keep_validating = input("¿Desea validar otro número de DNI? (Si/No): ").strip().lower() #Una vez realizada la validación, se pregunta si se desea repetir el proceso
    if keep_validating != "si":
        break