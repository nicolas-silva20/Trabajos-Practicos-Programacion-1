#Se solicita al usuario ingresar el día, mes y año de nacimiento
dia = int(input("Ingrese el día de nacimiento: "))
mes = int(input("Ingrese el mes de nacimiento: "))
anio = int(input("Ingrese el año de nacimiento: "))

#Se imprime la fecha en formato dd/mm/aaaa
fecha_nacimiento = f"{dia:02d}/{mes:02d}/{anio:04d}" #Se aplica el formateo para que se impriman 2 digitos en dia y mes y 4 digitos en año
print(f"Fecha de nacimiento: {fecha_nacimiento}")