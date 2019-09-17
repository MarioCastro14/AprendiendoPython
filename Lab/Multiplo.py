#Multiplo.py
#Autor: Mario Castro
#Fecha de realización: 17/09/2019

#Pedimos números y los almacenamos despues de convertirlos a int

numero=int(input("Dame un número entero multiplo de 3 y 5, o 7: "))
#Almacenamos el residuo de la evaluación en valores booleanos
#Si el residuo es cero quiere decir que el numero si es multiplo

Multiplo3=((numero%3)==0)
Multiplo5=((numero%5)==0)
Multiplo7=((numero%7)==0)

#Usaremos un and para que el resultado sea verdadero siempre y cuando
#los demas tambien sean verdaderas. El or tiene la función de dar verdadero
#Siempre y cuando uno se cumpla. Los parentesis distinguen
#Cuales condiciones están juntas.

if ((Multiplo3 and Multiplo5) or Multiplo7):
    print("Correcto.")
else:
    print("Incorrecto.")
