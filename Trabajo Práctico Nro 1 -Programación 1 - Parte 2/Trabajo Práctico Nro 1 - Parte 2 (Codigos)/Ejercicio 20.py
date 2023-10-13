#Se solicita al usuario ingresar la fecha de nacimiento en formato DDMMAAAA
fecha_nacimiento = input("Ingrese la fecha de nacimiento en formato DDMMAAAA: ")

#Se extraen el día, mes y año de la fecha ingresada
dia = int(fecha_nacimiento[0:2])
mes = int(fecha_nacimiento[2:4])
anio = int(fecha_nacimiento[4:])

#Se imprime la fecha en formato dd/mm/aaaa
fecha_formato = f"{dia:02d}/{mes:02d}/{anio:04d}"
print(f"Fecha de nacimiento: {fecha_formato}")