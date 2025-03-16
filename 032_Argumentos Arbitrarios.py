"""Esta vez verás como utilizar
*args en ellas, los conocidos como
argumentos arbitrarios.
Estos nos permiten dejar un valor indefinido
de argumentos, puedes mandarle de 1 a n valores
y todos los podremos utilizar dentro de la función"""

def colores(*args):
	print('El color', args[1], 'es mi favorito.', 'El color', args[0], 'tampoco está mal.')

colores('Blanco', "Amarillo")

def suma(*args):
	total = args[0] + args[1] + args[2] + args[3] + args[4]
	print(total)
	
suma(10, 15, 20, 25, 30)