#Se solicita el ingresode horas trabajadas en el mes y el salario por hora
horas_trabajadas = float(input("Ingresa el total de horas trabajadas en el mes: "))
salario_por_hora = float(input("Ingresa el salario por hora: "))

#Se define la jornada laboral mínima (en horas)
jornada_minima = 48

#Se calcula si hay horas extras y cuántas son en case de haberlas
if horas_trabajadas > jornada_minima:
    horas_extras = horas_trabajadas - jornada_minima
else:
    horas_extras = 0

#Se calcula el salario total
salario_total = (jornada_minima * salario_por_hora) + (horas_extras * salario_por_hora * 1.1)

#Se imprimen tanto las horas extras trabajadas como el salario total
print(f"Horas extras trabajadas: {horas_extras} horas")
print(f"Salario total: ${salario_total:.2f}")