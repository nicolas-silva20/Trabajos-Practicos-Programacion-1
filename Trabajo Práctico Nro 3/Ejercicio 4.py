#Se solicita el ingreso de un numero entero
number = int(input("Ingrese un número entero positivo: "))

#Se verifica que el numero ingresado sea mayor a 0, caso contrario se solicita el ingreso nuevamente
if number < 0:
    print("Por favor, ingrese un número entero positivo.")
else:
    countdown = "" #Se crea inicializa una cadena vacía donde se almacenará los numeros y comas
    while number >= 0: #En tanto el valor que ingresa al bucle sea mayor a '0' el bucle se ejecutará
        countdown += str(number) #Se ingresa a la cadena el valor del numero inicial convertido a cadena
        if number > 0:
            countdown += ", " #Se añade una coma y un espacio al numero en la cadena
        number -= 1 #Se decrementa el valor del numero en 1
    print(countdown) #Se imprime la cadena con los numeros separados por coma