#Se solicita el ingreso de un número entero.
n = int(input("Ingresa un número: "))

#Mediante un bucle 'for' se generan las filas del triángulo.
#Se inicia con 1 e incrementa de 2 en 2 para obtener números impares.
for i in range(1, n + 1, 2):
    #Con el segundo bucle 'for' se imprimen los números en orden descendente.
    for j in range(i, 0, -2):
        #Se imprime el número sin salto de línea.
        print(j, end="")
    #Se imprime un salto de línea para pasar a la siguiente fila.
    print()