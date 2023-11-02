import sys
sys.path.append("D:/Facultad/Programacion/TP y Ejercicios en Clase/Parcial Nro 2")
import funciones_parcial2

dna = []

#Se solicita al usuario ingresar las 6 filas de ADN
for i in range(6):
    while True:
        row = input(f"Ingrese la fila {i + 1} de ADN (6 letras de A, C, G o T): ")
        if len(row) == 6 and all(nitrogenous_base in "ACGT" for nitrogenous_base in row):
            break
        else:
            print("Entrada inválida. Debe contener exactamente 6 letras de A, C, G o T.")
    dna.append(row)

is_mutant_result = funciones_parcial2.is_mutant(dna)
#Se imprime el resultado de la verificación
print(f"Es un mutante: {is_mutant_result}")

#Se imprime la matriz de ADN
print("Matriz de ADN:")
funciones_parcial2.print_dna_sequence(dna)