#Aleatorio.py
#Autor: Mario Castro
#Fecha de realización: 17/09/2019

#Python tiene librerías, las librerías nos ayudan a implementar codigos a nuestros proyectos.
#Las librerías son conocidas como modules (module)
#Para utilizar un modulo/librería en un programa Tenemos que
#importarlas, con la instrucción import.

import random

#Definimos una variable float con un valor ya asignado.

primernumero=float(10.5)

#En phyton las funciones son un conjunto de instrucciones que
#procesan una tarea.
#Las declaramos con instruccion def. Todo el codigo debajo de def
#Tiene que estar posicionado debajo del nombre de la función.

def miFuncion():
    #convertimos a float el número aleatorio generado por
    #random.randrange(). Solo se generará si importamos la libreria.

    segundonumero=float(random.randrange(1,10))

    #Se utiliza una meta sustitución para mostrar el resultado.
    mensaje="La suma de {} y {} es {}"
    print(mensaje.format(primernumero, segundonumero, primernumero+segundonumero))

#Ejecutamos la función que elaboramos al principio.

miFuncion()
