'''Ejercicio 18: Contador de Palabras
Ejercicios Introducción a Python: Enunciados 3. Crea un programa que cuente la cantidad de palabras en una oración ingresada por el usuario.'''

count=0
texto = input("Ingrese una texto: ")
palabras = texto.split()
count = 0
for i in palabras:
    count+=1
print (f'El numero de vocales es: {count}')