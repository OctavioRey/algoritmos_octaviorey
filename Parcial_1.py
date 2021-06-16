#Ejercicio 1
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



#Ejercicio 2

# from cola import Cola
# from pila import Pila

# class notificacion(object):
    
#     def __init__(self, hora, app, mensaje):
#         self.hora = hora
#         self.app = app
#         self.mensaje = mensaje

# notificacion1 = notificacion("19:30", "Twitter", "Python es un quilombo")
# notificacion2 = notificacion("17:32", "Facebook", "Vos sos loco?") 
# notificacion3 = notificacion("13:45", "Facebook", "HOLA QUERIDO") 
# notificacion4 = notificacion("19:20", "Instagram", "Juan te dio Like")
# notificacion5 = notificacion("08:50", "Instagram", "Laura te dio Like") 
# notificacion6 = notificacion("01:15", "Instagram", "Ricardo comento tu foto") 
# notificacion7 = notificacion("20:18", "Instagram", "Pepito comento tu foto") 
# notificacion8 = notificacion("23:5", "Instagram", "Esteban likeo tu comentario")  

# cola_notificaciones = Cola()
# pila_notificaciones = Pila()



# cola_notificaciones.arribo(notificacion1)
# cola_notificaciones.arribo(notificacion2)
# cola_notificaciones.arribo(notificacion3)
# cola_notificaciones.arribo(notificacion4)
# cola_notificaciones.arribo(notificacion5)
# cola_notificaciones.arribo(notificacion6)
# cola_notificaciones.arribo(notificacion7)
# cola_notificaciones.arribo(notificacion8)


# def facebook():     # Punto C
#     for n in range(0, cola_notificaciones.tamanio()):
#         aux = cola_notificaciones.atencion()
#         if ("Facebook" != aux.app):
#             cola_notificaciones.arribo(aux)

# print ("Notificaciones en facebook antes de limpiarlo: ", cola_notificaciones.tamanio())
# facebook()
# print("Notificaciones en facebook despues de limpiarlo: ", cola_notificaciones.tamanio())

# def Mensaje():       # Punto D
#     for i in range (0, cola_notificaciones.tamanio()):
#         aux = cola_notificaciones.atencion()
#         if (aux.app == "Twitter"):
#             buscado = "Python"
#             mensaje = aux.mensaje
#             if (0 == mensaje.find(buscado)):
#                 print(mensaje)
#         cola_notificaciones.arribo(aux)

# print()
# Mensaje()


# def Instagram():        # Punto E
#     for n in range (0, cola_notificaciones.tamanio()):
#         aux = cola_notificaciones.atencion()
#         if (aux.app == "Instagram"):
#             pila_notificaciones.apilar(aux)
#     while (not pila_notificaciones.pila_vacia()):
#         print(pila_notificaciones.elemento_cima().mensaje, "a las: ", pila_notificaciones.elemento_cima().hora)
#         pila_notificaciones.desapilar()

# print()
# Instagram()


#Ejercicio 3

# from lista import Lista

# personajes = ["Hulk", "Black Widow", "Spider Man", "Thor", "Capitan America", "Scalet Witch"]
# lista_auxiliar = ["Black Widow", "Hulk", "Rocket Racoon", "Loki"]
# lista_personajes = Lista()

# for personaje in personajes: 
#     lista_personajes.insertar(personaje)



# lista_personajes.barrido()
# print()
# print ("Thor se encuentra en la posicion: ", lista_personajes.busqueda("Thor"))    #Punto A
# print()


# lista_personajes.modificar_elemento(lista_personajes.busqueda("Scalet Witch"), "Scarlet Witch") #Punto B

# lista_personajes.barrido()

# for personaje in lista_auxiliar:                   # Punto C
#     if (lista_personajes.busqueda(personaje) == -1):
#         lista_personajes.insertar(personaje)

# lista_personajes.barrido()

# print()

# lista_personajes.barrido_inverso()      # Punto D

# print()
# print ("En la posición 7 se encuentra: ", lista_personajes.obtener_elemento(7)) #Punto E

# lista_personajes.barrido_personajes_letra()                    # Punto F


# Acá separé el ejercicio por mera comodidad, ya que me di cuenta al final que iba a tener que agregarle nuevos campos

# from lista import Lista

# personajes = [
#     {'name':'Thor','Anio Aparicion': 1995, 'Heroe': True },
#     {'name':'Black Widow','Anio Aparicion': 2010, 'Heroe': True},
#     {'name':'Capitan America','Anio Aparicion': 1997, 'Heroe': True},
#     {'name':'Hulk','Anio Aparicion': 1967, 'Heroe': True},
#     {'name':'Loki','Anio Aparicion': 1979, 'Heroe': False},
#     {'name':'Rocket Racoon','Anio Aparicion': 2005, 'Heroe': True},
#     {'name':'Spider Man','Anio Aparicion': 1970, 'Heroe': True},
#     {'name':'Scarlet Witch','Anio Aparicion': 2011, 'Heroe': True},
# ]

# lista_personajes = Lista()                          # Punto G

# for personaje in personajes:
#     lista_personajes.insertar(personaje, "name")

# print ("Lista ordenada por nombre:")
# lista_personajes.barrido()

# print()

# lista_personajes.ordenar("Anio Aparicion")

# print ("Lista ordenada por anio de aparicion:")
# lista_personajes.barrido()