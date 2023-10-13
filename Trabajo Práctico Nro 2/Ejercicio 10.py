#Se solicita el ingreso de la edad del usuario
edad = int(input("Ingrese su edad: "))

#Se calcula el precio de la entrada según la edad
if edad < 4:
    precio_entrada = 0  #Menores de 4 años entran gratis
elif edad >= 4 and edad <= 18:
    precio_entrada = 500  #Edades entre 4 y 18 años pagan $500
else:
    precio_entrada = 1000  #Mayores de 18 años pagan $1000

#Se imprime el precio de la entrada
print(f"El precio de la entrada es: ${precio_entrada}")