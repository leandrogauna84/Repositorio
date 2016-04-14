# -*- encoding: utf-8 -*-
print("===================================")
print("     ORDEN ASCENDENTE")
print("===================================")

print("\nVamos a ingresar 3 valores y ordenarlos:")
print("------------------------------------------")

num1 = input("\nIngrese primer valor: ")
num2 = input("\nIngrese segundo valor: ")
num3 = input("\nIngrese tercer valor: ")

print("------------------------------------------")

if num1 <= num2:     # 1 es el más chico
    if num1 <= num3: # 1 sigue siendo el más chico
        if num2 <= num3:
            print("El orden es: ", num1, num2, num3)
        else:
            print("El orden es: ", num1, num3, num2)
    else:            # 3 ahora es el más chico
        print("El orden es: ", num3, num1, num2)
elif num2 <= num3:  # 2 es más chico 
    if num1 <= num3:
        print("El orden es: ", num2, num1, num3)
    else:
        print("El orden es: ", num2, num3, num1)
else:               # 3 es el más chico.
    print("El orden es: ", num3, num2, num1)

print("__________________________________________")
