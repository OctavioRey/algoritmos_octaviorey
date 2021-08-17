# Ejercicio 1
# Dado un vector con personaje de las películas
# de la saga de Stars Wars resolver:
# a. Realizar un barrido recursivo del vector.
# b. Realizar una función recursiva que permita
#    determinar si 'Yoda' está en el vector y en qué
#    posición.

personajes = ["Luke", "Anakin", "Yoda", "Leia"]

vector_prueba = personajes

def listar(vector):                 #Punto A
    if (len(vector) > 0):
        print(vector[0])
        listar(vector[1:])



listar(vector_prueba)

print()

def buscar_yoda(vector, pos):                           #Punto B
    if (len(vector) > 0 and (vector[pos] == "Yoda")):
        return pos
    else:
        return buscar_yoda(vector, pos+1)
   
print ("Yoda esta en la posicion: ", buscar_yoda(vector_prueba, 0))