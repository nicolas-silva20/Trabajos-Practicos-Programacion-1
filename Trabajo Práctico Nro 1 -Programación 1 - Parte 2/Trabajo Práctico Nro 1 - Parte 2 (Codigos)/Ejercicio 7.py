#Se solicita el ingreso de la cantidad de minutos
minutos = int(input("Ingrese la cantidad de minutos: "))

#Se calculan las horas y minutos
horas = minutos // 60  # División entera para obtener las horas
minutos_restantes = minutos % 60  # Módulo para obtener los minutos restantes

#Se imprimen los resultados
print(f"{minutos} minutos son {horas} horas y {minutos_restantes} minutos.")