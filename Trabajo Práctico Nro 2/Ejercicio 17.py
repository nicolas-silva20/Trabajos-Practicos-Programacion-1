#Se solicita el ingreso de un dia de la semana
dia_semana = input("Ingresa un día de la semana: ")

#Se comprueba qué día fue ingresado y se imprime el mensaje correspondiente
if dia_semana.lower() == "lunes":
    print("Es lunes. Suerte, va a hacer falta.")
elif dia_semana.lower() == "viernes":
    print("Es viernes. A disfrutar")
elif dia_semana.lower() == "sábado" or dia_semana.lower() == "domingo":
    print("Es fin de semana. A descansar.")
else:
    print("No es lunes, viernes ni fin de semana. Toca sufrir.")