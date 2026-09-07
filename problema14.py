#La politica de la compañia telefonica "chimefon" es: "Chismea + X -". Cuando se realiza una llamada, el cobro es por el tiempo que esta dura, de tal forma que los primeros cinco minutos cuestan $1 peso c/u, los siguientes tres, 80 centavos de peso c/u, los siguientes dos minutos 70 centavos de peso c/u, y a partir del decimo minuto, 50 centavos de peso c/u. Ademas se carga un impuesto del 3% cuando es domingo, y si es dia habil, en turno matutino, 15% y en turno vespertino, 10%. Realice un algoritmo para determinar cuanto debe pagar por cada concepto una persona que realiza una llamada en moneda nacional mexicana (MXN)
minutos=int(input("Minutos de la llamada: "))
dia=input("Dia de la semana: ")
turno=input("Turno vespertino o matutino?: ")
cobro=0
if minutos<5:
	cobro=1
elif minutos<8:
	cobro=0.8
elif minutos<10:
	cobro=0.7
else:
	cobro=0.5
semitotal=cobro*minutos

if dia=="domingo":
	impuesto=(semitotal*3)/100
	elif turno=="matutino":
		impuesto=(semitotal*15)/100
	else:
		impuesto=(semitotal*10)/100

total=semitotal+impuesto

print(f"El costo de la llamada es de: {total}")
"""
Una modificacion del codigo anterior, en esta otra version le pide al usuario el dia y el turno para determinar el impuesto
si no es domingo inmediatamente se va a la seccion de dia habil
y si no es turno matutino el programa interpreta que es turno vespertino y aplica ese descuento
"""