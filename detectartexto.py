import operator

def Ngrama(n, palabra):
	lista = []
	for x in range(len(palabra)-(n-1)):
		lista.append(palabra[x:x+n])	#Manda a una lista los ngramas

	dic = {}
	for w in lista:
		if ' ' in w or '\n' in w:
			pass
		else:
			dic.update({w : lista.count(w)}) #Se agrega en un diccionario el ngrama y se actualiza el numero de apariciones

	l = sorted(dic.items(), key=operator.itemgetter(1)) #Se acomoda de menor al mayor numero de apariciones en una lista
	l.reverse() #Se invierte la lista para que sea de mayor a menor el numero de apariciones
	return (l)

def detectar_idioma(texto):
	docesp = open('esp.txt', 'r')
	docing = open('ing.txt', 'r')
	docfran = open('frances.txt', 'r')
	documento_esp = docesp.read()	
	documento_ing = docing.read()	
	documento_fran = docfran.read()	
	
	espanol, ingles, frances = 0, 0, 0

	list_esp = Ngrama(3, documento_esp)
	list_ing = Ngrama(3, documento_ing)
	list_fran = Ngrama(3, documento_fran)	
	ngramas = Ngrama(3, texto)

	for x in range(150):
		esp_ngramas = list_esp[x][0]
		ing_ngramas = list_ing[x][0]
		fran_ngramas = list_fran[x][0]
		for a in range(len(ngramas)):
			esp = ngramas[a][0]
			if esp_ngramas == esp:
				espanol = espanol + 1

		for b in range(len(ngramas)):
			ing = ngramas[b][0]
			if ing_ngramas == ing:
				ingles = ingles + 1

		for c in range(len(ngramas)):
			fran = ngramas[c][0]
			if fran_ngramas == fran:
				frances = frances + 1

	if espanol > ingles and espanol > frances:
		print("El idioma es espanol")
	elif ingles > espanol and ingles > frances:
		print("El idioma es ingles")
	else:
		print("El idioma es frances")

	docesp.close()
	docing.close()
	docfran.close()

	
def mostrarNgramas(ngramas):
	num = int(input("\nCuantos ngramas desea ver? "))
	if num > len(ngramas):	print(ngramas) #Si el numero de ngramas que se desea ver es mayor al numero de ngramas se muestran todos
	else:
		for x in range(num): #Se muestra el numero de ngramas indicados
			print(ngramas[x]) 

def main():
	arch = open('ngramas.txt','w+')
	opc = input("\nDesea ingresar texto?\n1)Desde teclado\n2)Desde archivo\n$$")
	if opc == "1":
		texto = input("\nIngrese texto:\n$$")
		gramas_base = Ngrama(3, texto)
		detectar_idioma(texto)
	elif opc == "2":
		doc = input("\nIngrese nombre del archivo(Ej:archivo.txt):\n$$")
		d = open(doc, 'r')
		texto = d.read()
		detectar_idioma(texto)
		d.close()
	else:
		main()
	arch.close()

main()