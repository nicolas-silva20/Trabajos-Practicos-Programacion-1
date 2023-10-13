lineas = [] #Se crea la lista que almacenará las lineas a ingresar

#Se pide el ingreso de lineas
while True:
    linea = input("Ingrese una línea (o deje en blanco para finalizar): ")
    
    if not linea:
        break  #Se asle del bucle en caso de que no se ingrese ninguna linea
    
    lineas.append(linea)  #Se agregan la linea ingresada la lista

#Se imprimen las lineas luego de convertirlas a mayuscula
for linea in lineas:
    print(linea.upper())