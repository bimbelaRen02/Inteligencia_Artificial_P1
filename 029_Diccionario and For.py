"""Los valores de las claves en los diccionarios pueden
modificarse indicando el diccionario, su clave y asignandole
el nuevo valor. Ejemplo:
diccionario1['key1'] = 'value2' """

teclado1 = {
	'Categoría': 'Teclados',
	'Modelo': 'HyperX Alloy FPS Pro',
	'Precio': '$89,99'
}

for x in teclado1:
    print(x + " = " + teclado1[x] + '.') #Si imprimos x da el valor de la clave, si ponemos diccionario[x] es el valor