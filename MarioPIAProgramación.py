#a) Definimos una clase, en este caso "Videojuegos", para poder guardar todos los datos
from operator import attrgetter
import json
class Videojuegos:
    nombre=""
    genero=""
    def __init__(self, nombre, genero):
        self.nombre=nombre
        self.genero=genero
    def MostrarContenido(objeto):
        print(objeto.nombre)
        print(objeto.genero)
        

        
#b) Creamos una lista, en este caso "Biblioteca de juegos", donde guardaremos la lista
#de los juegos que iremos colocando.
bibliotecajuegos= []
cantidadjuegos=()


#c)Insertamos unos cuantos videojuegos a la lista.
bibliotecajuegos.append(Videojuegos("Counter Strike: Global Offensive", "Acción, Estrategia"))
bibliotecajuegos.append(Videojuegos("Call Of Duty Modern Warfare", "Acción"))
bibliotecajuegos.append(Videojuegos("Fortnite", "Battle Royale"))
bibliotecajuegos.append(Videojuegos("Red Dead Redemption 2", "Acción, Aventura"))
bibliotecajuegos.append(Videojuegos("Minecraft", "Aventura, Construcción"))
bibliotecajuegos.append(Videojuegos("Grand Theft Auto V", "Acción"))


#d)Mostramos los datos de las propiedades de la clase.

print ("------Los valores de las propiedades de la clase------")

pjuego1=Videojuegos("Counter Strike: Global Offensive", "Acción, Estrategia")
pjuego2=Videojuegos("Call Of Duty Modern Warfare", "Acción")
pjuego3=Videojuegos("Fortnite", "Battle Royale")
pjuego4=Videojuegos("Red Dead Redemption 2", "Acción, Aventura")
pjuego5=Videojuegos("Minecraft", "Aventura, Construcción")
pjuego6=Videojuegos("Grand Theft Auto V", "Acción")
MostrarContenido=(pjuego1, pjuego2, pjuego3, pjuego4, pjuego5, pjuego6)
print(MostrarContenido)


#e) Ordenar los elementos de la clase, en este caso de manera alfabeticamente.
bibliotecajuegos.sort(key=attrgetter("nombre"),reverse=False)

#f)Mostramos el contenido de la lista.
print("-------------------------------------------------------")
print("El Contenido de la lista: ")
for juego in bibliotecajuegos:
    print(juego.nombre)
    print(juego.genero)
    print("----------")
#g)Serializamos el contenido de la lista a tipo JSON
print("-----------SERIALIZACIÓN A JSON-----------")
print(bibliotecajuegos)

json_data= json.dumps(bibliotecajuegos, default=lambda o: o.__dict__, indent=4)
print(json_data)
