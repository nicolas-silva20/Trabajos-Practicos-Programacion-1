#Se solicita el ingreso de los valores de A y B
A = float(input("Ingrese el valor de A: "))
B = float(input("Ingrese el valor de B: "))

#Se intercambian los valores de A y B utilizando una variable temporal
temp = A
A = B
B = temp

#Se imprimen los valores de A y B después del intercambio
print(f"Después del intercambio, el valor de A es: {A}")
print(f"Después del intercambio, el valor de B es: {B}")