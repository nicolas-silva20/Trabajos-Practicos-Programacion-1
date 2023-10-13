import math

#Se solicita el ingreso de un número
numero = float(input("Ingrese un número: "))

#Se calcula la raíz cuadrada
raiz_cuadrada = math.sqrt(numero)

#Se calcula la raíz cúbica
raiz_cubica = numero ** (1/3)

#Se imprimen los resultados
print(f"La raíz cuadrada de {numero} es: {raiz_cuadrada}")
print(f"La raíz cúbica de {numero} es: {raiz_cubica}")