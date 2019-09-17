respuestacorrecta= ("A"  "B"  "C")

respuestacorrecta= True

mensaje =(input("Escriba una letra:\n"))
if mensaje== "A" or mensaje== "B" or mensaje== "C":
    print ("Hemos finalizado")
else:
    print("Letra incorrecta, inténtelo de nuevo")
    while respuestacorrecta == True:
        mensaje= (input("Escriba la letra A, B o C para cerrar:\n "))
        if mensaje== "A" or mensaje== "B" or mensaje== "C":
            respuestacorrecta=False
            print("Hemos finalizado")
