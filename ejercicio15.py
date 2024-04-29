'''Ejercicio 15: Conversor de Tiempo
Escribe un programa que convierta un número de minutos en horas y minutos. Por ejemplo, 145 minutos serían 2 horas y 25 minutos.'''
tiempo=int(input("Introduce el número de minutos a convertir: "))
horas=tiempo//60
minutos=tiempo % 60
print(f'Los {tiempo} minutos transformados en horas y minutos son {horas} horas y {minutos} minutos')