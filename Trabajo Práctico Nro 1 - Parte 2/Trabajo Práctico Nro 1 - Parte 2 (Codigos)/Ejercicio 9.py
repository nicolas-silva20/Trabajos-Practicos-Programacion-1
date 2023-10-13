# Se solicita el ingreso del monto total de la compra
monto_total = float(input("Ingrese el monto total de la compra: "))

#Se calcula el descuento (15% del monto total)
descuento = monto_total * 0.15

#Se calcula el monto final a pagar (monto total - descuento)
monto_final = monto_total - descuento

#Se imprime el monto final a pagar
print(f"El monto a pagar después del descuento del 15% es: {monto_final}")