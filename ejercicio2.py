'''Ejercicio 2: Calculadora de Propina
Crea un programa que calcule el monto total a pagar en un restaurante, incluyendo
una propina del 15% sobre el total de la cuenta.'''

primer_plato = float(input("El primer Plato cuesta: "))
segundo_plato = float(input("El segundo Plato cuesta: "))
postre = float(input("El postre cuesta: "))
bebidas = float(input("Las bebidas cuestan: "))
Cuenta = round((primer_plato + segundo_plato+postre+bebidas),2)
Cuenta_con_propina = round ((Cuenta*1.15),2)
print(f'El total de la cuenta es: {Cuenta}')
print(f'El total de la cuente incluyendo un 15% de propina es: {Cuenta_con_propina}')
