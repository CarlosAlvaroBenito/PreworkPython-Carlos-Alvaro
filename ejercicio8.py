'''Ejercicio 8: Cálculo del Índice de Masa Corporal (IMC)
Escribe un programa que calcule el Índice de Masa Corporal (IMC) de una persona.'''

def imc(estatura,peso):
  return peso/ altura**2
peso = float(input("Escriba su peso en kg "))
altura = float(input("Escriba su estatura en m "))
indice = imc (peso, altura)

print(f'El índice de masa corporal es: {indice}')