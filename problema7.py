#Almacenes "El harapiento distinguido" tiene una promocion: a todos los trajes que tienen un precio superior a $2500 se les aplicara un descuento de 15%, a todos los demas se les aplicara solo 8%. Realice un algoritmo para determinar el precio final que debe pagar una persona por comprar un traje y de cuanto es el descuento que obtendra
costraje=int(input("Ingrese el precio del traje: "))
if costraje>2500:
	porcentaje=15
	descuento=(costraje*15)/100
else:
	porcentaje=8
	descuento=(costraje*8)/100
total=costraje-descuento
print(f"El precio final del traje es de: {total} aplicando un {porcentaje}% de descuento")
"""
Lo que hace este programa es pedirle el precio del traje (nuevamente un sistema extremadamente engañable)
a el usuario y ese al ingresar un precio mayor a 2500 (exclusivamente mayor porque asi lo especifica el problema)
se aplicara un descuento de 15%, de lo contrario sera un descuento del 8%
al final el programa le imprime al usuario el total de su compra y cual porcentaje de descuento recibio dependiendo del precio
"""