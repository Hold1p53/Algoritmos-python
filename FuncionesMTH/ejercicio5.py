#crea una funcion que devuelva el numero mas grande sin usar la funcion integrada max(). si son iguales, retorna cualquiera de los dos
def mayor2(numero1, numero2):
	if numero1>numero2:
		return numero1
	elif numero2>numero1:
		return numero2
	else:
		return "Ambos numeros son iguales"
print(mayor2(15, 27))
print(mayor2(40, -10))
print(mayor2(8, 8))
"""
en este caso me fui un poco fuera de lo que se solicito y agregue un escenario donde ambos numeros iguales
en el caso de que ambos sean iguales imprimira la frase indicada dentro de la funcion
"""