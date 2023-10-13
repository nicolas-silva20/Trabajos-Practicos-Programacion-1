#Se solicita el ingreso de una letra
letra = input("Ingrese una letra: ")

#Se valida si la entrada tiene un solo carácter
if len(letra) == 1:
    #Se convierte la letra ingresada a minúscula para hacer la comparación sin distinción de mayúsculas/minúsculas
    letra = letra.lower()

    #Se verifica si la letra es una vocal
    if letra in ['a', 'e', 'i', 'o', 'u']:
        print("Es vocal.")
    else:
        print("No es vocal.")
else:
    print("No se puede procesar el dato: Ingrese solo un carácter.")