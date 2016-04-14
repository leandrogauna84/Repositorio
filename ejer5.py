
#Determinar en que tipo de jubilacion quedara una persona


#Ejercicio edad jubilatoria
print "_____________________________________________________"
print "*-  CALCULO DEL ANSES PERSONAS JUBILADAS ESTE ANIO -*"
print "_____________________________________________________"
print " "
print " "
print " "
print "_______________________________________________________________________________"
print " "
print "********************** "
print "*  EDAD JUBILATORIA  *"
print "********************** "
print " "
print " "

edad= input ("Ingrese la edad de la persona ")
antiguedad= input ("Ingrese la antiguedad en el empleo ")

if (edad >= 60):
  	if (antiguedad < 25):
  		print " *********************"
  		print "* JUBILACION POR EDAD *"
  		print "********************** "
  		print "  "
 		print "  "
 		print "A esta persona le corresponde la jubilacion por edad"
 	elif (antiguedad >= 25):
 		print " "
  		print "******************************** "
		print "* JUBILACION ANTIGUEDAD ADULTA *"
		print "******************************** "
		print " "
		print " "
		print "a esta persona le corresponde la jubilacion por antiguedad adulta"
elif (antiguedad >= 25):
	print "  "
	print "********************************"
	print "* JUBILACION ANTIGUEDAD JOVEN  *"
	print "******************************** "
	print " "
	print " "
	print "A esta persona le corresponde la jubilacion por antiguedad joven"
else:
	print ("_______________________________________________________")
	print ("Usted no se puede jubilar aun tiene menos de 60 anios")
	print ("_______________________________________________________")


