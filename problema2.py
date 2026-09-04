#Una empresa que contrata personal requiere determinar la edad de las personas que solicitan trabajo, pero cuando se les realiza la entrevista solo se les pregunta el año en que nacieron
año=2026
naciaño=int(input("Ingrese el año de nacimiento: "))

edad=año-naciaño
print(f"La persona deberia tener {edad} años")
"""
En este programa primero defini el año actual siendo 2026 ya que este fue el año en el que se realizo este programa
luego se introduce el año en que nacio la persona entrevistada
al final se resta el año de nacimiento con el año actual lo que nos deberia de dar la edad aproximada
cabe recalcar "aproximada" ya que aun faltaria el mes y dia para saber si esa persona ya cumplio años este año
"""