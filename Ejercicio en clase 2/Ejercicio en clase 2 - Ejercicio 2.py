# Se incializan los contadores de numeros pares e impares
nros_pares_totales = 0
nros_impares_totales = 0

while True: # Con el bucle while True se asegura la ejecución de forma indefinida hasta la ejecución de la instrucción break, dada cuando el usuario ingrese 0
    numero = int(input("Ingrese un número entero positivo (o 0 para salir): ")) # Se solicita el ingreso de un numero

    if numero == 0:
        break  # Se rompe el bucle en cuanto se lea el ingreso del numero 0

    # Se inicializan los contadores de dígitos pares e impares en el número actual
    pares = 0
    impares = 0

    # Se calculan los dígitos pares e impares del número actual
    while numero > 0:
        digito = numero % 10 # Mediante esta operación se obtiene el último dígito del número
        if digito % 2 == 0: #Se determina si el numero es par
            pares += 1 # En caso de serlo se añade al contador de numeros pares
        else:
            impares += 1 # Si no lo es, se añade al de numeros impares
        numero //= 10 # Mediante esta operación se elimina el ultimo digito, así se puede trabajar con el siguiente

    # Se imprimen los resultados del número actual
    print(f"Dígitos pares en el número: {pares}")
    print(f"Dígitos impares en el número: {impares}")

    # Se modifica los contadores totales segun corresponda
    nros_pares_totales += pares
    nros_impares_totales += impares

# Se imprimen los resultados del conteo total de pares e impares
print(f"Total de dígitos pares contados: {nros_pares_totales}")
print(f"Total de dígitos impares contados: {nros_impares_totales}")