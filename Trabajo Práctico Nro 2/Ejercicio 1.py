#Se solicita el ingreso del número de años de la computadora
anios_computadora = int(input("Ingrese el número de años que tiene la computadora: "))

#Se comprueba si la computadora es nueva o vieja
if anios_computadora <= 2:
    print("La computadora es nueva.")
else:
    print("La computadora es vieja.")