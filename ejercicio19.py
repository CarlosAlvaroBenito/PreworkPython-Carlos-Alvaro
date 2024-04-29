'''Ejercicio 19: Verificación de Año Bisiesto
Escribe un programa que determine si un año ingresado por el usuario es bisiesto o no.'''

ano = int(input("Introduce el ano a comprobar:"))

if ano % 4 != 0:
	print("No es bisiesto")
elif ano % 4 == 0 and ano % 100 != 0:
	print("Es bisiesto")
elif ano % 4 == 0 and ano % 100 == 0 and ano % 400 != 0:
	print("No es bisiesto")
elif ano % 4 == 0 and ano % 100 == 0 and ano % 400 == 0:
	print("Es bisiesto")