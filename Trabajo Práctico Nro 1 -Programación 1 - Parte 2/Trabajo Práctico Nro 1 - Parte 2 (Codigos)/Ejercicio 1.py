#Se solicitael ingreso de la base y la altura del rectángulo
base = float(input("Ingrese la base del rectángulo: "))
altura = float(input("Ingrese la altura del rectángulo: "))

#Se calcula el perímetro y el área
perimetro = 2 * (base + altura)
area = base * altura

#Se imprimen los resultados
print(f"El perímetro del rectángulo es: {perimetro}")
print(f"El área del rectángulo es: {area}")