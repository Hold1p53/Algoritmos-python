#crea una funcion llamada obtener_signo(numero) que reciba un numero real o enter. mediante las ramas if, elif y else, clasifica el valor: retorna "positivo" si es mayor que cero, "Negativo" si es menor que cero, o "cero" si es exactamente igual a cero
def signo(numero):
	if numero>0:
		return "Positivo"
	elif numero==0:
		return "Cero"
	else:
		return "Negativo"
print(signo(12))
print(signo(-8))
print(signo(0))
"""
me pregunto si el profesor se moleste si uso otras nombres de funciones que las indicadas en el problema
no deberia afectar si cumple la funcion esperada no?
"""