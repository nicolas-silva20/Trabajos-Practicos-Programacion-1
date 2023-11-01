import sys
sys.path.append("D:/Facultad/Programacion/TP y Ejercicios en Clase/Funciones")
import funciones


strings = [] #Se crea la lista que contendrá las cadenas a ingresar
while True:
    current_string = input("Ingrese una cadena (presione Enter para finalizar): ")
    if not current_string: #Cuando el usuario presione Enter sin haber escrito una cadena, se rompe el bucle
        break
    strings.append(current_string) #Caso contrario, se añade la cadena a la lista

print("Lista de cadenas original:", strings)
funciones.strings_in_order_insertion(strings)  #Se invoca a la función de ordenamiento.
print("Lista de cadenas ordenada por longitud:", strings)  #Se imprime la lista ordenada.