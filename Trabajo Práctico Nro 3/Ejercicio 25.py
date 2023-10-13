#Se solicita el ingreso de un numero positivo
number = int(input("Ingrese un número entero positivo: "))

#Se verifica si el número es negativo
if number < 0:
    print("El factorial no está definido para números negativos.")
elif number == 0:
    print("El factorial de 0 es 1.")
else: #En caso de no ser '0' o un numero menor a '0', se calcula el factorial
    factorial = 1
    for i in range(1, number + 1): #Se recorren los numeros comprendidos entre 1 y el numero ingresado
        factorial *= i #Se multiplica el valor de 'factorial' por el de 'i' y se guarda el resultado en la variable 'factorial' para ser multiplicada por el siguiente numero entero

    #Se imprime el factorial del numero ingresado
    print(f"El factorial de {number} es {factorial}.")