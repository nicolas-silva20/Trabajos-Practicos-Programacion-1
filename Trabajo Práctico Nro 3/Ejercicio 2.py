age = int(input("Ingrese su edad:")) #Se solicita el ingreso de la edad del usuario

#Se imprime la cantidad de años cumplidos por el mismo. Se coloca el valor mínimo 1 y al valor de la edad se le suma +1 para que sea leída durante la ejecución del bucle
print("Usted ha cumplido los siguientes años:")
for n in range(1, age + 1):
    print(n)