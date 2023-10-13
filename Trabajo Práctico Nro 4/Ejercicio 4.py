#Se ingresan los años que marcarán el periodo a contar
start_year = int(input("Ingresa el año inicial: "))
end_year = int(input("Ingresa el año final: "))

print("Los años bisiestos y múltiplos de 10 en el intervalo de ambos años son los siguientes:")
for year in range(start_year, end_year + 1):
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0): #Se determina si el año es bisiesto y múltiplo de 10
        if year % 10 == 0:
            print(year)