#Se solicita al usuario los valores a y b
a = float(input("Ingresa el primer valor (a): "))
b = float(input("Ingresa el segundo valor (b): "))

#Se solicita al usuario la operación que a realizar
print("Opciones de operación:")
print("1. Suma")
print("2. Multiplicación")
print("3. Resta")
print("4. División")
opcion = int(input("Selecciona una opción (1/2/3/4): "))

#Se realiza la operación según la opción seleccionada
if opcion == 1:
    resultado = a + b
    print(f"Resultado de la suma: {resultado}")
elif opcion == 2:
    resultado = a * b
    print(f"Resultado de la multiplicación: {resultado}")
elif opcion == 3:
    resultado = a - b
    print(f"Resultado de la resta: {resultado}")
elif opcion == 4:
    if b == 0:
        print("Error: No se puede dividir por cero.")
    else:
        resultado = a / b
        print(f"Resultado de la división: {resultado}")
else:
    print("Opción no válida. Selecciona una opción válida (1/2/3/4).")