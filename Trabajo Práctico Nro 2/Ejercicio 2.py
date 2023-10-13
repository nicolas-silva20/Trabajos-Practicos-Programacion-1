#Se solicita el ingreso del número de años de la computadora
anios_computadora = int(input("Ingrese el número de años que tiene la computadora: "))

#Se verifica si el número de años es negativo y mostrar un mensaje de error si es así
if anios_computadora < 0:
    print("Error: El número de años no puede ser negativo.")
else:
    # Comprobar si la computadora es nueva o vieja
    if anios_computadora <= 2:
        print("La computadora es nueva.")
    else:
        print("La computadora es vieja.")