count_primes = 0

while True:
    num = int(input("Ingresa un numero ('0' para detener el conteo): "))
    
    if num == 0:
        break

    if num > 1:
        is_prime = True
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                is_prime = False
                break
        if is_prime:
            count_primes += 1

print(f"Numero de numeros primos ingresados: {count_primes}")