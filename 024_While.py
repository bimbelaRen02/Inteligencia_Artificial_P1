x = 0
y = 0
z = 10

"""Con el bucle while podrás ejecutar una serie de declaraciones siempre que
la condición se cumpla, que sea verdadera.
Una vez se convierta en falsa, va a dejar de ejecutar el código del bucle.
La condición suele ser una variable iteradora que cambia su valor en cada vuelta"""

while x <= 15:
    print(x)
    x += 5 #Iterador  incrementa (+=) en 5 cada vuelta
print("\n")

while y >= -100:
    print(y)
    y -= 20 #Iterador  decrementa (-=) en 20 cada vuelta
print("\n")

while z >= 0:
    print('El valor del iterador es: ' + f"{z}") #Para concatenar una string y un número hay que convertir el número en string con la función f"{variable}"
    z -= 1 #Iterador  decrementa (-=) en 1 cada vuelta