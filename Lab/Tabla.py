#Tabla.py
#Autor: Mario Castro
#Fecha de realización: 17/09/2019

#Pediremos un número de entre el 1 al 9

numero=input("Dame un número del 1 al 9: ")
numero=int(numero)

#usamos for para ejecutar las veces que nosotros deseemos
#el segundo parámetro de range (11) no se incluye en la serie
#entonces el número real de range será del 1 al 10.

for i in range(1,11):
    #la i va variando a cada iteración.
    resultado="{} x {} = {}"
    print(resultado.format(numero,i,i*numero))
