#Funcion - Sumar Digitos y Numeros
def add_digits(number):
    add = 0
    while number != 0:
        digit = number % 10 #Se obtiene el ultimo dígito del número
        add += digit #Se suma el ultimo digito al resultado
        number//= 10 #Se elimina el ultimo dígito del numero
    return add #Se retorna la suma de los dígitos del numnero



#Funciones - Ahorcado
def choosen_word():
    import random
    words = ["arquitectura", "medicina", "psicologia", "abogacia", "ingenieria"]
    return random.choice(words) #Se retorna una palabra del la lista "words" elegida de manera aleatoria

def show_word(word, guessed_letters):
    result = ""
    for letter in word:
        if letter in guessed_letters: #En caso de haber sido adivinada la letra, es mostrada
            result += letter
        else:
            result += "_" #Caso contrario, se muestran "_"
    return result #Se retorna la cadena que muestra las letras adivinadas en su lugar y "_" donde quedan letras desconocidas aun






#Funciones - Bingo
import random

def generate_bingo_card():
    #Se genera el cartón de bingo para el usuario.
    #El usuario ingresa 25 números únicos en el rango de 1 a 75 para completar el cartón.
    #Se retorna una matriz de 5x5 con los números ingresados, conformada por 5 listas con 5 de los numeros ingresados cada una.

    bingo_card = []
    eneterd_numbers = 0
    while eneterd_numbers < 25:
        number = input("Ingrese un número único (1-75) para su cartón de bingo: ")
        if number.isdigit():
            number = int(number)
            if 1 <= number <= 75 and number not in bingo_card:
                bingo_card.append(number)
                eneterd_numbers += 1
            else:
                print("Ingrese un número válido y único en el rango de 1 a 75.")
        else:
            print("Ingrese un número válido y único en el rango de 1 a 75.")

    bingo_card_as_matrix = [bingo_card[i:i + 5] for i in range(0, 25, 5)]
    
    return bingo_card_as_matrix

def print_bingo_card(bingo_card, completed_line=None):
    #Función que muestra el estado actual del cartón de bingo al usuario.
    #Muestra los números en un formato de matriz de 5x5.
    #Si una celda está en la línea completa, muestra 'X' en lugar del número.

    print("Su cartón de Bingo:")
    for i in range(5):
        for j in range(5):
            if completed_line and (i, j) in completed_line:
                print("X", end="  ")
            else:
                print(bingo_card[i][j], end="  ")
        print()

def check_completed_line(bingo_card):
    #Función que verifica si se ha completado una línea en el cartón de Bingo.
    #Comprueba filas, columnas y diagonales para líneas completas.
    #Devuelve las coordenadas de la línea completa si existe, de lo contrario, devuelve una lista vacía.

    for i in range(5):
        if all(bingo_card[i][j] == 'X' for j in range(5)) or all(bingo_card[j][i] == 'X' for j in range(5)):
            return [(i, j) for j in range(5)]
    if all(bingo_card[i][i] == 'X' for i in range(5)) or all(bingo_card[i][4 - i] == 'X' for i in range(5)):
        return [(i, i) for i in range(5)]
    return []

def play_bingo(bingo_card):
    #Función que simula el juego de Bingo.
    #Extrae números al azar del rango de 1 a 75 hasta que se complete una línea en el cartón.
    #Muestra el estado actual del cartón y los números extraídos.

    extracted_numbers = set()
    extracted_balls = []

    while True:
        number = random.randint(1, 75)
        if number not in extracted_numbers:
            extracted_numbers.add(number)
            extracted_balls.append(number)
            
            for i in range(5):
                for j in range(5):
                    if bingo_card[i][j] == number:
                        bingo_card[i][j] = 'X'
            
            completed_line = check_completed_line(bingo_card)
            
            print_bingo_card(bingo_card, completed_line)
            print(f"Números extraídos: {', '.join(map(str, extracted_balls))}")

            if completed_line:
                print("¡Bingo! Ha completado al menos una línea. ¡Felicidades!")
                break

            input("Presione Enter para continuar...")


#Funciones TP N° 5

#Ejercicio 1
def validate_dni(dni_number):

    if isinstance(dni_number, str) and dni_number.isdigit(): #Se verifica que el usuario haya ingresado una cadena de digitos numericos
        #Se verifica que el numero de DNI tenga entre 7 y 8 digitos
        if 7 <= len(dni_number) <= 8:
            return True #Si se cumplen las condiciones se retorna "True"
    else:
        return False #Caso contrario, se retorna "False"


#Ejercicio 4
def is_multiple(first_number, second_number):

    if second_number == 0: #Se verifica que el segundo numero no sea cero
        return False  #En tal caso,se evita la división por cero
    return first_number % second_number == 0 #Si es distinto de 0, se retorna True o False si uno de los numeros es multiplo del otro o no, respectivamente


#Ejercicio 7
def find_max_min(list):
    #Se inicializan los valores máximo y mínimo como None
    maximum = minimum = None

    #Se verifica si la lista está vacía
    if not list:
        return None, None

    #Se recorre la lista de números
    for each_value in list:
        valid_number = True

        #Se verifica cada caracter en el valor
        for caracter in each_value:
            #Se comprueba si el caracter es un dígito o un punto (para números decimales)
            if not (caracter.isdigit() or (caracter == '.' and '.' not in each_value)):
                valid_number = False
                break

        #Si el valor es un número válido, se lo convierte a tipo float
        if valid_number:
            number = float(each_value)

            #Se actualiza el valor máximo y mínimo
            if maximum is None or number > maximum:
                maximum = number
            if minimum is None or number < minimum:
                minimum = number

    #Se retorna el valor máximo y mínimo
    return maximum, minimum



#Funciones TP N°7
#Ejercicio 1
def numbers_in_order_bubble(numbers_list):
    n = len(numbers_list)
    for i in range(n): #Se itera a través de la lista
        for j in range(0, n - i - 1): #Se itera a través de los elementons no ordenados de la lista
            if numbers_list[j] > numbers_list[j + 1]: 
                #Se intercambian los elementos si el actual es mayor que el siguiente
                numbers_list[j], numbers_list[j + 1] = numbers_list[j + 1], numbers_list[j]

#Ejercicio 2
def words_in_order_selection(words_list):
    n = len(words_list)
    for i in range(n): #Se itera a través de la lista
        minimum_element = i #Se supone al valor actual como el valor minimo
        for j in range(i + 1, n): #Se busca a un elemento menor que el valor actual
            if words_list[j] < words_list[minimum_element]:
                minimum_element = j #Se actualiza el valor minimo en caso de encontraselo
        words_list[i], words_list[minimum_element] = words_list[minimum_element], words_list[i] #Se intercambia el elemento actual con el encontrado

#Ejercicio 4
def strings_in_order_insertion(strings_list):
    n = len(strings_list) #Se obtiene la longitud de la lista de cadenas

    for i in range(1, n): #Se recorre la lista desde el segundo elemento (índice 1) hasta el último.
        current_string = strings_list[i]  #Se guarda la cadena actual que se va a insertar en la posición correcta.
        length_current_string = len(current_string)  #Se obtiene la longitud de la cadena actual.
        j = i - 1  #Se inicializa j para comparar con las cadenas anteriores.

        #Mientras j sea mayor o igual a cero y la longitud de la cadena en lista[j] sea mayor que la longitud actual:
        while j >= 0 and len(strings_list[j]) > length_current_string:
            strings_list[j + 1] = strings_list[j]  #Se mueve la cadena anterior a la derecha.
            j -= 1  #Se avanza hacia atrás en la lista.

        strings_list[j + 1] = current_string  #Se inserta la cadena actual en la posición correcta.



#Funciones TP N°8
#Ejercicio 1
def count_digits(n):
    if n < 10:
        return 1  #Cuando n es un solo dígito, se retorna 1.
    else:
        return 1 + count_digits(n // 10)  #Se divide n por 10 y se llama a la función recursivamente.


#Ejercicio 5
def add_elements():
    numbers_list = [] #Se crea la lista que contendrá los valores a ingresar
    while True:
        entrance = input("Ingrese un número (o 'fin' para terminar): ")
        if entrance.lower() == 'fin': #Se verifica si el usuario ingresó 'fin'
            break #En tal caso, se rompe el bucle
        if entrance.isdigit():
            number = int(entrance)
            numbers_list.append(number) #Caso contrario, se añade el valor a la lista
        else:
            print("Ingrese un número válido.")
    return numbers_list #Se retorna la lista


def find_greatest(numbers_list):
    #Caso base: si la lista tiene un solo elemento, ese es el mayor
    if len(numbers_list) == 1:
        return numbers_list[0]
    else:
        #Se llama recursivamente a la función con una sublista que excluye el primer elemento
        greatest_sublist = find_greatest(numbers_list[1:])
        #Se compara el primer elemento de la lista con el mayor de la sublista y devuelve el valor más grande utilizando la función max
        return max(numbers_list[0], greatest_sublist)



#Ejercicio 7
def calculate_summation(n, p):
    #Caso base: si n es 1, se retorna p (el primer término).
    if n == 1:
        return p
    #Llamada recursiva para calcular la sumatoria de los términos anteriores y sumar el término actual.
    return n * p + calculate_summation(n - 1, p)