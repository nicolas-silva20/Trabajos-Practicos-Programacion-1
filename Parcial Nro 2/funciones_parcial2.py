#Parcial N°2

#Verificación si es mutante o no
def is_mutant(dna):
    num_rows = len(dna)
    num_cols = len(dna[0])

    for i in range(num_rows):
        for j in range(num_cols):
            current_char = dna[i][j]
            #Se verifica horizontalmente
            if j + 3 < num_cols and all(current_char == dna[i][j + k] for k in range(1, 4)):
                return True
            #Se verifica verticalmente
            if i + 3 < num_rows and all(current_char == dna[i + k][j] for k in range(1, 4)):
                return True
            if i + 3 < num_rows and j + 3 < num_cols:
                #Se verifica de forma diagonal hacia la derecha y abajo
                if all(current_char == dna[i + k][j + k] for k in range(1, 4)):
                    return True
            if i + 3 < num_rows and j - 3 >= 0:
                #Se verifica de forma diagonal hacia la izquierda y abajo
                if all(current_char == dna[i + k][j - k] for k in range(1, 4)):
                    return True
    return False

#Impresión de la secuencia de ADN(matriz)
def print_dna_sequence(dna):
    for row in dna:
        print(row)