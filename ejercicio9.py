'''Ejercicio 9: Conversor de Divisas
Ejercicios Introducción a Python: Enunciados 2
Crea un programa que convierta una cantidad de dólares a euros. Suponiendo que
1 dólar es igual a 0.85 euros.'''

cambio_dolares = float(input("Escriba la cantidad de dolares que quiere cambiar a euros"))

euros = 1 / 0.85 * cambio_dolares

print(f'El valor en Euros es: {euros}')