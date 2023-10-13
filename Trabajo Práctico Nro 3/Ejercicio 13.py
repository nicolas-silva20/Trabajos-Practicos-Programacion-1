while True: #Se ejecuta el bucle en tanto el usuario ingrese algo distinto de 'salir'
    new_input = input("Ingrese algo (o escriba 'salir' para terminar): ") #Se solicita el ingreso de una cadena o caracter
    if new_input.lower() == "salir": #Se transforma el ingreso a minusculas y se verifica si es igual a 'salir'
        print("Saliendo del programa.") #En tal caso se rompe el bucle y se imprime el mensaje
        break
    print("Eco:", new_input) #Caso contrario se imprime el eco de lo ingresado y se reinicia el bucle