#Se solicita al usuario que ingrese cuatro notas
nota1 = float(input("Ingrese la primera nota: "))
nota2 = float(input("Ingrese la segunda nota: "))
nota3 = float(input("Ingrese la tercera nota: "))
nota4 = float(input("Ingrese la cuarta nota: "))

#Se calcula el promedio de las notas
promedio = (nota1 + nota2 + nota3 + nota4) / 4

#Se comprueba si el promedio es mayor o igual a 6 para aprobar
if promedio >= 6:
    print("El alumno ha aprobado el curso con un promedio de", promedio)
else:
    print("El alumno ha reprobado el curso con un promedio de", promedio)