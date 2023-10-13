#Se solicita al usuario que ingrese su nombre
nombre = input("Ingrese su nombre: ")

#Se solicita al usuario que ingrese su sexo (M para mujer, H para hombre)
sexo = input("Ingrese su sexo (M para mujer, H para hombre): ")

#Se covierte el nombre a mayúsculas para comparación
nombre = nombre.upper()

#Se determina el grupo al que pertenece
if (sexo == "M" and nombre < "M") or (sexo == "H" and nombre > "N"):
    grupo = "A"
else:
    grupo = "B"

#Se imprime el grupo al que pertenece
print(f"Usted pertenece al grupo {grupo}.")