#Se solicita al usuario una palabra
word = input("Ingresa una palabra: ")

#Se revierte la palabra y se almacena en una nueva variable
word_reverse = word[::-1]

#Se imprimen de a una las letras de la cadena que contiene la palabra en reversa
for letter in word_reverse:
    print(letter)