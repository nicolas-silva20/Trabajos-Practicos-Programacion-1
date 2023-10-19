def add_digits(number):
    add = 0
    while number != 0:
        digit = number % 10
        add += digit
        number//= 10
    return add


def choosen_word():
    import random
    words = ["arquitectura", "medicina", "psicologia", "abogacia", "ingenieria"]
    return random.choice(words)

def show_word(word, guessed_letters):
    result = ""
    for letter in word:
        if letter in guessed_letters:
            result += letter
        else:
            result += "_"
    return result