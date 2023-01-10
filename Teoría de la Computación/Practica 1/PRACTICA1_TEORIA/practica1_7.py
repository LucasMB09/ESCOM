repetido = []
noRepetido = []
 
valores = input("Ingresa una cadena de numeros: ")

if len(valores) > 5:
	for x in valores:
		if x not in noRepetido:
			noRepetido.append(x)
		else:
			if x not in repetido:
				repetido.append(x)
	if len(repetido) > 0:
		print("Cadena valida")
	else:
		print("Cadena no valida")
else:
	print("Introduce una cadena valida")