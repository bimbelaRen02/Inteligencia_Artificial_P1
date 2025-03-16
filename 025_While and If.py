"""break lo que hace es romper el flujo de ejecución del bucle y
se pueden hacer saltos dentro del bucle while gracias a continue."""

x = 0
while x <= 30:
    x += 1
    if x == 15:
        print("Se detuvo la ejecución cuando x valía 15")
        break #La instrucción break detiene la ejecución del bucle mientras cumpla la condición del if
    if x == 4 or x == 6 or x == 10:
        print("Se saltó el valor " + f"{x}" " de x")
        continue #La instrucción continue salta la iteración actual del bucle y continúa con la siguiente
    print('El valor del bucle es: ' + f"{x}") #Para concatenar una string y un número hay que convertir el número en string con la función f"{variable}"