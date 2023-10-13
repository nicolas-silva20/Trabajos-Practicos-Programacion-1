#Se crea la lista contenedora de las opciones del menú
food_list = [
    "Milanesa a la napolitana", "Bife de chorizo", "Ravioles de ricota",
    "Pechuga de pollo", "Lomo de cerdo"
]

#Se inicializa la variable que almacenará el monto final a pagar por el cliente
amount_to_pay = 0

#Se crea la lista que contendrá las comidas pedidas
final_ticket = []

#Se crea la iteración que permitirá el ingreso de las opciones en el menú 
while True:
  print("---------------------------")
  print("1- Mostrar Menu")
  print("2- Agregar plato")
  print("3- Quitar plato")
  print("4- Elegir metodo de pago (C - TD -TC)")
  print("5- Imprimir ticket")
  print("0- Salir")

  choice = int(input("Ingrese una opción del menú: ")) #Se solicita el ingreso de un valor correspondiente a las opociones del menú inicial

  print()

    
  n=1
  if choice == 1: 
    print("Eligio la opcion 1")
    print("Las opciones del menu son: ")
    for dish in food_list: 
      print(f"{n} {dish}")
      n=n+1 
  elif choice == 2:
    print("Eligio la opcion 2")
    food_item = int(input("Ingrese el item del plato a añadir: ")) # Se agrega el plato seleccionado y actualiza el monto a pagar
    if food_item == 1:
      add_item = food_list[0]
      final_ticket.append(add_item)
      amount_to_pay += 350
    elif food_item == 2:
      add_item = food_list[1]
      final_ticket.append(add_item)
      amount_to_pay += 450
    elif food_item == 3:
      add_item = food_list[2]
      final_ticket.append(add_item)
      amount_to_pay += 320
    elif food_item == 4:
      add_item = food_list[3]
      final_ticket.append(add_item)
      amount_to_pay += 380
    elif food_item == 5:
      add_item = food_list[4]
      final_ticket.append(add_item)
      amount_to_pay += 420
    else:
      print("Ingreso invalido, intente nuevamente")
      continue
  elif choice == 3:
    print("Eligio la opcion 3")
    food_item = int(input("Ingrese el item del plato a remover: ")) # Remueve el plato seleccionado y actualiza el monto a pagar
    if food_item == 1:
      final_ticket.remove("Milanesa a la napolitana")
      amount_to_pay -= 350
    elif food_item == 2:
      final_ticket.remove("Bife de chorizo")
      amount_to_pay -= 450
    elif food_item == 3:
      final_ticket.remove("Ravioles de ricota")
      amount_to_pay -= 320
    elif food_item == 4:
      final_ticket.remove("Pechuga de pollo")
      amount_to_pay -= 380
    elif food_item == 5:
      final_ticket.remove("Lomo de cerdo")
      amount_to_pay -= 420
    else:
      print("Ingreso invalido, intente nuevamente")
      continue
  elif choice == 4:
    print("Eligio la opcion 4")
    payment_method = input("Ingrese el metodo de pago (C - TD - TC)") # Actualiza el monto a pagar según el método de pago elegido
    if payment_method == "C":
      amonut_to_pay = amount_to_pay
    elif payment_method == "TD":
      amount_to_pay = amount_to_pay - (amount_to_pay * 0.05)
    elif payment_method == "TC":
      amount_to_pay = amount_to_pay - (amount_to_pay * 0.10)
    else:
      print("Ingreso inválido, intente nuevamente")
      continue
  elif choice == 5: #Se imprimen los elmentos elegidos por el cliente y el monto a pagar
    print("Eligio la opcion 5")
    print(f"El ticket es:  {final_ticket}")
    print(f"El precio final es: ${amount_to_pay}")
    break
  elif choice == 0: #Se ejecuta la salida del programa
    print("Eligio la opcion 0")
    print("Adios")
    break
  else:
    print("La opción ingresada no es válida, inténtelo nuevamente")
    continue