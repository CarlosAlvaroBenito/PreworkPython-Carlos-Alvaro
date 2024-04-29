'''Ejercicio 20: Suma de Números en una Lista
Crea un programa que sume todos los números en una lista ingresada por el usuario.'''

Lista = [int(input('Introduce el primer número: ')) + int(input('Introduce el segundo número: ')) + int(input('Introduce el tercer número: ')) + + int(input('Introduce el cuartoo número: '))]

suma_de_numeros = sum(Lista)

print(f' La suma de números de la lista es: {suma_de_numeros}')