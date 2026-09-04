#Una empresa importadora desea determinar cuantos dolares puede adquirir con equis cantidad de dinero mexicano
dolar=19.96
pesos=float(input("Ingrese la cantidad de pesos mexicanos a convertir: "))

conversion=pesos/dolar

print(f"La conversion de pesos a dolares es de {conversion} dolares")
"""
Lo que va a hacer esta linea de comandos de python es pedirle al usuario la cantidad de pesos mexicanos que desea convertir a moneda estadounidense
luego de eso el programa divide los pesos mexicanos entre la cantidad necesaria de pesos mexicanos para comprar un dolar
y finalmente devuelve el dato obtenido al usuario con "print()"
"""