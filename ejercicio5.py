'''Ejercicio 5: Suma de Números Pares
Escribe un programa que calcule la suma de todos los números pares del 1 al 100.'''

n = 1
p = 0
while n <= 100:
  if n%2 == 0:
   print (n)
  if n%2 == 0:
    p += n
  n += 1
print (f'La suma de los pares es igual a: {p}')

