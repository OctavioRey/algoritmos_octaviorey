#! Ejercicio 1

from pila import Pila
from random import randint

""" pila_datos = Pila()
pila_aux = Pila()

for i in range(0, 100):
    num = randint(1, 100)
    print(num)
    pila_datos.apilar(num)

cantidad = 0
contar = int(input('ingrese el numero que desea contar '))        // Funciona

while(not pila_datos.pila_vacia()):
    x = pila_datos.desapilar()
    if(x == contar):
        cantidad += 1

print('cantidad de ocurrencias', cantidad) """

#! Ejercicio 2

""" pila_datos = Pila()
pila_aux = Pila()

for i in range (0, 10):
    num = randint(1, 50)
    print(num)
    pila_datos.apilar(num)

while(not pila_datos.pila_vacia()):
    x = pila_datos.desapilar()                // Funciona
    pila_aux.apilar(x)
    
print()

while (not pila_aux.pila_vacia()):
    x = pila_aux.desapilar()
    if (x % 2 == 0):
        pila_datos.apilar(x)
        print (x) """


#! Ejercicio 3






#! Ejercicio 5

""" pila_letras = Pila()
pila_aux = Pila()
pila_inversa = Pila()


palabra = input('Ingrese una palabra')

for letra in palabra:
    pila_letras.apilar(letra)

while(not pila_letras.pila_vacia()):
    x = pila_letras.desapilar()
    print (x)
    pila_aux.apilar (x)
    pila_inversa.apilar(x)

print ()

while (not pila_aux.pila_vacia()):
    x = pila_aux.desapilar()
    pila_letras.apilar(x)
    print (x)

while (not pila_letras.pila_vacia() and pila_letras.elemento_cima() == pila_inversa.elemento_cima()):
    pila_letras.desapilar()
    pila_inversa.desapilar()
  
if(pila_letras.pila_vacia()):
    print('La palabra ingresada es un palindromo')
else:
    print('Lo que ingresaste no es un palindromo') """

#! Ejercicio 10

# pila_dioses = Pila()
# pila_aux = Pila()

# pila_dioses.apilar('Zeus')
# pila_dioses.apilar('Helios')
# pila_dioses.apilar('Poseidon')
# pila_dioses.apilar('Ares')
# pila_dioses.apilar('Hermes')

# posicion_insertar = 4

# if (pila_dioses.tamanio() >= posicion_insertar):
#     pos = 0
#     while (not pila_dioses.pila_vacia() and pos < posicion_insertar):
#         pos += 1
#         pila_aux.apilar(pila_dioses.desapilar())
#     pila_dioses.apilar('Atenea')
#     while(not pila_aux.pila_vacia()):
#         pila_dioses.apilar(pila_aux.desapilar())
#     while(not pila_dioses.pila_vacia()):
#         print(pila_dioses.desapilar())


# else:
#     print ('La pila no tiene la cantidad de elementos necesarios')



#! Ejercicio 14

# pila_datos = Pila()
# pila_aux = Pila()

# numeros = [0, 3, 1, 7, 5, 10]


# for i in range(0, 6):
#     numero = numeros[i]
#     if(pila_datos.pila_vacia()):
#         pila_datos.apilar(numero)
#     else:
#         if(numero >= pila_datos.elemento_cima()):
#             pila_datos.apilar(numero)
#         else:
#             while(not pila_datos.pila_vacia() and pila_datos.elemento_cima() > numero):
#                 pila_aux.apilar(pila_datos.desapilar())

#             pila_datos.apilar(numero)

#             while(not pila_aux.pila_vacia()):
#                 pila_datos.apilar(pila_aux.desapilar())


# while (not pila_datos.pila_vacia()):
#     print (pila_datos.desapilar())

#! Ejercicio 13        Falta Terminarlo

class Traje(object):
    modelo, pelicula, estado = ' ' , ' ', ' '

    def __init__(self, modelo, pelicula, estado):
        self.modelo = modelo
        self.pelicula = pelicula
        self.estado = estado
    
    def __str__(self):
        return self.modelo + ' - ' + self.pelicula+ ' - ' +self.estado

pila = Pila()
pila_aux = Pila()

traje = Traje('Mark III', 'Iron Man I', 'Dañado')
pila.apilar(traje)
traje = Traje('Mark III', 'Iron Man I', 'Dañado')
pila.apilar(traje)
traje = Traje('Mark XLIV', 'Iron Man X', 'Dañado')
pila.apilar(traje)
traje = Traje('Mark III', 'Iron Man I', 'Dañado')
pila.apilar(traje)
traje = Traje('Mark III', 'Iron Man I', 'Dañado')
pila.apilar(traje)

control_traje = True

while(not pila.pila_vacia()):
    x = pila.desapilar()
    if (x.modelo == 'Mark XLIV'):                                               # Punto A
        print('El modelo MARK XLIV fue utilizado en ', x.pelicula)

    if(x.estado == 'Dañado'):
        print('El modelo ', x.modelo, ' resultó dañado.')                         # Punto B

    if (x.estado == 'Destruido '):                                              #Punto C
        print('El modelo ', x.modelo, ' resulto destruido')                
    else:
        pila_aux.apilar(x)
 
    if(x.pelicula == 'Capitan America: Civil War' or x.pelicula == 'Spiderman : Homecoming'):
        print(x.modelo, ' Es utilizado en las peliculas indicadas')

while (not pila_aux.pila_vacia()):
    pila.apilar(pila_aux.desapilar())

if(not control_traje):
    traje = Traje('Mark LXXXV', 'Avengers II', 'Dañado')
    pila.apilar(Traje)

while (not pila.pila_vacia()):
    print(pila.desapilar())

# print(pila.desapilar()[1])          # Lo que va dentro del corchete es el contenido de la lista en esa posición

#Ejercicio 17

from pila import Pila


pila_vocales = Pila()
pila_consonantes = Pila()
pila_simbolos = Pila()

vocales = ['a', 'e', 'i', 'o', 'u']

print ('Ingrese un parrafo que finalice en un punto: ')
parrafo = input()

for caracter in parrafo:
    if(caracter.lower() in vocales):
        pila_vocales.apilar(caracter)
    elif(ord(caracter.lower()) > 97 and ord(caracter.lower()) <= 122):
        pila_consonantes.apilar(caracter)
    else:
        pila_simbolos.apilar(caracter)

 #! Punto A   
print('Cantidad de vocales', pila_vocales.tamanio())
print('Cantidad de consonantes', pila_consonantes.tamanio())
print('Cantidad de simbolos', pila_simbolos.tamanio())



cantidad_numeros = 0
cantidad_blancos = 0

#! Punto E
print('cantidad de vocales y simbolos son iguales ?', pila_vocales.tamanio() == pila_simbolos.tamanio())

while(not pila_simbolos.pila_vacia()):
    letra = pila_simbolos.desapilar()
    if(letra == ' '):
        cantidad_blancos += 1
    elif(ord(letra) >= 48 and ord(letra) <= 57):
        cantidad_numeros += 1
        #break


#! Punto B y D
print('Cantidad de espacios en blanco: ', cantidad_blancos)
print('Cantidad de numeros: ', cantidad_numeros)

#Punto F letra z

while(not pila_consonantes.pila_vacia()):
    letra = pila_consonantes.desapilar()
    if(letra.lower() == 'z'):
        print ('Hay una z')
        #break
