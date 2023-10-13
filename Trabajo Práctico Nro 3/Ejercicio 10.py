#Se solicita el ingreso de un número entero
number = int(input("Ingresa un número entero: "))

#Se incializa la variable is_prime como falsa
is_prime = True

if number <= 1:
    is_prime = False #En caso de que el numero sea menor o igual a 1 el valor de la variable cambia a falso
else:
    for i in range(2, number): #Se recorren los valores comprendidos entre 2 y el numero anterior al ingresado por el usuario
        if number % i == 0: #Se comprueba si el numero ingresado es divisible por 'i'
            is_prime = False #De ser así, la variable is_prime se torna falsa
            break

#Se imprime el resultado
if is_prime:
    print(f"{number} es un número primo.")
else:
    print(f"{number} no es un número primo.")