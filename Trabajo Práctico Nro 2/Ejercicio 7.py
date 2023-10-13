#Se solicita el ingreso de 3 numeros
numero1 = float(input("Ingrese el primer número: "))
numero2 = float(input("Ingrese el segundo número: "))
numero3 = float(input("Ingrese el tercer número: "))

#Se encuentra el menor de los tres números mediante la funcion min()
menor = min(numero1, numero2, numero3)

#Se imprime el menor número en pantalla
print(f"El menor de los tres números es: {menor}")