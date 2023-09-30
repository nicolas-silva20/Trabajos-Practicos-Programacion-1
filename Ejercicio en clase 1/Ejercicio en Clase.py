#Se solicita el ingreso de la fecha en un formato determinado
fecha = input("Ingrese la fecha actual (dia, DD/MM): ")
#Se extrae del string el dia de la semana, dia del mes y mes del año 
dia_semana = fecha [0 : fecha.find(",")]
dia = int(fecha [fecha.find(" ") + 1 : fecha.find("/")])
mes = int(fecha[fecha.find("/") + 1 : ])

#Se convierte el dia de la semana a minúsculas
dia_semana = dia_semana.lower()

#Se crea un arreglo
dias = ["lunes", "martes", "miercoles", "jueves", "viernes"]

#Se comprueba que la fecha ingresada es valida
if (dia_semana not in dias or dia > 31 or mes > 12):
    print("El programa se interrumpio debido a un error")

#Se establecen acciones correspondientes para cada dia de la semana
if (dia_semana == "lunes" or dia_semana == "martes" or dia_semana == "miercoles" ):
    examen = input("¿Hoy hubo examenes? si/no: ")
    if (examen == "si"):
        alumnos_aprobados = int(input("Ingrese el numero de alumnos aprobados: "))
        alumnos_desaprobados = int(input("Ingrese el numero de alumnos desaprobados: "))
        alumnos_total = alumnos_aprobados + alumnos_desaprobados
        porcenaje = alumnos_aprobados * 100 / alumnos_total
        print(f"El prorcentaje de alumnos aprobados es de {porcenaje}% ")
elif (dia_semana == "jueves"):
    alumnos_presentes = int(input("Ingrese el procentaje de alumnos presentes: "))
    if (alumnos_presentes >= 50):
        print("Asisitió la mayoría")
    else:
        print("No asistió la mayoría")
elif (dia_semana == "viernes" and dia == 1 and mes == 1 or mes == 7):
    print("Comienzo de nuevo ciclo")
    nuevos_ingresantes = int(input("Ingrese el numero de nuevos ingresantes: "))
    arancel = int(input("Ingrese el arancel en $ por alumno: "))
    ingreso_total = nuevos_ingresantes * arancel
    print(f"El inreso total es ${ingreso_total}")
            