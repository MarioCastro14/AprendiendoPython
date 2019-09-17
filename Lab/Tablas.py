#Tablas.py
#Autor: Mario Castro
#Fecha de realización: 17/09/2019


#Aqui le estamos dando el número base para que las multiplicaciones se hagan
#con un número en especifico.
for i in range(1,11):
    encabezado="Tabla del {}"
    print(encabezado.format(i))
    #Mandamos un print para que elabore la información que le hemos dado arriba
    print()

    #Dentro de este for necesitamos hacer otro
    for j in range(1,11):
        #El i será el numero de base, el que no va a cambiar
        #la letra j tendrá que subir de 1 en 1 hasta parar en el 10 en la tabla.
        tabla="{} x {} = {}"
        print(tabla.format(i,j,i*j))
    else:
        #al terminar las iteraciones ejecutamos un print para dar un salto
        #de linea
        print()
