

from cola import Cola
from random import randint



# cola_datos = Cola()
# cola_aux = Cola()

# for i in range (0,10):
#     num = randint(0,100)
#     cola_datos.arribo(num)
#     print(num)

# print()

# cantidad_elemento = 0

# while(cantidad_elemento < cola_datos.tamanio()):
#     dato = cola_datos.mover_final()
#     print(dato)
#     cantidad_elemento =+ 1


# while(not cola_datos.cola_vacia()):
#     dato = cola_datos.atencion()
#     cola_aux.arribo(dato)
#     print(dato)

# while (not cola_aux.cola_vacia()):
#     dato = cola_aux.atencion()
#     cola_datos.arribo(dato)


#Ejercicio 1

# cola_letras = Cola()
# palabra = input ('Ingrese una palabra')

# for letra in palabra:
#     cola_letras.arribo(letra.lower)()

# vocales = ['a', 'e', 'i', 'o', 'u']

# i, cantidad_elemento = 0 , cola_letras.tamanio()

# while(i < cantidad_elemento):
#     dato = cola_letras.atencion()
#     if(not dato in vocales):
#         cola_letras.arribo(dato)
#     i += 1
# cantidad_elemento = 0

# while(cantidad_elemento < cola_letras.tamanio()):
#     dato = cola_letras.mover_final()
#     print(dato)
#     cantidad_elemento =+ 1


# Ejercicio 2

# from pila import Pila

# datos = Cola()
# datos_aux = Pila()

# for i in range (0, 10):
#     num = randint(0, 100)
#     datos.arribo(num)
#     print(num)

# print ()

# while(not datos.cola_vacia()):
#     datos_aux.apilar(datos.atencion())

# while (not datos_aux.pila_vacia()):
#     datos.arribo(datos_aux.desapilar())

# cantidad_elemento = 0
# while(cantidad_elemento < datos.tamanio()):
#     dato = datos.mover_final()
#     print(dato)
#     cantidad_elemento += 1


# Ejercicio 4

def es_primo(num):
    for n in range(2, num):
        if num % n == 0:
            return False
    return True


datos_cola = Cola()

for i in range (0, 10):
    num = randint(0, 100)
    datos_cola.arribo(num)
    print(num)

print ()

i = 0 
cantidad_elemento = datos_cola.tamanio()


while(i < cantidad_elemento):
    numero = datos_cola.atencion()
    if(es_primo(numero)):
        datos_cola.arribo(numero)
    i += 1

cantidad_elemento = 0



while(cantidad_elemento < datos_cola.tamanio()):
    dato = datos_cola.mover_final()
    print(dato)
    cantidad_elemento += 1
    


