#diseña una funcion llamada area_triangulo(base,altura) que calcule el area mediante la formula (baseXaltura)/2 y valide que ambos valores sean mayores a cero; si no lo son, debe retornar 0
def area_triangulo(base,altura):
	if base>0 and altura>0:
		area=(base*altura)/2
		print(area)
	else:
		print("0")
area_triangulo(10,5)
area_triangulo(7,4)
area_triangulo(-2,5)
"""
En este caso defini cualquier valor debajo de 0 o igual a 0 retornaria el valor 0 aunque la operacion no resulte en 0
esto evita que algun mal uso de la funcion resulte en otro resultado que no sea 0
"""