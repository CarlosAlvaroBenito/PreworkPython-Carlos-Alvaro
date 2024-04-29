'''Ejercicio 16: Contador de Números Pares e Impares
Crea un programa que cuente y muestre la cantidad de números pares e impares en
una lista ingresada por el usuario.'''

numeros = [1,2,3,4,5,6,7,8,9,10,11]
par=0
impar=0
for numero in numeros:
  if numero % 2 == 0:
    par+=1
  else:
   impar+=1
print(f'El número de números pares es {par} y el número de números impares es {impar}')