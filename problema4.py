#La compañia de autobuses "La curva loca" requiere determinar el costo que tendra el boleto de un viaje sencillo, esto basado en los kilometros por recorrer y en el costo por kilometro. Costo por km: $80.00mxn
costokm=80
kilometros=float(input("Ingrese la cantidad de kilometros a recorrer"))
costoviaje=costokm*kilometros
print(f"El costo del viaje es de ${costoviaje}")
"""
Lo que va a hacer este programa es pedirle al usuario los kilometros que recorrera para el viaje ya que con estos
el programa hace una multiplicacion por el precio de cada kilometro a recorrer para que finalmente
le imprima al usuario el costo de su viaje
nota: este programa pudo ser mas sofisticado usando redondeos para kilometros fraccionarios pero se mantuvo sencillo
por motivos educativos
"""