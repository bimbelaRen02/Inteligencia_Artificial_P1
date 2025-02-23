age = int(input('¿Cuál es tu edad?\n'))

if age <= 0:
	print('Nadie puede tener esa edad (zopenco).')
elif age >= 1 and age < 18:
	print('Eres menor de edad (huele a cárcel).')
elif age >= 18 and age <= 45:
	print('Eres un adulto (ya agarra el pedo, ya tienes peleas en la arena coliseo).')
elif age > 45 and age <= 100:
	print('Eres muy adulto (a su mecha, ya estás vejete).')
elif age > 100 and age <= 120:
	print('Eres increíblemente anciano (ya estás robando oxígeno).')
else:
	print('O encontraste la fuente de la juventud eterna o estás mintiendo (o eres tonto para digitar tu edad).')