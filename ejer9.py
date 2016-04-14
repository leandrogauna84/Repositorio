
print "_____________________________________________________"
print "*-    CALCULO DE AREAS DE TRIANGULO Y CIRCULO      -*"
print "_____________________________________________________"
print " "
print " "
print " "
print "_______________________________________________________________________________"

print " "
print ("            Bienvenido!")
print ("\n Eliga una opcion: ")
print ("\n\n - 1 Triangulo.")
print ("\n - 2 Circulo.")

opcion = int (input ('\n Seleccion: '))


if (opcion == 1):
	print '\n Eligio la opcion triangulo.'
	baseT = float (input('\n Ingrese la base del triangulo: '))
	alT = float (input('\n Ingrese la altura del triangulo: '))
	areaT = baseT*alT

	print '\n\n El area del triangulo es: ',areaT

elif (opcion == 2):
	print '\n Eligio la opcion circulo.'
	radioC = float (input('\n Ingrese el radio del circulo: '))

	pi = 3.14
	areaC = pi*radioC

	print '\n\n El area del circulo es: ',areaC

else:
	print '\n Error, no es una opcion >:c'

print " "
print " "
print "_______________________________________________________________________________"