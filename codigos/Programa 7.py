mensaje= (str(input("¿Que palabra deseas saber si es palidromo? *Escribir en minusculas*: \n")))
mensajesinespacios= mensaje.replace(" ","")


reves = mensaje[::-1]

palidromo= mensaje

print ("El mensaje al revés es:")
print(reves)

revessinespacios=reves.replace(" ","")

if mensajesinespacios == revessinespacios:
    print("La palabra si es palidromo")
else:
    print("la palabra no es palidromo")
