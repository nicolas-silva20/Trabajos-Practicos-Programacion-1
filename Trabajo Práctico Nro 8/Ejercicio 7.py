import sys
sys.path.append("D:/Facultad/Programacion/TP y Ejercicios en Clase/Funciones")
import funciones

#Se solicita al usuario el ingreso de los valores de n y p.
n = int(input("Ingrese el valor de n: "))
p = int(input("Ingrese el valor de p: "))

#Se calcula la sumatoria usando la función recursiva.
result = funciones.calculate_summation(n, p)

#Se imprime el resultado.
print(f"K({n}, {p}) = {result}")