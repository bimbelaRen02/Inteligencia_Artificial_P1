"""La consola devuelve diez números y puesto que range()
empieza a contar desde el 0, nos quedan los números del
0 al 9 (diez en total).
Esto nos ahorra código si lo comparamos con los ejemplos
anteriores y además, por defecto incrementa el valor de x,
no hay que especificarlo como hacíamos en otros códigos.
El rango se ha reducido.
Esta vez no empieza a contar desde el 0, si no que lo hace
desde el 5.
El número 10 no lo incluye. Si quieres que cuente hasta 10,
deberás ponerle un 11 en el rango.
Puedes darle un tercer parámetro para especificar el
incremento o decremento, solo tienes que poner un número
positivo o negativo"""

for x in range(7,701,100): #x itera de 7 a 700 en incrementos 100
    print (x)