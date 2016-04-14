print("*************************")
print("--------BIENVENIDO-------")
print("*************************")

print "_____________________________________________________"
print "*-              CALCULO DEL VALOR PROMEDIO         -*"
print "_____________________________________________________"
print " "
print " "
print " "
print "_______________________________________________________________________________"
print " "




print("\n\nVALORES")
valor1 = int(input("\nIngrese el primer valor: "))
valor2 = int(input("\nIngrese el segundo valor: "))
valor3 = int(input("\nIngrese el tercer valor: "))

print("\n\nPROMEDIO")
prom = (valor1 + valor2 + valor3) / 3

print "\nEl promedio de los 3 valores es: ",prom

print("\n\nVALORES MAYORES O MENORES AL PROMEDIO")
if (valor1 > prom):
	print "\nEl primer valor ", valor1, "es mayor al promedio"
	if (valor1 == prom):
		print "\nEl primer valor ", valor1, "es igual al promedio"
	#else:
		#print "El primer valor ", valor1, "es mayor al promedio"

print " "
print " "
print "_______________________________________________________________________________"
print "_______________________________________________________________________________"
print " "
print " "

if (valor2 >= prom):
	
	if (valor2 == prom):
		print "\nEl segundo valor ", valor2, "es igual al promedio"
	else:
		print "\nEl segundo valor ", valor2, "es mayor al promedio"

if (valor3 >= prom):
	
	if (valor3 == prom):
		print "\nEl tercer valor ", valor3, "es igual al promedio"
	else:
		print "\nEl tercer valor ", valor3, "es mayor al promedio\n\n"

		print " "
print " "
print " "
print "_______________________________________________________________________________"
print " "



