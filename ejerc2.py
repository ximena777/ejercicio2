lista1=[]
inicio=int(raw_input("Ingrese el Rango Incial: "))
fin=int(raw_input("Ingrese el Rango Final: "))
con=inicio
while con<=fin:
	lista1=lista1+[con]
	con=con+1
else:
	print lista1
	lista2=[]
	con=inicio
	con2=0
	while con<=fin:
		if lista1[con2]%2==0:
			lista2=lista2+[lista1[con2]]
		con=con+1
		con2=con2+1
	else:
		print lista2