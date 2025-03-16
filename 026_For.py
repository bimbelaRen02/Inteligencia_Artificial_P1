colores = ('rojo', 'azul', 'verde', 'amarillo')

""" Lo que está pasando aquí es que he creado un bucle for con una
variable llamada x y le digo que me itere el string, por lo que cada
vuelta que da el bucle, almacena una letra del string que es la que
saca en cada print()."""

for x in colores:
    print(x) 

for x in '':
    pass #Esta instrucción brinca el bucle for y while, sirve para compilar sin errores pero sin hacer algo