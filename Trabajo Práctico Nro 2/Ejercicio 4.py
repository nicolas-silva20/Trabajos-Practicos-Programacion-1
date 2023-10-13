#Se muestran las opciones de candidatos disponibles
print("Opciones de candidatos:")
print("A - Candidato A por el partido rojo")
print("B - Candidato B por el partido verdad")
print("C - Candidato C por el partido azul")

#Se solicita el ingreso del voto
voto = input("Elija un candidato (A/B/C): ")

#Se verifica la elección del usuario y se muestra el mensaje correspondiente
if voto == "A":
    print("Usted ha votado por el partido rojo.")
elif voto == "B":
    print("Usted ha votado por el partido verdad.")
elif voto == "C":
    print("Usted ha votado por el partido azul.")
else:
    print("Opción errónea: La opción ingresada no corresponde a ninguno de los candidatos disponibles.")