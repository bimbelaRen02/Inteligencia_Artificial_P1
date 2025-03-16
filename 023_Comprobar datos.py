colors = ('Rojo', 'Azul', 'Blanco', 'Negro') #Definimos la tupla
selected_color = input('Selecciona el color de tu equipo en Halo:\n') #En este input no necesitamos especificar el tipo de la variable porque se espera una string

#El comparativo in busca una variable en una lista o tupla
if selected_color in colors: #Consultamos si la string recibida en input está en la tupla
    print('Ahora perteneces al equipo ' + selected_color + '.') #Si está, entonces imprime que pertenece a un color
else:
    print("No hay ningún equipo color " + selected_color + ', lo sentimos.') #Si no está, entonces imprime que el color seleccionado no está