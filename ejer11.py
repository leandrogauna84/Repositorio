print "_____________________________________________________"
print "*-       CALCULO DE SUELDO Y HORAS EXTRAS          -*"
print "_____________________________________________________"
print " "
print " "
print " "
print "_______________________________________________________________________________"
print " "
print " "
print " "


print '     Bienvendio!'


diastrabajados = input('\n Ingrese cuantos dias entre semana en el mes trabajo el empleado: ')
sueldo = float = (input('\n Ingrese el sueldo del trabajador: $'))
print '\n Eliga la opcion de horas extras de trabajo:'

print '\n\n - 1 Domingo con 3-5 hs extras.'
print '\n - 2 Domingo con 6-10 hs extras.'
print '\n - 3 Domingo con 3-10 hs extras.'
opcion = int (input('\n\n Seleccion: '))
if diastrabajados>=20:
	if (opcion == 1):
		print('\n El empleado recibira en 3% de bonificacion.')
		nuevoSueldo = ((sueldo*0.03) +sueldo)
		print '\n Su nuevo sueldo sera de: ', nuevoSueldo
	elif (opcion==2):
		print('\n El empleado recibira en 10% de bonificacion.')
		nuevoSueldo = ((sueldo*0.10) +sueldo)
		print '\n Su nuevo sueldo sera de: ', nuevoSueldo
elif opcion==3:
	print('\n El empleado recibira en 2% de bonificacion.')
	nuevoSueldo = ((sueldo*0.02) +sueldo)
	print '\n Su nuevo sueldo sera de: ', nuevoSueldo
else:
	print "NO RECIBE PAGO POR HORAS EXTRAS"


print " "
print " "
print "_______________________________________________________________________________"
print " "