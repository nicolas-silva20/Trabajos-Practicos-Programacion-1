#Se solicita el ingreso del nombre de usuario y contraseña
nombre_usuario = input("Ingrese su nombre de usuario: ")
contrasena = input("Ingrese su contraseña: ")

#Se verifica si el nombre de usuario y la contraseña son correctos
if nombre_usuario == "Gwenevere" and contrasena == "excalibur":
    print("Usuario y contraseña correctos. Puede ingresar a Camelot.")
else:
    print("Acceso denegado.")