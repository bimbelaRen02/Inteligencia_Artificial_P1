'''Las clases en Python son la base de la programación
orientada a objetos. Permiten definir un "molde" para
crear objetos con atributos (datos) y métodos (funciones)
asociados. Se definen con la palabra clave class, y los
objetos que se crean a partir de ellas pueden tener
comportamientos y características específicos.
¡Son útiles para estructurar el código y reutilizarlo!'''

"""El método __init__, es un método especial que podemos
poner en las clases para establecer unos valores iniciales
a los objetos que se creen a partir de la clase que lo contenga."""

'''self es como el this en otros lenguajes de programación.
Es simplemente una palabra reservada de Python para
referirse "a si mismo", de esa forma no tenemos que escribir
por ejemplo NombreDeClase.atributo1, NombreDeClase.atributo2.'''

"""Para declarar una clase vacía en Python, solo tienes que
utilizar pass tal y como en bucles o condicionales.
Eliminar atributos de un objeto es tan sencillo cómo utilizar
del seguido del nombre del objeto y el atributo a eliminar:
del nombre_objeto.atributo
Para eliminar el objeto solo necesitamos del y nombre del objeto:
del objeto1"""

'''La herencia nos permite que una clase obtenga propiedades
de otra clase. En general, la herencia se utiliza para ahorrarnos
código y evitar tener que repetir cosas.
En la herencia, llamamos a la clase de la cual heredan otras clases,
clase padre, clase base, principal o superclase.
Puedes llamarla como quieras. A las que reciben la herencia se
les llama clases hijo, derivadas, secundarias o subclases.'''

"""En este caso se utiliza el __init__ de la subclase,
ya que al volver a declararlo, lo estamos reemplazando por
el suyo propio. El resto de elementos se heredan con normalidad.
Esto lo que demuestra, es que si en las subclases redeclaras cosas,
prevalecen las redeclaraciones pertenecientes a la propia clase."""

'''El término "scope" se refiere al alcance que tiene una variable,
si es local o global. Las variables de las funciones son de ámbito
local y solo podemos acceder a ellas dentro de la misma función.
En cambio, las variables declaradas fuera de una función son directamente
globales y las podemos utilizar tanto dentro como fuera de ellas.'''

"""Una función anidada en Python es una función definida dentro de
otra función. Nos sirve para encapsular lógica que solo debe usarse
dentro del contexto de la función externa, ayudando a organizar
mejor el código y mantenerlo más limpio y seguro.
Las funciones lambda en Python, también llamadas funciones anónimas,
son funciones con una sintaxis simplificada que pueden tener solo
una expresión.
Son útiles para definir funciones rápidas y temporales, especialmente
como argumentos de otras funciones, sin necesidad de definirlas."""

# Clase vacía usando pass:
class ClaseVacia:
    pass

# Superclase:
class Persona:
    def __init__(self, nombre, edad):  # Método __init__ para inicializar atributos
        self.nombre = nombre
        self.edad = edad

    def mostrar_info(self):  # Método para mostrar información
        print("Soy ", self.nombre, " y tengo ", self.edad, " años.")  # Concatenamos con comas

    # Método para incrementar la edad y actualizar una variable global
    def incrementar_edad(self, age):
        global edad_global  #Declaramos una variable global
        self.edad += age
        edad_global = age  # Actualizamos la variable global
        print("Ahora tengo ", self.edad, " años.")

# Subclase que hereda de Persona:
class Empleado(Persona):
    def __init__(self, nombre, edad, puesto):
        super().__init__(nombre, edad)  # super() hereda atributos remplaza lo siguiente:
        # self.nombre = nombre
        # self.edad = edad
        self.puesto = puesto

    def mostrar_info(self):  # Método para mostrar información específica del empleado
        print("Soy ", self.nombre, ", tengo ", self.edad, " años y trabajo como ", self.puesto, ".")

# Creación de objetos:
persona = Persona("Carlos", 22)
empleado = Empleado("Bimpolla", 22, "Ingeniero Mecatrónico")

# Uso de los métodos y atributos:
persona.mostrar_info()
persona.incrementar_edad(5)
print("Los años añadidos fueron: ", edad_global) #Usamos la variable global después de ser modificada
empleado.mostrar_info()

# Ejemplo de clase vacía:
objeto_vacio = ClaseVacia()
print("Esto es un objeto de la clase vacía: " + f"{type(objeto_vacio)}")