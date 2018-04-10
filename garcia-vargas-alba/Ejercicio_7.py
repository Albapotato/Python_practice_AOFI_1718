import time
respuesta = 0
sino = "si"
lista =[]

while sino == "si":
	respuesta = input("Dame valores")
	lista.append(respuesta)
	sino = input("quieres añdir mas?si/no")
for i in lista:
	print(i)
	time.sleep (0.65)
