'''Ejercicio 7: Calculadora Simple
Crea un programa que realice operaciones aritméticas simples (suma, resta,
multiplicación, división) según la elección del usuario.'''

def suma(a,b):
  return a+b
def resta(a,b):
  return a-b
def multiplicacion (a,b):
 return a*b
def division (a,b):
 return a/b
while True:
  try:
      operacion = int(input("Introduce la operación a realizar: ""\n1. Suma\n2. Resta\n3. Multiplicación\n4. División\n"))
      if(operacion <=4 and operacion>0):
        break
  except:
    print("Operación no válida")
numero1 =float(input("Introduce el primer número: "))
numero2 =float(input("Introduce el segundo número: "))

if operacion ==1:
  resultado = suma(numero1,numero2)
elif operacion ==2:
  resultado = resta(numero1,numero2)
elif operacion ==3:
  resultado = multiplicacion(numero1,numero2)
elif operacion ==4:
  resultado = division(numero1,numero2)
else:
  print("La operación no es válida")
  
print(f'Resultado es: {resultado}')