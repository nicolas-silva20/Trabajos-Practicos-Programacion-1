#Se solicita al usuario que elija el tipo de pizza
print("Elija el tipo de pizza:")
print("1. Pizza vegetariana")
print("2. Pizza no vegetariana")
opcion = int(input("Ingrese el número de su elección: "))

#Se define la lista de ingredientes comunes a todas las pizzas
ingredientes_comunes = ["mozzarella", "tomate"]

#Se inicializa la lista de ingredientes adicionales vacía
ingredientes_adicionales = []

#En caso de ser una pizza vegetariana:
if opcion == 1:
    print("Elija un ingrediente adicional para su pizza vegetariana:")
    print("1. Pimiento")
    print("2. Tofu")
    ingrediente_elegido = int(input("Ingrese el número de su elección: "))
    
    if ingrediente_elegido == 1:
        ingredientes_adicionales.append("pimiento")
    elif ingrediente_elegido == 2:
        ingredientes_adicionales.append("tofu")
    else:
        print("Opción no válida")

#En caso de no ser una pizza vegetariana:
elif opcion == 2:
    print("Elija un ingrediente adicional para su pizza no vegetariana:")
    print("1. Peperoni")
    print("2. Jamón")
    print("3. Salmón")
    ingrediente_elegido = int(input("Ingrese el número de su elección: "))
    
    if ingrediente_elegido == 1:
        ingredientes_adicionales.append("peperoni")
    elif ingrediente_elegido == 2:
        ingredientes_adicionales.append("jamón")
    elif ingrediente_elegido == 3:
        ingredientes_adicionales.append("salmón")
    else:
        print("Opción no válida")

#Se imprime la información de la pizza
print("Su pizza es:")

if opcion == 1:
    print("Pizza vegetariana con los siguientes ingredientes:")
else:
    print("Pizza no vegetariana con los siguientes ingredientes:")
    
print(", ".join(ingredientes_comunes + ingredientes_adicionales))