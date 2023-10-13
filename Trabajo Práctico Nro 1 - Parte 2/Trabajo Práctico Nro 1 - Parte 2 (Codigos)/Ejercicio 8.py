#Se solicitan el ingreso del sueldo base
sueldo_base = float(input("Ingrese su sueldo base: "))

#Se solicita el ingreso del monto de las tres ventas
venta1 = float(input("Ingrese el monto de la primera venta: "))
venta2 = float(input("Ingrese el monto de la segunda venta: "))
venta3 = float(input("Ingrese el monto de la tercera venta: "))

#Se calcula el monto total de comisiones (10% de la suma de las ventas)
comisiones = (venta1 + venta2 + venta3) * 0.10

#Se caclula el salario total
salario_total = sueldo_base + comisiones

#Se imprimen los resultados
print(f"El monto total de comisiones es: {comisiones}")
print(f"El salario total en el mes es: {salario_total}")