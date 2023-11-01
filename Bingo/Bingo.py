import sys
sys.path.append("D:/Facultad/Programacion/TP y Ejercicios en Clase/Funciones")
import funciones

print("¡Bienvenido al juego de Bingo!")
    
while True:
    bingo_card = funciones.generate_bingo_card()
    funciones.print_bingo_card(bingo_card)
    funciones.play_bingo(bingo_card)

    play_again = input("¿Desea jugar de nuevo? (Sí/No): ").strip().lower()
    if play_again != "si":
        break