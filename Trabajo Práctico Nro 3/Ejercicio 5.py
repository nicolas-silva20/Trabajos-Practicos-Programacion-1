#Se solicita al usuario la cantidad a invertir, el interés anual y el número de años
amount_to_invest = float(input("Ingrese la cantidad a invertir ($): "))
annual_interest_rate = float(input("Ingrese la tasa de interés anual (%): "))
number_of_years = int(input("Ingrese el número de años: "))

#Se convierte la tasa de interés de porcentaje a decimal
decimal_interest_rate = annual_interest_rate / 100

#Se calcula el capital obtenido cada año
for year in range(1, number_of_years + 1): #Se ejecuta el ciclo tantas veces como la cantidad de años introducida
    capital = amount_to_invest * (1 + decimal_interest_rate) #Se calcula el monto obtenido en el año
    print(f"Año {year}: Capital obtenido = ${capital:.2f}") #Se imprime el monto final en el año
    amount_to_invest = capital  #Se actualiza la cantidad invertida para el próximo año