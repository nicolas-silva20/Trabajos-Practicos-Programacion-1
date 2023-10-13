#Se solicita el ingreso del nombre y los dos apellidos
nombre_completo = input("Ingrese su nombre y dos apellidos: ")

#Se separan el nombre y los apellidos y se almacenan en una lista llamada "palabras"
palabras = nombre_completo.split()

#Se obtienen las iniciales extrayendo el primer caracter de cada elemento de la lista y se los convierte en mayúscula
inicial_nombre = palabras[0][0].upper()
inicial_apellido1 = palabras[1][0].upper()
inicial_apellido2 = palabras[2][0].upper()

#Se imprimen las iniciales
print(f"Las iniciales son: {inicial_nombre}{inicial_apellido1}{inicial_apellido2}")