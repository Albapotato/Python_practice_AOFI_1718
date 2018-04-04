numero1 = 0
numero2 = 0
numero3 = 0
print ("Dame 3 números para que pueda hacerte una suma")
numero1 = int (input("Dame un número mayor que 0:"))

if numero1 > 0:
	numero2 = int (input("Dame un número mayor que el anterior:"))
	if numero2 > numero1:
		numero3 = int (input("Dame un número menor que 0:"))
		if numero3 < 0:
			print (numero1, "+",numero2, "+", numero3, "=", numero1+numero2+numero3)
		else:
			print("Inténtalo de nuevo")
	else:
		print("No estás siguiendo las reglas")
else:
	print("No me estás haciendo caso.")