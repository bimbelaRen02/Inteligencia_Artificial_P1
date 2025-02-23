colors = ('Rojo', 'Azul', 'Blanco', 'Negro')
selected_color = input('Selecciona el color de tu equipo en Halo:\n')

if selected_color in colors:
    print('Ahora perteneces al equipo ' + selected_color + '.')
else:
    print("No hay ningún equipo color " + selected_color + ', lo sentimos.')