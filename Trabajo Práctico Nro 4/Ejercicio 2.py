monto_final = 0 #Se inicializa el monto al cual se le añadirán los depositos y sustraerán los retiros

while True:
    linea = input("Ingrese operación ('D':Deposito) ('R':Retiro) (' ':Finalizar) ") #Se solicita el tipo de operación

    if not linea: #Si se ingresa un espacio en blanco se finalizan las operaciones
        break

    #Mediante las siguientes lineas se verifica que el ingreso se 'D' o 'R' seguido del monto a añadir o quitar
    partes = linea.split()
    if len(partes) != 2:
        print("El ingreso no es válido. Ingrese 'D' o 'R' seguido del monto a adicionar o sustraer.")
        continue

    tipo_de_operacion, cantidad = partes #Mediante la siguiente lista se separa la linea ingresada en dos valores, la operacion a realizar y el monto con el que se realizará dicha operación

    #Se realiza la operación correspondiente
    if tipo_de_operacion == 'D':
        monto_final += int(cantidad)
    elif tipo_de_operacion == 'R':
        monto_final -= int(cantidad)
    else:
        print("La operación ingresada no es válida. Ingrese 'D' para depósito o 'R' para retiro.")
        continue

#Se imprime el saldo en la cuenta
print("Saldo:", monto_final)