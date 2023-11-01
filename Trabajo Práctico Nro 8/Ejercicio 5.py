import sys
sys.path.append("D:/Facultad/Programacion/TP y Ejercicios en Clase/Funciones")
import funciones

elements = funciones.add_elements() #Se solicita el ingreso de los valores de la lista, para ello se emplea una funcion

if elements:
    #Se invoca a la función para encontrar el mayor elemento en la lista
    greatest = funciones.find_greatest(elements)
    print(f"El mayor elemento de la lista es: {greatest}")
else:
    print("La lista está vacía.")