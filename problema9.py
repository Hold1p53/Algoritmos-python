#Determina el promedio que obtendra un alumno considerando que realiza tres examenes de los cuales el primero y el segundo tienen una ponderacion del 25%, mientras que el tercero es de 50%
examuno= int(input("Introduce la primera calificacion: "))
examos= int(input("Introduce la segunda calificacion: "))
exames= int(input("Introduce la tercera calicifacion: "))

ponderacion1=(examuno+examos)*0.25
ponderacion2=exames*0.5
promedio=(examuno+examos+exames)
print(f"Su promedio final es de: {promedio} y su ponderacion es de: 50%: {ponderacion1}  25%: {ponderacion2}")
"""
Se piden tres calificaciones de tres examenes diferentes para que el programa los analice
se considera una ponderacion del 25% a los primeros dos y por lo mismo se juntan en la misma operacion
en el tercero se realiza una variable diferente solo para el
el promedio no se divide entre 3 ya que todo el proceso de la regla de 3 ya fue hecha en las ponderaciones
nota:supongo que el programa es para el profesor? si no este seria increiblemente otro sistema extremadamente engañable
"""