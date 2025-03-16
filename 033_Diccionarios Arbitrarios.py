"""Terminamos con las funciones en este curso viendo **kwargs.
Cuando queremos utilizar argumentos arbitrarios en diccionarios,
*args no nos va a servir, ya que los diccionarios constan de dos
partes, las claves y los valores. En este caso, necesitas usar **kwargs."""

def colores (**kwargs):
	print("Mi color favorito es el " + kwargs['color1'] + '.')
	print('Mi color menos favorito es el ' + kwargs['color2'] + '.')

colores(color1='amarillo', color2='café')