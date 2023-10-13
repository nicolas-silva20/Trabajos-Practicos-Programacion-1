#Se solicita el ingreso de la cantidad objetivo a ahorrar
objective = float(input("Ingrese la cantidad objetivo que desea ahorrar: "))

#Se inicializa el total ahorrado en cero
total_saved = 0

#Mediante un bucle se ingresas las cantidades a ahorrar en tanto no se haya alcanzado el objetivo
while total_saved < objective:
    #Se solicita la cantidad a ingresar y verifica si es un número positivo
    amount_to_enter = float(input("Ingrese la cantidad que desea ingresar: "))
    if amount_to_enter <= 0:
        print("La cantidad debe ser un número positivo. Intente nuevamente.")
        continue

    #Se agrega la cantidad ingresada al total ahorrado
    total_saved += amount_to_enter

#Se imprime un mensaje cuando se alcanza o supera el objetivo
print(f"¡Felicidades! Has alcanzado tu objetivo de ahorro de ${objective}.")