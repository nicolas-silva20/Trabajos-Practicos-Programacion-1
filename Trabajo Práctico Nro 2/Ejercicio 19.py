#Se solicita al usuario la cantidad de lápices a comprar
cantidad_lapices = int(input("Ingresa la cantidad de lápices que deseas comprar: "))

#Se define el costo por lápiz
costo_por_lapiz = 60

#Se calcula el costo sin descuento
costo_sin_descuento = cantidad_lapices * costo_por_lapiz

#Se determina si se aplica descuento
if cantidad_lapices >= 1000:
    descuento = 0.07  #7% de descuento
    costo_con_descuento = costo_sin_descuento - (costo_sin_descuento * descuento)
else:
    costo_con_descuento = costo_sin_descuento

#Se imprime el costo final
print(f"Costo total de {cantidad_lapices} lápices: ${costo_con_descuento:.2f}") #Se formatea el valor del costo para que muestre solo 2 decimales