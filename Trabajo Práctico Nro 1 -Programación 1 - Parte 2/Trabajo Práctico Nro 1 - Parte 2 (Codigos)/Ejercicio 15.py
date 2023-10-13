#Se solicita el ingreso de la hora de salida en formato HH:MM:SS
HH = int(input("Ingrese la hora de salida (HH): "))
MM = int(input("Ingrese los minutos de salida (MM): "))
SS = int(input("Ingrese los segundos de salida (SS): "))

#Se solicita el ingreso del tiempo de viaje en segundos
T = int(input("Ingrese el tiempo de viaje en segundos (T): "))

#Se calcula la hora de llegada sumando el tiempo de viaje
total_segundos_salida = HH * 3600 + MM * 60 + SS
total_segundos_llegada = total_segundos_salida + T

#Se calcula la hora, minutos y segundos de llegada
HH_llegada = total_segundos_llegada // 3600
MM_llegada = (total_segundos_llegada % 3600) // 60
SS_llegada = total_segundos_llegada % 60

#Se ajusta la hora de llegada si supera las 24 horas
if HH_llegada >= 24:
    HH_llegada -= 24

#Se imprime la hora de llegada
print(f"La hora de llegada a la ciudad B es: {HH_llegada:02d}:{MM_llegada:02d}:{SS_llegada:02d}") #Se emplea "":02d" como formateo de cadena para dar formato al valor