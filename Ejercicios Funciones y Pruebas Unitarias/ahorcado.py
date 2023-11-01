import sys
sys.path.append("D:/Facultad/Programacion/TP y Ejercicios en Clase/Funciones")
import funciones

import random


word = funciones.choosen_word()
guessed_letters = []
lifes = 6

print("Juego del ahorcado: ")
print(funciones.show_word(word, guessed_letters))

while True:
    letter = input("Ingresa una letra: ").lower()

    if len(letter) != 1 or not letter.isalpha():
        print("Ingresa una letra válida.")
        continue

    if letter in guessed_letters:
        print("Ya ingresaste esa letra.")
        continue

    guessed_letters.append(letter)

    if letter not in word:
        lifes -= 1
        print(f"Letra incorrecta. Te quedan {lifes} vidas.")
        if lifes == 0:
            print(f"Perdiste. La palabra era: {word}")
            break

    current_word = funciones.show_word(word, guessed_letters)
    print(current_word)

    if "_" not in current_word:
        print("Bien! Adivinaste la palabra.")
        break