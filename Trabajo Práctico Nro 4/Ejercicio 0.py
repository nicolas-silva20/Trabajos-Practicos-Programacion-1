x = 0

while x < 30:
    if x == 15:
        break
    if x in [4, 6, 10]:
        print("Se saltó el valor " + str(x) + " de x")
        x += 1
        continue
    print(str(x))
    x += 1

if x == 15:
    print("Se rompió la ejecución del bucle cuando x valía " + str(x))