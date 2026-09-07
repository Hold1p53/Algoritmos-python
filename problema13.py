#La politica de la compañia telefonica "chimefon" es: "Chismea + X -". Cuando se realiza una llamada, el cobro es por el tiempo que esta dura, de tal forma que los primeros cinco minutos cuestan $1 peso c/u, los siguientes tres, 80 centavos de peso c/u, los siguientes dos minutos 70 centavos de peso c/u, y a partir del decimo minuto, 50 centavos de peso c/u. Determinar cuanto debe pagar por cada concepto una persona que realiza una llamada en moneda nacional mexicana (MXN)
minutos=int(input("Minutos de la llamada: "))
cobro=0
if minutos<5:
	cobro=1
elif minutos<8:
	cobro=0.8
elif minutos<10:
	cobro=0.7
else:
	cobro=0.5
total=cobro*minutos

print(f"El costo de la llamada es de: {total}")
"""
Un programa bastante sencillo, recibe los datos de cuantos minutos duro la llamada del usuario
luego determina el pago por un metodo de eliminacion con los if, elifs, y elses,
y al final devuelve al usuario el resultado sin importar que
"""