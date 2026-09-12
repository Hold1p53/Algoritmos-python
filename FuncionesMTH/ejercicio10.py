#Implementa una funcion llamada operacion_basica(a,b,operacion) donde a y b son operandos numericos y la operacion es una cadena. Usa ramas condicionales para comparar el texto: si vale "suma", devuelve a+b, si vale "resta" devuelve a-b, si vale "multiplica", devuelve a*b, si el texto recibido no coincide con ninguna de estas opciones, debe retornar "operacion no valida"
def operacion(a,b,op):
	if op=="suma":
		print(a+b)
	elif op=="resta":
		print(a-b)
	elif op=="multiplicacion":
		print(a*b)
	elif op=="division":
		print(a/b)
	else:
		print("operacion no valida")
operacion(12,2,"suma")
operacion(12,2,"resta")
operacion(12,2,"multiplicacion")
operacion(12,2,"division")
operacion(12,2,"raiz")
"""
este es un algoritmo algo mas complejo, pero nada que no se pueda hacer en unos minutos
ahora me justifico que la funcion y los critetios tienen un nombre mas corto
debido a que tenia que ser rapido para completar esta funcion primero
ademas el profesor, adicionalmente nos pidio incluir division a pesar de que el problema no lo menciona
"""