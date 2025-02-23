colors = ['rojo', 'azul', 'verde', 'amarillo', 'marrón', 'lila', 'negro', 'rosa', 'blanco', 'naranja']
print(colors)

newcolors_1 = colors.pop(-2)
newcolors_2 = colors.pop(1)
newcolors = [newcolors_1, newcolors_2]

print(colors)
print(newcolors)