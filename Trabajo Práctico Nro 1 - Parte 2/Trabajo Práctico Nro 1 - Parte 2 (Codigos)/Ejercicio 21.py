#Se solcita el ingreso de los datos necesarios
km_por_litro = float(input("Ingrese cuántos kilómetros puede recorrer su moto con 1 litro de combustible: "))
capacidad_tanque = float(input("Ingrese la capacidad del tanque en litros: "))
km_total = float(input("Ingrese cuántos kilómetros en total recorrerán: "))

#Se calculan la cantidad de tanques de combustible necesarios
tanques_necesarios = km_total / km_por_litro

#Se imprime la cantidad de tanques de combustible necesarios
print(f"Para recorrer {km_total} kilómetros, necesitarán {tanques_necesarios:.2f} tanques de combustible.")