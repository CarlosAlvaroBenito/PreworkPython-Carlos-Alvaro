'''Ejercicio 12: Calculadora de Área de un Rectángulo
Crea un programa que calcule el área de un rectángulo. El usuario debe ingresar la
longitud y el ancho del rectángulo'''

def Area(Largo,Ancho):
  return Largo * Ancho
Largo = float(input("Escriba el largo del rectángulo en centímetros: "))
Ancho = float(input("Escriba el ancho del rectángulo en centímetros: "))
Area_Rect= Area(Largo,Ancho)
print(f' El Área del rectángulo en centímetros es: {Area_Rect}')