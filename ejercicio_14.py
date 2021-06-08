#Ejercicio 14

# Realizar un algoritmo que permita ingresar elementos en una pila, y que estos queden orde-
# nados de forma creciente. Solo puede utilizar una pila auxiliar como estructura extra –no se

# pueden utilizar métodos de ordenamiento–.

from pila import Pila
from random import randint

pila_numeros = Pila()
pila_aux = Pila()


for i in range(0, 10):
    numero = randint(0,100)
    # Otra opción es usar el metodo expresado debajo con un ciclo while
    #numero = int(input("Ingrese el número a introducir en la pila: "))
    if(pila_numeros.pila_vacia()):
        pila_numeros.apilar(numero)
    else:
        if(numero >= pila_numeros.elemento_cima()):
            pila_numeros.apilar(numero)
        else:
            while(not pila_numeros.pila_vacia() and pila_numeros.elemento_cima() > numero):
                pila_aux.apilar(pila_numeros.desapilar())

            pila_numeros.apilar(numero)

            while(not pila_aux.pila_vacia()):
                pila_numeros.apilar(pila_aux.desapilar())


while (not pila_numeros.pila_vacia()):
    print (pila_numeros.desapilar())