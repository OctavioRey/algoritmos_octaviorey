# Ejercicio 16
# Se tienen dos pilas con personajes de Star Wars, en una los del episodio V de “The empire
# strikes back” y la otra los del episodio VII “The force awakens”. Desarrollar un algoritmo que
# permita obtener la intersección de ambas pilas, es decir los personajes que aparecen en am-
# bos episodios.

from pila import Pila

personajes_v = ["Leia" , "Luke" , "Anakin" , "Jabba"]
personajes_vii = ["Obi Wan", "Anakin", "Jar Jar", "Luke", "R2D2"]
pila_v = Pila()
pila_vii = Pila()
pila_aux = Pila()


for i in range (0, len(personajes_v)):          # Cargamos la pila del episodio V
    pila_v.apilar(personajes_v[i])


for i in range (0, len(personajes_vii)):        # Cargamos la pila del episodio VII
    pila_vii.apilar(personajes_vii[i])


# pila_v        pila_vii    
#                       
#        Anakin              Anakin
                                
                       
while (not pila_v.pila_vacia()):
    if (pila_v.elemento_cima() == pila_vii.elemento_cima()):
        print ('El personaje' , pila_v.desapilar(), " se encuentra en ambas peliculas")
        pila_vii.desapilar()
        while(not pila_aux.pila_vacia()):
            pila_vii.apilar(pila_aux.desapilar())
    else:
        while (not pila_vii.pila_vacia() and pila_v.elemento_cima() != pila_vii.elemento_cima()):
            pila_aux.apilar(pila_vii.desapilar())
        
        if (pila_vii.pila_vacia()):
            pila_v.desapilar()
            while(not pila_aux.pila_vacia()):
                pila_vii.apilar(pila_aux.desapilar())

