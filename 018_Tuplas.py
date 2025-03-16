"""Las tuplas son listas inmutables, es decir,
no se pueden modificar una vez creadas, ni se añaden ni se quitan.
Fuera de modificarlas, podemos hacer las mismas cosas que con una lista."""

colors = ('rojo', 'azul', 'verde', 'amarillo', 'marrón', 'lila', 'negro', 'rosa', 'blanco', 'naranja')
print(colors[1]) #Imprimimos el índice 1 de la tupla

nums = (10, 1, 5, 11)
op = nums[0] - nums[1] + nums[2] + nums[3] #Hacemos una operación aritmética con algunos elementos de la tupla
print(op) #Imprimimos el resultado de la operación