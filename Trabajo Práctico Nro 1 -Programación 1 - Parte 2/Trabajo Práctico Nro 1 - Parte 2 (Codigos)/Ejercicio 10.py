#Se solicita el ingreso de las calificaciones
parcial1 = float(input("Ingrese la calificación del primer parcial: "))
parcial2 = float(input("Ingrese la calificación del segundo parcial: "))
parcial3 = float(input("Ingrese la calificación del tercer parcial: "))
examen_final = float(input("Ingrese la calificación del examen final: "))
trabajo_final = float(input("Ingrese la calificación del trabajo final: "))

#Se cakcula el promedio de los parciales
promedio_parciales = (parcial1 + parcial2 + parcial3) / 3

#Se calculan los porcentajes de la calificación final
porcentaje_parciales = promedio_parciales * 0.55
porcentaje_examen_final = examen_final * 0.30
porcentaje_trabajo_final = trabajo_final * 0.15

#Se calcula la calificación final
calificacion_final = porcentaje_parciales + porcentaje_examen_final + porcentaje_trabajo_final

#Se imprime la calificación final
print(f"La calificación final es: {calificacion_final}")