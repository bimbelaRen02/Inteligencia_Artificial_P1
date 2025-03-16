"""El condicional if a a ejecutar
un determinado código solo si se
cumplen una o varias condiciones.
Nombre del operador /	Descripción
>	Mayor que
<	Menor que
>=	Mayor o igual que
<=	Menor o igual que
==	Igual que
!=	Diferente que """

num_1 = 15
num_2 = 20
num_3 = 1450
num_4 = 60

if num_1 == num_2:
    print('Los números son iguales')

if num_1 < num_2:
    print('El número 1 es menor que el 2')

if num_3 < num_4:
    print('El número 3 es menor que el 4')

if num_3 > num_4:
    print('El número 3 es mayor que el 4')

if num_3 != num_4:
    print('El número 3 es diferente que el 4')

num_3 = 60
if num_3 != num_4:
    print('El número 3 es igual que el 4')