#Se pregunta al usuario si desea calcular el área de un triángulo o un círculo
opcion = input("¿Desea calcular el área de un triángulo (T) o un círculo (C)? ").lower() #Se convierte el caracter ingresado a minuscula para realizar el condicional

if opcion == 't':
    #Se calcula el área del triángulo
    base = float(input("Ingresa la base del triángulo: "))
    altura = float(input("Ingresa la altura del triángulo: "))
    area = 0.5 * base * altura
    print(f"El área del triángulo es: {area}")
elif opcion == 'c':
    #Se calcula el área del círculo
    radio = float(input("Ingresa el radio del círculo: "))
    area = 3.14159 * (radio ** 2)
    print(f"El área del círculo es: {area}")
else:
    print("Opción no válida. Ingresa 'T' para triángulo o 'C' para círculo.")