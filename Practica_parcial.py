                                # Recursividad

#Ejercicio 10

# def suma_digitos(numero):
#     if (numero <= 9):
#         return 1
#     else:
#         return (suma_digitos(numero / 10 ) + 1)

# print (suma_digitos(56732))


#Ejercicio 11



# def invertir_numero(numero , inverso = 0):
#     if (numero < 10):
#         return inverso + numero
#     else:
#         inverso = inverso * 10 + ((numero % 10) * 10)
#         return invertir_numero((numero // 10) , inverso)

# print (invertir_numero(451))


                                        #Pila

from pila import Pila

#Ejercicio 11

import string
import random

# pila_letras = Pila()
# pila_aux = Pila()
# cont = 0

# vocal = ["a", "e", "i", "o", "u"]

# for i in range (0, 10):
#     letra = random.choice(string.ascii_letters)
#     pila_letras.apilar(letra.lower())
#     pila_aux.apilar(letra.lower())
    
# while (not pila_letras.pila_vacia()):
#     letra = pila_letras.desapilar()
#     if (letra in vocal):
#         cont += 1

    


# while (not pila_aux.pila_vacia()):
#          x = pila_aux.desapilar()     
#          print (x)

# print()
# print (cont)




#Ejercicio 14

# pila_numeros = Pila()
# pila_aux = Pila()



# for i in range (0,3):
#     numero = input()
#     if (pila_numeros.pila_vacia()):
#         pila_numeros.apilar(numero)
#     else:
#         if (numero >= pila_numeros.elemento_cima()):
#             pila_numeros.apilar(numero)
#         else:
#             while (not pila_numeros.pila_vacia() and pila_numeros.elemento_cima() > numero ):
#                 pila_aux.apilar(pila_numeros.desapilar())

#             pila_numeros.apilar(numero)

#             while (not pila_aux.pila_vacia()):
#                 pila_numeros.apilar(pila_aux.desapilar())



# print()

# while (not pila_numeros.pila_vacia()):
#          x = pila_numeros.desapilar()     
#          print (x)




                                #Listas





from lista import Lista


# Ejercicio 1
# Contar la cantidad de nodos dentro de una lista


# lista = Lista()


# for i in range (0,10):
#     dato = random.randint(0,100)
#     lista.insertar(dato)

# print (lista.tamanio()) // Solicitado del ejercicio //
# print()
# lista.barrido()

# Ejercicio 2

# lista = Lista()
# from random import randint

# vocales = ["A", "E", "I", "O", "U"]


# for i in range (0, 10):
#     letra = chr(randint(65, 90))
#     lista.insertar(letra)

# lista.barrido()

# for vocal in vocales:
#     aux = lista.eliminar(vocal)
#     while (aux is not None):
#         aux = lista.eliminar(vocal)




#  lista.barrido_eliminando(vocales)    // Este método elimina sólo una de las vocales repetidas, la primera encontrada.

# print()

# lista.barrido()

#Ejercicio 3

# from random import randint
# lista_numeros = Lista()
# lista_pares = Lista()


# for i in range (0, 10):
#     numero = randint(0,100)
#     if (numero % 2 == 0 ):
#         lista_pares.insertar(numero)
#     else:
#         lista_numeros.insertar(numero)

# lista_numeros.barrido()
# print()
# lista_pares.barrido()

#Ejercicio 4

