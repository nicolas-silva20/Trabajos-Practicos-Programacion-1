# Se solicita el mensaje y el corrimiento a emplear
mensaje = input("Ingrese el mensaje a encriptar: ")
corrimiento = int(input("Ingrese el corrimiento (número de lugares a mover las letras): "))

mensaje_encriptado = ""
abecedario = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"  # Se crea una cadena con las letras del abecedario para realizar el encriptamiento

for letra in mensaje:
    if letra.isalpha():  # Se verifica si el caracter en cuestion es una letra
        mayuscula = letra.isupper()  # Se comprueba si la letra está en mayusculas
        letra = letra.upper()  # Se convierte la letra a mayuscula para poder reasignar las letras
        indice = abecedario.index(letra) # Se determina el indice en el abecedario de la letra en cuestión
        nuevo_indice = (indice + corrimiento) % 26 # Se determina el nuevo indice, con el modulo %26 se asegura que al llegar al final del alfabeto se vuelva al principio de éste
        nueva_letra = abecedario[nuevo_indice] # Se asigna el nuevo indice
        if not mayuscula:  # Se mantiene la letra en minúscula en caso de que la letra original así haya estado
            nueva_letra = nueva_letra.lower()
        mensaje_encriptado += nueva_letra
    else:
        mensaje_encriptado += letra  # En caso de no ser una letra, el caracter es añadido al mensaje encriptado directamente

# Imprimir el mensaje encriptado
print(f"Mensaje encriptado: {mensaje_encriptado}")