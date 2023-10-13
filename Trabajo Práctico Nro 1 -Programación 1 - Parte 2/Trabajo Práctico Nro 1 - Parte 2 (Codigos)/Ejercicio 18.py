#Se solicita el ingreso del costo de la cena
costo_cena = float(input("Ingrese el costo de la cena: "))

#Se calcula el servicio (6.2% del costo de la cena)
servicio = costo_cena * 0.062

#Se calcula la propina (10% del costo de la cena)
propina = costo_cena * 0.10

#Se calcula el monto final a pagar
monto_final = costo_cena + servicio + propina

#Se imprime el monto final a pagar
print(f"El monto final a pagar es: ${monto_final:.2f}")#Se emplea el formateo del monto final(float) para que se muestren 2 decimales