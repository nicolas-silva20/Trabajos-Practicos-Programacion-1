#Se inicializa la variable para almacenar los montos de las compras
total_amount = 0

#Mediante un bucle while se ingresan los montos de compra
while True:
    #Se solicita el ingreso del monto de la compra
    amount = float(input("Ingrese el monto de la compra (o 0 para terminar): "))
    
    #Se verifica si el monto es igual a 0
    if amount == 0:
        break #En tal caso, se rompe el bucle
    
    #Se verifica si el monto es negativo
    if amount < 0:
        print("No se aceptan montos negativos. Ingrese un nuevo monto.")
        continue  #Se salta al inicio del bucle para ingresar un monto válido
    
    #Se suma el monto al total
    total_amount += amount

#Se aplica el descuento del 10% si el total de compras supera $1000
if total_amount > 1000:
    discount = total_amount * 0.10
    total_amount -= discount

#Se imprime el total de compras con el descuento aplicado si fué necesario
print(f"Total de compras: ${total_amount:.2f}")