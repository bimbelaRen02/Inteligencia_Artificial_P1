colors = ['rojo', 'azul', 'verde', 'amarillo', 'marrón', 'lila', 'negro', 'rosa', 'blanco', 'naranja']
print(colors)

print(sorted(colors, reverse=True)) #Organizamos los elementos de una lista con la función sorted activando el reverse para ser de Z-A dentro del print para NO modificar la lista
print(colors)
colors.sort(reverse=True) #Aquí con sort SÍ modificamos la lista
print(colors)