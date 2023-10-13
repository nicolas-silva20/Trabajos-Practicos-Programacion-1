#Se itera desde 1 hasta 10 para las tablas de multiplicar
for i in range(1, 11):
    print(f"Tabla de multiplicar del {i}:")

    #Se itera desde 1 hasta 10 para cada tabla de multiplicar
    for j in range(1, 11):
        result = i * j
        print(f"{i} x {j} = {result}")

    print()  #Se agrega un espacio en blanco para separar cada tabla