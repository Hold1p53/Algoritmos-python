#Crea una funcion llamada calificar(nota) que reciba un numero decimal o entero que represente una calificacion de 0 a 100. utilizando una cadena de condiciones if/elif/else
#si la nota es mayor o igual a 90, retorna "A", si esta entre 80 y 89 inclusive, retorna "B", si esta entre 70 y 79 inclusive, retorna "C", si es menor estrictamente a 70, retorna "F"
nota=int(input("Ingrese la nota del estudiante: "))
def calificar(nota):
	if nota>=90:
		print("A")
	elif nota>=80:
		print("B")
	elif nota>=70:
		print("C")
	else:
		print("F")

calificar(nota)
"""
en muchos ejercicios por fin se ve una funcion usando un input del usuario
en este caso el usuario ingresa su propia calificacion y el algoritmo la incluye a la funcion
luego realiza toda la logica explicada antes y retorna la nota respectivamente
"""