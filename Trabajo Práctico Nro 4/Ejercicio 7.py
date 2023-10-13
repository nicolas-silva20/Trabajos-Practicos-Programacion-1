while True:
    print("Menú de opciones:")
    print("1. Opción 1")
    print("2. Opción 2")
    print("3. Opción 3")
    print("0. Salir")

    option = input("Elija una opción: ")

    if option == "0":
        print("Saliendo del programa.")
        break
    elif option == "1":
        print("Ha elegido la opción 1.")
    elif option == "2":
        print("Ha elegido la opción 2.")
    elif option == "3":
        print("Ha elegido la opción 3.")
    else:
        print("Opción no válida. Intente nuevamente.")