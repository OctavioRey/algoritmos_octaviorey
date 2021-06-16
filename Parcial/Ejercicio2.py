# Ejercicio 2

from cola import Cola
from pila import Pila

class notificacion(object):
    
    def __init__(self, hora, app, mensaje):
        self.hora = hora
        self.app = app
        self.mensaje = mensaje

notificacion1 = notificacion("19:30", "Twitter", "Python es un quilombo")
notificacion2 = notificacion("17:32", "Facebook", "Vos sos loco?") 
notificacion3 = notificacion("13:45", "Facebook", "HOLA QUERIDO") 
notificacion4 = notificacion("19:20", "Instagram", "Juan te dio Like")
notificacion5 = notificacion("08:50", "Instagram", "Laura te dio Like") 
notificacion6 = notificacion("01:15", "Instagram", "Ricardo comento tu foto") 
notificacion7 = notificacion("20:18", "Instagram", "Pepito comento tu foto") 
notificacion8 = notificacion("23:50", "Instagram", "Esteban likeo tu comentario")  

cola_notificaciones = Cola()
pila_notificaciones = Pila()



cola_notificaciones.arribo(notificacion1)
cola_notificaciones.arribo(notificacion2)
cola_notificaciones.arribo(notificacion3)
cola_notificaciones.arribo(notificacion4)
cola_notificaciones.arribo(notificacion5)
cola_notificaciones.arribo(notificacion6)
cola_notificaciones.arribo(notificacion7)
cola_notificaciones.arribo(notificacion8)


def facebook():     # Punto C
    for n in range(0, cola_notificaciones.tamanio()):
        aux = cola_notificaciones.atencion()
        if ("Facebook" != aux.app):
            cola_notificaciones.arribo(aux)

print ("Notificaciones en facebook antes de limpiarlo: ", cola_notificaciones.tamanio())
facebook()
print("Notificaciones en facebook despues de limpiarlo: ", cola_notificaciones.tamanio())

def Mensaje():       # Punto D
    for i in range (0, cola_notificaciones.tamanio()):
        aux = cola_notificaciones.atencion()
        if (aux.app == "Twitter"):
            buscado = "Python"
            mensaje = aux.mensaje
            if (0 == mensaje.find(buscado)):
                print(mensaje)
        cola_notificaciones.arribo(aux)

print()
Mensaje()


def Instagram():        # Punto E
    for n in range (0, cola_notificaciones.tamanio()):
        aux = cola_notificaciones.atencion()
        if (aux.app == "Instagram"):
            pila_notificaciones.apilar(aux)
    while (not pila_notificaciones.pila_vacia()):
        print(pila_notificaciones.elemento_cima().mensaje, "a las: ", pila_notificaciones.elemento_cima().hora)
        pila_notificaciones.desapilar()

print()
Instagram()