#Se inicializa la variable para almacenar los montos de las compras
total_amount = 0

#Mediante un bucle while se ingresan los montos de compra
while True:
    #Se solicita el ingreso del monto de la compra
    amount = float(input("Ingrese el monto de la compra (o 0 para terminar): "))

    #Se verifica si el monto es igual a 0
    if amount == 0:
        break #En tal caso, se rompe el bucle

    #Se suma el monto al total
    total_amount += amount

#Se imprime el total de compras realizado por el cliente
print(f"El total de compras del cliente es: {total_amount}")