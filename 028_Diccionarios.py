"""Los diccionarios en Python equivalen
a las estructuras en C++ o Java, permiten en una sola variable
ponerle características (key) con sus valores (value) para
declararse de hace con llaves {} y se separan las keys con comas"""

teclado1 = {
	'Categoría': 'Teclados',
	'Modelo': 'HyperX Alloy FPS Pro',
	'Precio': '$89,99'
}

teclado2 = {
	'Categoría': 'Teclados',
	'Modelo': 'Corsair K55 RGB',
	'Precio': '$59,99'
}

print(teclado1) #Imprimes todos los datos del diccionario
print(teclado1['Modelo']) #Imprimes solamente el valor de una key de un diccionario
print("El modelo " + teclado2['Modelo'] + " cuesta " + teclado2['Precio']) #Imprimimos un mensaje con valores del diccionario 2