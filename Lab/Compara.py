#Compara.py
#Autor: Mario Castro
#Fecha de realización: 17/09/2019

#primero solicitamos dos numeros a comparar

primernumero=input("Dame el primer numero: ")
segundonumero=input("Dame el segundo número: ")

resultado="Tus números son los siguientes: {} y {}, {}"

if primernumero == segundonumero:
    #Aqui comparamos en caso de que sean iguales
    print(salida.format(primernumero, segundonumero, "Los dos numeros son iguales"))
else:
    #En caso de que lo anterior no se cumpla usamos un else
    if primernumero>segundonumero:
        #En caso de que el numero uno sea mayor
        print(resultado.format(primernumero, segundonumero, "El primer numero es mayor"))
    else:
        #En caso de que el numero dos sea mayor
        print(resultado.format(primernumero, segundonumero, "El segundo numero es mayor"))
