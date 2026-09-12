#escribe una funcion llamada mayor_de_edad(edad) que reciba un entero y retorne "mayor" si tiene 18 años o mas, y "menor" en caso contrario
def mayor_de_edad(edad):
	if edad>=18:
		print("Mayor")
	else:
		print("Menor")

mayor_de_edad(17)
mayor_de_edad(18)
mayor_de_edad(45)
"""
Este algoritmo deduce si una persona es mayor o menor de edad con un simple "if" y un "else"
no hay mucho que decir de estos algoritmos porque la mayoria son bastante sencillos
"""