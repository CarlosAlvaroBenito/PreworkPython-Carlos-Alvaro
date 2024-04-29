'''Ejercicio 10: Determinar el Día de la Semana
Escribe un programa que determine el día de la semana correspondiente a un
número ingresado por el usuario (1 para lunes, 2 para martes, etc.).'''

operacion = int(input("Introduce el numero del día de la semana: ""\n1. Lunes\n2. Martes\n3. Miercoles\n4. Jueves\n5. Viernes\n6. Sábado\n7. Domingo\n "))
if operacion ==1:
  print("Lunes")
elif operacion ==2:
    print("Martes")
elif operacion ==3:
    print("Miércoles")
elif operacion ==4:
    print("Jueves")
elif operacion ==5:
    print("Viernes")
elif operacion ==6:
    print("Sábado")
elif operacion ==7:
    print("Domingo")
else:
    print("día no existe")