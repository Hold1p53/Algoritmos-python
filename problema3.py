#Un estacionamiento requiere determinar el cobro que debe aplicar a las personas que lo utilizan. Considere que el cobro es con base en las horas que lo disponen y que las fracciones de hora se toman como completas
import math
preciora=20
horas=float(input("Ingrese la cantidad de horas que estuvo estacionado"))
minutos=float(input("Ingrese la cantidad de minutos estacionado"))
math.ceil(horas)
minutos=minutos/60
math.ceil(minutos)
costora=horas*preciora
costonuto=minutos*preciora
total=costora+costonuto
print(f"El costo total de su estadia es de ${total}")
"""
Aqui importamos la libreria math ya que es necesaria para usar el comando "ceil" el cual nos permite redondear al siguiente numero
si es que el anterior tiene un decimal, esto para cobrar las horas fraccionarias como completas
luego de hacer los calculos imprime para el usuario el costo total de su estadia en el estacionamiento
"""