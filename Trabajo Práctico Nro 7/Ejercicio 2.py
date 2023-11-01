import sys
sys.path.append("D:/Facultad/Programacion/TP y Ejercicios en Clase/Funciones")
import funciones

words = []

while True:
    palabra = input("Ingrese una palabra (o 'fin' para terminar): ")
    if palabra.lower() == 'fin':
        break
    words.append(palabra)

if words:
    print("Lista de palabras:", words)
    funciones.words_in_order_selection(words)
    print("Lista de palabras ordenada:", words)
else:
    print("No se ingresaron palabras.")