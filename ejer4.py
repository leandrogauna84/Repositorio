# -*- coding: utf-8 -*-
print("===========================================")
print("		   FACTURACION ELECTRONICA            ")
print("==========================================")
print
print
total = input("Ingrese importe total: ")
impuestos = input("\nIngrese monto de impuestos: ")

print " "
print("_______________________________________________________________")
print " "

neto = total - impuestos

if (neto == 0):
	print("Error: Importe neto no puede ser cero.\n")
elif (neto < 0 ):
	print("Error: Los impuestos no deben superar al importe total\n")
elif ( neto > 5000 ):
	print("Monto Superado para Consumidor Final")
else:
	print("Importe neto a pagar: ", neto)


print " "
print " " 
print("______________________________________________________________")
