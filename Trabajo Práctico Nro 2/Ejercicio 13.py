#Se solicita el ingreso de dos números enteros
num1 = int(input("Ingrese el primer número entero: "))
num2 = int(input("Ingrese el segundo número entero: "))

#Se verifica si los números son negativos o nulos
if num1 <= 0 or num2 <= 0:
    print("Ingrese números enteros positivos.")
else:
    #Se determina el número mayor y el menor
    mayor = max(num1, num2)
    menor = min(num1, num2)

    #Se verifica si el número mayor es múltiplo del menor
    if mayor % menor == 0:
        print(f"{mayor} es múltiplo de {menor}.")
    else:
        print(f"{mayor} no es múltiplo de {menor}.")