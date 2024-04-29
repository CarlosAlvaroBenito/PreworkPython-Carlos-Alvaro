'''Ejercicio 13: Verificación de Número Primo
Escribe un programa que determine si un número ingresado por el usuario es primo o no.'''
numero = int(input("Introduce un número para comprobar si es primo: "))
def es_primo(numero):
  contador = 0
  for n in range(1, numero+1):
        if numero % n == 0:
          contador +=1
  if contador ==2:
        return ("Es número Primo")
  else:
        return ("No es número primo")
print(es_primo(numero))