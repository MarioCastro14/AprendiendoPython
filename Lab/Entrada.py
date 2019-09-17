#Entrada.py
#Autor: Mario Castro
#Fecha de realización: 17/09/2019

#Declaramos una variable que recibirá un valor y mostraremos el tipo de dato que es.
entrada=input()

print(type(entrada))

#La variable booleana puede darnos el resultado después de verificar
#si lo que obtuvimos como respuesta fue un dígito y si es que se encuentra
#en un punto. De detectar un punto detectará que es un numero de tipo float.
#Si find retorna -1 es porque no se encontró ningún punto decimal. Si el Entero
#Es True es porque lo que recibimos fue un entero.

Entero=(entrada.isdigit() and entrada.find(".")==-1)
if (Entero):
    #Si la condición es verdadera, se ejecutara el print, sino pasara a else.
    print("El dato es entero. ¡Muy bien")
else:
    #Si no se cumplió el if, es porque entonces se tiene que cumplir esta.

    print("Dato no es entero. Intenta nuevamente.")
