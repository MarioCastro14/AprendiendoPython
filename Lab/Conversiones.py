#Conversiones.py
#Autor: Mario Castro
#Fecha de realización: 17/09/2019

#Hay que declarar una variable str (texto), con una cadena de dígitos

numero="1234"

#Con print mostraremos el tipo de dato de la variable, tambien tenemos que usar type()

print(type(numero))

#Ahora convertiremos el número a int (valor númerico)

numero=int(numero)

#Verificamos que el número haya cambiado su tipo de dato igualmente que la primera vez.

print(type(numero))

#Declaramos una salida str, con una metasustitución {}, de esta forma
#las llaves se reemplazarán con el dato que nosotros seleccionemos.

resultado= "El número utilizado es {}"

#Se muestra el resultado, la meta sustitución colocará los valores en las llaves {}

print(resultado.format(numero))
