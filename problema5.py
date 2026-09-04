#Se requiere determinar el costo que tendra realizar una llamada telefonica con base en el tiempo que dura la llamada y en el costo por minuto. Costo por minuto: $3.00 mxn
costonuto=3
minutos=int(input("Ingrese los minutos que duró la llamada"))
costllamada=costonuto*minutos
print(f"El costo total de la llamada es de ${costllamada}")
"""
lo que hace el programa es pedirle al usuario los minutos que duró la llamada (un sistema extremadamente engañable)
y luego el programa hace una multiplicacion simple y imprime para el usuario el costo de su llamada
"""