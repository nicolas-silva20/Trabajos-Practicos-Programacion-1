#Se solicita el ingreso de una frase
phrase = input("Por favor, ingrese una frase: ")

#Se define una lista con las vocales
vowels = ['a', 'e', 'i', 'o', 'u']

#Se incializa un conjunto vacío para almacenar las vocales sin repetirse
vowels_once = set()

#Se recorren los caracteres de la frase y se buscan las vocales
for letter in phrase:
    if letter.lower() in vowels: #Se convierte el caracter en la iteracion a minuscula para poder compararla con las vocales en la lista
        vowels_once.add(letter.lower()) #Si el caracter coincide con alguna de las vocales en la lista, se añade al conjunto

#Se imprimen las vocales encontradas
print("Las vocales que encontradas son:")
for vowel in vowels_once:
    print(vowel)