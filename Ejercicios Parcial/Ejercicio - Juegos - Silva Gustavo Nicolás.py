# Se solicita al usuario el ingreso su nombre y se lo almacena en la variable user_name.
user_name = input("Por favor, ingrese su nombre: ")

#Se la bienvenida al usuario utilizando su nombre.
print(f"\nBienvenido, {user_name}")

#Se inicia un bucle while que se ejecutará continuamente hasta que el usuario elija la opción "0" para salir.
while True:
    #Se muestra el menú de opciones al usuario.
    print("\nMenú de opciones:")
    print("1. Juego de números")
    print("2. Juego de palabras")
    print("0. Salir")

    #Se solicita al usuario la elección de una opción y se la almacena en la variable option.
    option = input("Elija una opción (1/2/0): ")

    #Si el usuario elige la opción "1" (Juego de números):
    if option == "1":
        numbers = []  #Se inicializa una lista para almacenar números.

        #Se solicita al usuario el ingreso de números enteros hasta que ingrese "0" para finalizar.
        number = input("Ingrese un número entero (0 para terminar): ")
        while number != "0":
            if number.isdigit():
                number = int(number)
                numbers.append(number)
            else:
                print("El número ingresado debe ser entero. Intente nuevamente")
            number = input("Ingrese un número entero (0 para terminar): ")

        #Se verifica si se ingresaron números.
        if not numbers:
            print("No ha ingresado ningún número.")
        else: #Caso contrario:
            even_numbers = []  #Se inicializa una lista para números pares.
            odd_numbers = []   #Se inicializa una lista para números impares.
            largest_even_number = None  #Variable para el mayor número par.
            sum_odd_numbers = 0         #Variable para la suma de números impares.
            count_odd_numbers = 0       #Variable para el conteo de números impares.

            #Se recorre la lista de números para realizar los cálculos.
            for num in numbers:
                if num % 2 == 0: #Se verifica que el número sea par
                    if largest_even_number is None or num > largest_even_number:    #Se verifica que la variable largest_even_number esté vacía en primer instancia para la primer ejecución 
                                                                                    #y se evalúa si el numero actual es mayor que el corriente mayor número par
                        largest_even_number = num #Si el numero actual es el mayor número par encontrado hasta el momento, se actualiza
                else: #En caso de no ser par:
                    odd_numbers.append(num) #Se añade el número a la lista de números impares
                    sum_odd_numbers += num #Se suma el número a la sumatoria de números impares
                    count_odd_numbers += 1 #Se actualiza el conteo de número s impares

            #Se verifican los resultados y se los imprime.
            if largest_even_number is None:
                largest_even_number = "No hay números pares."
            if count_odd_numbers == 0:
                average_odd_numbers = "No hay números impares."
            else:
                average_odd_numbers = sum_odd_numbers / count_odd_numbers

            print(f"El mayor número par es: {largest_even_number}")
            print(f"El promedio de los números impares es: {average_odd_numbers}")

    #Si el usuario elige la opción "2" (Juego de palabras):
    elif option == "2":
        #Se solicita al usuario el ingreso de una frase y se la convierte a minúsculas para contar las vocales.
        phrase = input("Ingrese una frase: ")
        phrase = phrase.lower()

        #Se realiza el conteo de la cantidad de cada vocal en la frase mediante la función count().
        count_a = phrase.count('a')
        count_e = phrase.count('e')
        count_i = phrase.count('i')
        count_o = phrase.count('o')
        count_u = phrase.count('u')

        #Se imprimen los resultados.
        print(f"En la frase ingresada hay:")
        print(f"A: {count_a} veces")
        print(f"E: {count_e} veces")
        print(f"I: {count_i} veces")
        print(f"O: {count_o} veces")
        print(f"U: {count_u} veces")

    #Si el usuario elige la opción "0" (Salir):
    elif option == "0":
        print("Saliendo del programa. Adiós")
        break

    #Si el usuario ingresa una opción no válida:
    else:
        print("Opción no válida. Debe ingresar una de las opciones válidas: 1, 2 o 0.")