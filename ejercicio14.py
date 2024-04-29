'''Ejercicio 14: Calculadora de Descuento
Crea un programa que calcule el precio final de un artículo después de aplicar un descuento del 20%.'''

numero = float(input("Introduce un número para aplicar un descuento del 20%: " ))
descuento = round(numero*0.20,2)
valor_con_descuento= round(numero-descuento,3)
print(f'El descuento del 20%: {descuento}')
print(f'El valor con descuento del 20%: {valor_con_descuento}')
