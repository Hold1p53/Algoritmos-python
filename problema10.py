#Determina cuanto se debe pagar por equis cantidad de lapices considerando que si son 1000 o mas el cossto es de 0.85; de lo contrario, el precio es de 0.90
costo=0.90
lapices=int(input("Introduzca el numero de lapices a comprar: "))

if lapices>=1000:
	costo=0.85

precio=lapices*costo

print(f"El total es de: {precio}")
"""
El precio se coloca en 0.9 por defecto ya que solo necesito checar cierta condicion
si esa condicion se cumple se modifica por el precio con descuento y al final muestra al usuario el precio sin importar la situacion
Me pregunto cual es la cantidad optima de lapices para comprar y sacar el mayor provecho de este sistema?
"""