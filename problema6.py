#Determina cuanto pagara finalmente una persona por un articulo cualquiera, considerando que tiene un descuento de 20% y debe pagar 15% de IVA (debe mostrar el precio con descuento y el precio final), crea un menu para que el usuario elija entre 2 productos y el que elija, despliega el nombre del producto, precio, precio con descuento y precio final
cosa=input("Introduzca el articulo a comprar: Jugo (J), Agua (A)")
jugo=20
agua=10
if cosa=="J":
	cosa=jugo
elif cosa=="A":
	cosa=agua
else:
	print("Articulo invalido")

descuento=(cosa*20)/100
iva=(descuento*15)/100
semitotal=cosa-descuento
total=semitotal+iva

print(f"Articulo elejido: {cosa}")
print(f"Precio con descuento: {semitotal}")
print(f"Precio final (aplicando IVA): {total}")
"""
Este programa le da a elejir al usuario entre comprar jugo o agua y programe tambien un error para evitar que el usuario
elija otra cosa, despues si encuentra coincidencias con el articulo a comprar y la base de datos, le asignamos el articulo
saca el descuento y el IVA de ese mismo articulo y lo imprime en 3 lineas diferentes para simular el "menu"
"""