"""Las funciones de Python son bloques de
código que solo se van a ejecutar si se les llama.
Para definirlas es con el método
def nombre_de_funcion(argumentos):
Y todo el bloque de código que querramos llamar.
Los argumentos en las funciones son variables que
podemos especificar por defecto al llamar a una función.
Por ejemplo, si la función tuviese que realizar siempre
una suma a partir de dos números, esos son los argumentos
que se requerirían en la llamada a la función, por ejemplo,
suma(numero_1, numero2).
Estas variables (argumentos cuando pertenecen a una función)
son declarados directamente sobre los paréntesis de la función,
no tienes porque declararlos previamente.
Los argumentos que especifiques serán obligatorios en cada llamada.
Estos pueden contener los valores que quieras, un string, un integer,
un booleano, etc. Siempre siguiendo una coherencia basada en el
contenido de la propia función."""

def suma(v1, v2):
    vt = v1 + v2
    print(vt)

suma(10, 20)
suma(20, 30)
suma(50000, 7000)