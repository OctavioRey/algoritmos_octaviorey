# Ejercicio 3

from lista import Lista

personajes = ["Hulk", "Black Widow", "Spider Man", "Thor", "Capitan America", "Scalet Witch"]
lista_auxiliar = ["Black Widow", "Hulk", "Rocket Racoon", "Loki"]
lista_personajes = Lista()

for personaje in personajes: 
    lista_personajes.insertar(personaje)



lista_personajes.barrido()
print()
print ("Thor se encuentra en la posicion: ", lista_personajes.busqueda("Thor"))    #Punto A
print()


lista_personajes.modificar_elemento(lista_personajes.busqueda("Scalet Witch"), "Scarlet Witch") #Punto B

lista_personajes.barrido()

print()
for personaje in lista_auxiliar:                   # Punto C
    if (lista_personajes.busqueda(personaje) == -1):
        lista_personajes.insertar(personaje)

print("Nueva lista con personajes auxiliares agregados:")
lista_personajes.barrido()

print()

lista_personajes.barrido_inverso()      # Punto D

print()
print ("En la posición 7 se encuentra: ", lista_personajes.obtener_elemento(7)) #Punto E

lista_personajes.barrido_personajes_letra()                    # Punto F


# Acá separé el ejercicio por mera comodidad, ya que me di cuenta al final que iba a tener que agregarle nuevos campos


personajes_completo = [
    {'name':'Thor','Anio Aparicion': 1995, 'Heroe': True },
    {'name':'Black Widow','Anio Aparicion': 2010, 'Heroe': True},
    {'name':'Capitan America','Anio Aparicion': 1997, 'Heroe': True},
    {'name':'Hulk','Anio Aparicion': 1967, 'Heroe': True},
    {'name':'Loki','Anio Aparicion': 1979, 'Heroe': False},
    {'name':'Rocket Racoon','Anio Aparicion': 2005, 'Heroe': True},
    {'name':'Spider Man','Anio Aparicion': 1970, 'Heroe': True},
    {'name':'Scarlet Witch','Anio Aparicion': 2011, 'Heroe': True},
]

lista_personajes_completo = Lista()                          # Punto G

for personaje in personajes_completo:
    lista_personajes_completo.insertar(personaje, "name")

print ("Lista ordenada por nombre:")
lista_personajes_completo.barrido()

print()

lista_personajes_completo.ordenar("Anio Aparicion")

print ("Lista ordenada por anio de aparicion:")
lista_personajes_completo.barrido()