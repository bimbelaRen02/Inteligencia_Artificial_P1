x = 0
y = 0
z = 10

while x <= 15:
    print(x)
    x += 5
print("\n")

while y >= -100:
    print(y)
    y -= 20
print("\n")

while z >= 0:
    print('El valor del iterador es: ' + f"{z}") #Para concatenar una string y un número hay que convertir el número en string con la función f"{variable}"
    z -= 1