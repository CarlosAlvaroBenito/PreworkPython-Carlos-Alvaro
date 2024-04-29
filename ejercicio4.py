'''Ejercicio 4: Contador de Vocales
Crea un programa que cuente el número de vocales en una palabra ingresada por el
usuario.'''

texto=str(input(("Introduce una palabra para contar sus vocales: ")))
vocales = "aeiouAEIOU"
conteo=0
for letra in texto:
  if letra in vocales:
   conteo += 1

print (f'El numero de vocales es: {conteo}')