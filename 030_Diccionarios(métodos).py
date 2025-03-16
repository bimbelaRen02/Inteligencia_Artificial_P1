teclado1 = {
	'Categoría': 'Teclados',
	'Modelo': 'HyperX Alloy FPS Pro',
	'Precio': '89,99'
}

teclado2 = {
	'Categoría': 'Teclados',
	'Modelo': 'Corsair K55 RGB',
	'Precio': '59,99'
}

teclado1['Color'] = 'Negro' #Le agregamos una nueva key con un nuevo value al diccionario teclado1
print(len(teclado1)) #Imprimimos cuántas claves hay en teclado1 con el método len (al igual que con listas y tuplas)
""" #Vaciamos el diccionario teclado1 más no lo eliminamos, solo está vacío
del teclado1['Categoría']
del teclado1['Modelo']
del teclado1['Precio']
del teclado1['Color']"""
del(teclado1) #Eliminamos entero el diccionario teclado1 con el método del (como listas y tuplas)
del teclado2['Categoría']
del teclado2['Precio']

#print(teclado1)
print(teclado2['Modelo'])