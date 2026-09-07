#Se requiere determinar cual de tres cantidades proporcionadas es la mayor
numuno=int(input("Introduzca el primer numero: "))
numos=int(input("Introduzca el segundo numero: "))
numes=int(input("Introduzca el tercer numero: "))

mayor=0

if numuno>numos:
	if numuno>numes:
		mayor=numuno
	else:
		mayor=numes
elif numos>numes:
	mayor=numos
else:mayor=numes

print(f"El numero mayor es: {mayor}")
"""
Aqui el programa solicita tres numeros introducidos por el usuario y con ellos se realiza
un proceso de eliminacion buscando cual es el mayor con logica y al determinarlo se le asigna el valor 
de este numero a la variante "mayor"
"""