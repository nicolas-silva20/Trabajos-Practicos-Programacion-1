#Se solicita al usuario un número entero para la altura del triángulo
height = int(input("Ingrese un número entero para la altura del triángulo: "))

#Se itera desde 1 hasta la altura ingresada
for i in range(1, height + 1):
    #Se imprime una fila con i asteriscos (*)
    print('*' * i)