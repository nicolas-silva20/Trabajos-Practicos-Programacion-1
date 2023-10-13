#Se solicita el ingreso del año actual
año_actual = int(input("Ingrese el año actual: "))

#Se solicita el ingreso del año a comparar
año_comparar = int(input("Ingrese un año para comparar: "))

#Se calcula la diferencia de años
diferencia_años = año_actual - año_comparar

#Se determina si se trata de años pasados o años futuros
if diferencia_años > 0:
    print(f"Han pasado {diferencia_años} años desde el año {año_comparar} hasta el año {año_actual}.")
elif diferencia_años < 0:
    print(f"Faltan {abs(diferencia_años)} años para llegar al año {año_comparar} desde el año {año_actual}.")
else:
    print(f"Estamos en el año {año_actual}")