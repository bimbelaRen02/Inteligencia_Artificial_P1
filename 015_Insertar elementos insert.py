colors = ['rojo', 'azul', 'verde', 'amarillo', 'marrón', 'lila', 'negro', 'rosa', 'blanco', 'naranja']
print(colors)

colors.insert(6, 'magenta')
colors.insert(-1, 'turquesa') #El método insert no permite agregar en la última posición con negativos (-1) será el penúltimo
print(colors)