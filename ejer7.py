# -*- encoding: utf-8 -*-

print("===================================")
print("     Año Bisiesto")
print("===================================")

anio = input("\nIngrese año: ")


if ((anio % 400) == 0):
    esBisiesto = True
elif ((anio % 100) == 0):
    esBisiesto = False
elif ((anio % 4) == 0):
    esBisiesto = True
else:
    esBisiesto = False

print("\n-----------------------------------")
if (esBisiesto):
    print("El año ingresado es bisiesto.")
else:
    print("El año ingresado no es bisiesto")
print("___________________________________")
    
