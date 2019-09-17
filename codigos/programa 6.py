cantidadnombres= int(input("¿Cuantos nombres vas a registrar?:\n"))

nombresfamiliares=[]


for nombrefamiliar in range(1, cantidadnombres +1):
    nombrefamiliar=(input("¿Cúal es el nombre?\n"))
    nombresfamiliares.append(nombrefamiliar)

numerofamiliares= int(input("¿Cuantos familiares introduciste?\n"))

if numerofamiliares== cantidadnombres:
    print(nombresfamiliares)





