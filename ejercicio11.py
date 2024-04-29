'''Ejercicio 11: Calculadora de Edad
Escribe un programa que solicite al usuario su año de nacimiento y calcule su edad
actual.'''


Ano_nacimiento = int(input("Escriba su ano de nacimiento: "))
Ano_actual = int(input("Escriba el ano actual: "))

if Ano_nacimiento>=Ano_actual:
  print("Ano de nacimiento no válido")
else:
  Edad_Persona = Ano_actual-Ano_nacimiento
print(Edad_Persona)

