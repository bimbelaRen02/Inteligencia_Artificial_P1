colors = ['rojo', 'azul', 'verde', 'amarillo', 'marrón', 'lila', 'negro', 'rosa', 'blanco', 'naranja']
print(colors)

#Podemos inertar elementos en una posición específico de una lista con la función insert(índice, elemento)
colors.insert(6, 'magenta') #Añadimos magenta en la posición de índice 6
colors.insert(-1, 'turquesa') #El método insert no permite agregar en la última posición con negativos (-1) será el penúltimo
print(colors)