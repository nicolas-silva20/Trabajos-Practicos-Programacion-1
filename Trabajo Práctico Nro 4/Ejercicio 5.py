#Se realiza el conteo de numeros entre 1 y 20
for num in range(1, 21):
    if num % 2 != 0:  #Se saltean los números impares
        continue
    print(num) #Se imprimen los pares
