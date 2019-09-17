#Acumulado.py
#Autor: Mario Castro
#Fecha de realización: 17/09/2019

#Declaramos las variables.

acumulado= int(0)
numero=str("")

#Iniciamos un while como True, para hacer que el ciclo
#Sea incapaz de romperse hasta que se cumpla break

while True:
    numero=input("Dame un número entero: ")
    if numero == "":
        #Aqui creamos el break, por si el espacio es vacío
        #termine la condición
        break
    else:
        #en caso de que el usuario haya puesto un número, iremos
        #acumulando sus números.
        acumulado+=int(numero)
        salida="Su monto acumulado es: {}"
        print(salida.format(acumulado))
