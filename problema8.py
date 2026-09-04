#El director de una escuela esta organizando un viaje de estudios, y requiere determinar cuanto debe cobrar a cada alumno y cuanto debe pagar a la compañia de viajes por el servicio. La forma de cobrar es la siguiente: si son 100 alumnos o mas, el costo por cada alumno es de $65; de 50 a 99 alumnos, el costo es de $70, de 30 a 49, de $95, y si son menos de 30, el costo de la renta del autobus es de $4000 sin importar el numero de alumnos.
alumnos=int(input("Introduzca el numero de alumnos: "))
costo=0
if alumnos>=100:
	costo=65
elif alumnos>=50:
	costo=70
elif alumnos>=30:
	costo=95
else:
	alumnos=1
	costo=4000

print(f"El costo del viaje es de: {costo*alumnos}")
"""
en este programa introducimos los alumnos (este es un sistema menos engañable, le concedo eso)
y luego realizara un proceso de eliminacion dependiendo de la cantidad de alumnos para darnos el precio final
la razon por la que los alumnos se reducen a 1 si son menos de 30 es para poder colocar el costo de la renta
del autobus sin tener que definir mas variables
"""