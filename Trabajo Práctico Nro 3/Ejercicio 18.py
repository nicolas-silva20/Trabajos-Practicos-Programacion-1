#Se inicializan los primeros dos números de la secuencia
a, b = 0, 1

#Se imrpime el primer número (0) antes del bucle
print(a)

#Meidante un bucle se calculan e imprimen los siguientes números
for _ in range(9):  #Se repetirá el proceso solo 9 veces, pues ya se imprimió el primer 0
    a, b = b, a + b  #Se calcula el siguiente número
    print(a)  #Se imrpime el número actual