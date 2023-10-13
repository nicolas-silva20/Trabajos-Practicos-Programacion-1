#Se solicita el ingreso de una frase y una letra
phrase = input("Ingresa una frase: ")

letter = input("Ingresa una letra: ")

#Se inicializa una variable para contar las ocurrencias de la letra
counter = 0

#Se recorre cada carácter en la frase y se aumenta en 1 el contador por cada vez que se encuentra la letra durante el recorrido
for character in phrase:
    if character == letter:
        counter += 1

#Se imprime el número de veces que aparece la letra
print(f'La letra "{letter}" aparece {counter} veces en la frase.')