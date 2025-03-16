colors = ['rojo', 'azul', 'verde', 'amarillo', 'marrón', 'lila', 'negro', 'rosa', 'blanco', 'naranja']
print(colors)

#Podemos mover elementos de una lista a una variable con la función pop
newcolors_1 = colors.pop(-2)
newcolors_2 = colors.pop(1)
newcolors = [newcolors_1, newcolors_2] #Creamos una nueva lista con los valores sacados de la lista original

print(colors)
print(newcolors)