#Se solicita el ingreso de los coeficientes 'a' y 'b'
a = float(input("Ingrese el coeficiente 'a': "))
b = float(input("Ingrese el coeficiente 'b': "))

#Se verifica si 'a' es igual a 0
if a == 0:
    if b == 0:
        print("La ecuación tiene infinitas soluciones.")
    else:
        print("La ecuación no tiene solución.")
else:
    x = -b / a
    print(f"La solución de la ecuación es x = {x:.2f}") #Se formatea el resultado para que muestren solo 2 decimales