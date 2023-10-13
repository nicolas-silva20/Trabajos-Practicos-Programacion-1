#Se almacena la contraseña
correct_password = "contraseña123"

#Se solicita al usuario que ingrese la contraseña
while True:
    entered_password = input("Ingresa la contraseña: ")
    
    #Se comprueba si la contraseña ingresada es correcta
    if entered_password == correct_password:
        print("Contraseña correcta")
        break  #Se sale del bucle cuando la contraseña es correcta
    else:
        print("Contraseña incorrecta")