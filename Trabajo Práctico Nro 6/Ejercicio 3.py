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

number_to_delete = int(input("Ingrese un número a eliminar: ")) #Se solicita el numero a eliminar de la lista

if number_to_delete in numbers: #Se revisa si el valor ingresado se encuentra en la lista
    numbers.remove(number_to_delete) #Si es hallado, se elimina
    print(f"Se ha eliminado la primera ocurrencia de {number_to_delete}.")
    print("Nueva lista de números:", numbers)
else:
    print(f"No se pudo eliminar {number_to_delete} porque no está en la lista.") #Si no es hallado, se imprime el mensaje correspondiente

summation = sum(numbers) #Se crea la variable que almacenará el valor de la suma y mediante la funcion "sum()" se realiza dicha sumatoria
print(f"La sumatoria de los números en la lista es: {summation}")