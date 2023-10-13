#Se solicitan los valores de los catetos
cateto_a = float(input("Ingrese la longitud del primer cateto: "))
cateto_b = float(input("Ingrese la longitud del segundo cateto: "))

#Se calcula la hipotenusa usando el teorema de Pitágoras
hipotenusa = (cateto_a ** 2 + cateto_b ** 2) ** 0.5

#Se imprime el resultado
print(f"La longitud de la hipotenusa es: {hipotenusa}")