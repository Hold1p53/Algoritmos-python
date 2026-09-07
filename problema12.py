#"La langosta ahumada" es una empresa dedicada a ofrecer banquetes; sus tarifas son las siguientes: el costo de platillo por persona es de $95, pero si el numero de personas es mayor a 200 pero menor o igual a 300 personas el costo es de $85. Para mas de 300 personas el costo por platillo es de $75. Se requiere un algoritmo que ayude a determinar el presupuesto que se debe presentar a los clientes que deseen realizar un evento.
costo=95
personas=int(input("Introduzca el numero de personas"))

if personas>=200:
	costo=85
	total=personas*costo
	print(f"El costo total es de: {total}")
elif personas>300:
	costo=75
	total=peronas*costo
	print(f"El costo total es de: {total}")
else:
	total=personas*costo
	print(f"El costo total es de: {total}")
"""
el costo por defecto se denominca como 95 y luego se le pide al usuario introducir el numero de personas para su evento
despues hace un progreso de eliminacion revisando que tan grande es el numero y asignarle el precio correspondiente
"""