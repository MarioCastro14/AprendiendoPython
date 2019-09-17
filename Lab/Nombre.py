#Nombre.py
#Autor: Mario Castro
#Fecha de realización: 17/09/2019

#Preguntamos el nombre por medio de dos variables.

nombre= input("Nombre: ")
apellidos= input("Apellidos: ")

#Combinamos las dos variables en una, ambos valores str con literal " "
#para dejar un espacio.

nombreCompleto= nombre+" "+apellidos

#Usamos upper para convertir todas las letras del nombre a mayusculas.

nombreCompleto=nombreCompleto.upper()
print(nombreCompleto)
