number = int(input("Ingrese un numeo entero positivo:")) #Se solicita el ingreso de un valor entero positivo

#Se crea la lista "impares" donde serán almacenados los valores de tal tipo
odd = []


for n in range(1, number + 1): #Se recorren los valores desde 1 hasta el numero ingresado
    if n % 2 != 0: #Se verifica si el numero en cuesión es impar
        odd.append(n) #En caso de serlo se añade a la lista "impares"

if odd: #Si la lista "impares" cointiene algun valor se imprimen luego de añadirles una ", "
        resultado = ", ".join(map(str, odd))
        print("Números impares desde 1 hasta", number, ":", resultado)