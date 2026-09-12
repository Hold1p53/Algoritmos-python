#diseña una funcion llamada mayor_de_tres(a,b,c) que reciba tres numeros y determine cual es el mayor utilizando unicamente operadores logicos (and) y comparaciones (>=), sin emplear max()
def mayor3(numero1, numero2,numero3):
	if numero1>numero2 and numero1>numero3:
		print(numero1)
	elif numero2>numero1 and numero2>numero3:
		print(numero2)
	elif numero3>numero1 and numero3>numero2:
		print(numero3)
	else:
		print("todos los numeros son iguales")

mayor3(5,12,9)
mayor3(20,3,1)
mayor3(4,4,4)
"""
La funcion lee los tres numeros y luego evalua cual es el mayor con un proceso algo primitivo pero necesario
para no usar max() a este punto escribo lo que suene mas eficiente para el algoritmo, la mayoria de las veces
prefiero no usar underscore (_) porque lo considero una perdida de tiempo
"""
