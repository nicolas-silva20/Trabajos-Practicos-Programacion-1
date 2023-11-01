numbers = [] #Se crea la lista que almacenará los numeros a ingresar

while True:
    number = int(input("Ingrese un número (0 para finalizar): ")) #Se solicita el ingreso de numeros

    if number == 0: #Al ingresarse el numero 0 el bucle finalizará
        break
    else:
        numbers.append(number) #Si el numero no es 0, se añade a la lista

if numbers:
    print("Números ingresados:", numbers)
else:
    print("No se ingresaron números.")