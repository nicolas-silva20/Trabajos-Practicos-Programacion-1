#Se solicita el ingreso de la temperatura en grados Fahrenheit
fahrenheit = float(input("Ingrese la temperatura en grados Fahrenheit: "))

#Se realiza la conversión a grados Celsius
celsius = (fahrenheit - 32) * 5/9

#Se imprime el resultado
print(f"{fahrenheit} grados Fahrenheit son equivalentes a {celsius} grados Celsius.")